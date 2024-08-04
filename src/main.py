import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.client.openAI_client import OpenAIClient
from src.utils.Excel import ExcelOperation
from src.utils.Image import ImageGeneration

if __name__ == '__main__':
    print("---------------------------------------------------------------------------------")
    print("|                  Welcome to 'Generating Image with AI' project :)             |")
    print("| Author : Alexis EGEA                                                          |")
    print("---------------------------------------------------------------------------------")
    print("\nTo use this project, you need an API key from OpenAI."
          "\nIf you don't have one, you can obtain it at https://platform.openai.com/api-keys")

    api_key_value = input("\nPlease enter you API key from OPENAI: ")
    openai_client = OpenAIClient(api_key=api_key_value)
    openai_client.initialize_client()
    print("The system is now ready for operation.")
    running_bool = True
    while running_bool:
        # update size image parameter
        size_image = input(
            "\nPlease, select what type of image by entering the corresponding number:\n"
            "1. Standard Image (1024x1024)\n"
            "2. Wide Image (1024x1792)\n"
            "3. Large Landscape (1792x1024)\n")

        if size_image == '1':
            size_image = "1024x1024"
        elif size_image == '2':
            size_image = "1024x1792"
        elif size_image == '3':
            size_image = "1792x1024"
        else:
            print("Invalid choice. Default size '1024x1024' selected.")
            size_image = "1024x1024"
        print(f"You selected an image size: '{size_image}'.")

        quality = input(
            "\nPlease, select the quality of image by entering the corresponding number:\n"
            "1. standard \n"
            "2. hd\n")
        if quality == '1':
            quality = "standard"
        elif quality == '2':
            quality = "hd"
        else:
            print("Invalid choice. Default quality 'standard' selected.")
            quality = "standard"
        print(f"You selected the quality: '{quality}'.")

        # update the model using the size inputed
        openai_client.model.update_model(size=size_image, quality=quality)

        # write prompt you want
        prompt = input("\nPlease write a clear and detailed description of the image you want to generate: ")
        print(f"You have requested to generate: '{prompt}'")

        print(f"\nFor this generation, the model being used is:\n{openai_client.model}")

        print("\nwaiting for response...")
        list_url_image = openai_client.get_response(prompt)
        print("Success ! Here is the url of your generated image:")
        for url_image in list_url_image:
            print(url_image)

            print("waiting to display the image...")
            excel = ExcelOperation()
            image = ImageGeneration(url_image)
            image.display_image()
            image.save_image(f"image_{excel.sheet.max_row}")
            print("saving history...")
            excel.add_new_image(prompt)
            excel.save_file()

        message_to_continue = input("Would you like to try again? (yes or no): ")
        if message_to_continue == "no" or message_to_continue == "n":
            running_bool = False
            print("\nThank you for testing this project! :)")
