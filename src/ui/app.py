import sys
import os

import tkinter as tk
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from src.client.openAI_client import OpenAIClient
from src.utils.Excel import ExcelOperation
from src.utils.Image import ImageGeneration


class SplashScreen(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Generating Image with AI project")
        self.geometry("1024x1024")
        self.configure(bg='white')

        # Configure the grid to center the widgets
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Title Label
        self.title_label = ctk.CTkLabel(self, text="Welcome to Generating Image with AI project :)",
                                        font=("Helvetica", 20, "bold"))
        self.title_label.grid(row=0, column=0, pady=20)

        # Instructions Label
        self.instructions_label = ctk.CTkLabel(self, text="To use this project, you need an API key from OpenAI.\n"
                                                          "If you don't have one, you can obtain it at https://platform.openai.com/api-keys",
                                               font=("Helvetica", 16))
        self.instructions_label.grid(row=1, column=0, pady=20)

        # Author Label
        self.author_label = ctk.CTkLabel(self, text="Author: Alexis EGEA", font=("Helvetica", 16))
        self.author_label.grid(row=2, column=0, pady=10)

        # Continue Button
        self.continue_button = ctk.CTkButton(self, text="Continue", command=self.show_main_app)
        self.continue_button.grid(row=3, column=0, pady=20)

    def show_main_app(self):
        self.destroy()  # Close splash screen
        app = ImageGeneratorApp(ctk.CTk())
        app.root.mainloop()


class ImageGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Image Generator")
        self.root.geometry("300x200")

        # Configuration de base de customtkinter
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # API Key Input
        self.api_key_label = ctk.CTkLabel(root, text="Enter your API Key:")
        self.api_key_label.grid(column=0, row=0)
        self.api_key_entry = ctk.CTkEntry(root, show="*")
        self.api_key_entry.grid(column=1, row=0)

        # Image Size Selection
        self.size_label = ctk.CTkLabel(root, text="Select Image Size:")
        self.size_label.grid(column=0, row=1)
        self.size_var = tk.StringVar()
        self.size_combobox = ctk.CTkComboBox(root, variable=self.size_var,
                                             values=['1024x1024', '1024x1792', '1792x1024'])
        self.size_combobox.grid(column=1, row=1)
        self.size_combobox.set('1024x1024')

        # Image Quality Selection
        self.quality_label = ctk.CTkLabel(root, text="Select Image Quality:")
        self.quality_label.grid(column=0, row=2)
        self.quality_var = tk.StringVar()
        self.quality_combobox = ctk.CTkComboBox(root, variable=self.quality_var, values=['standard', 'hd'])
        self.quality_combobox.grid(column=1, row=2)
        self.quality_combobox.set('standard')

        # Prompt Input
        self.prompt_label = ctk.CTkLabel(root, text="Prompt:")
        self.prompt_label.grid(column=0, row=3)
        self.prompt_entry = ctk.CTkEntry(root)
        self.prompt_entry.grid(column=1, row=3)

        # Generate Button
        self.generate_button = ctk.CTkButton(root, text="Generate Image", command=self.generate_image)
        self.generate_button.grid(column=1, row=4)

    def generate_image(self):
        # Get and clean the API Key
        api_key_value = self.api_key_entry.get().strip()
        if not api_key_value:
            CTkMessagebox(title="Error", message="API Key is required.", icon="cancel", option_1="OK")
            return

        # Initialize OpenAI client
        openai_client = OpenAIClient(api_key=api_key_value)
        openai_client.initialize_client()

        size_image = self.size_var.get()
        quality = self.quality_var.get()
        prompt = self.prompt_entry.get()

        if not prompt:
            CTkMessagebox(title="Error", message="Please enter a prompt for the image generation.", icon="cancel",
                          option_1="OK")
            return

        # Update the model with the selected size and quality
        openai_client.model.update_model(size=size_image, quality=quality)

        # Generate the image
        try:
            list_url_image = openai_client.get_response(prompt)
            if list_url_image:
                url_image = list_url_image[0]
                CTkMessagebox(title="Success", message=f"Image generated successfully! URL: {url_image}", icon="info",
                              option_1="OK")

                # Display and save the image
                image = ImageGeneration(url_image)
                image.display_image()
                excel = ExcelOperation()
                image.save_image(f"image_{excel.sheet.max_row}")
                excel.add_new_image(prompt)
                excel.save_file()
            else:
                CTkMessagebox(title="Error", message="Failed to generate the image.", icon="cancel", option_1="OK")
        except Exception as e:
            CTkMessagebox(title="Error", message=str(e), icon="cancel", option_1="OK")


if __name__ == '__main__':
    splash = SplashScreen()
    splash.mainloop()
