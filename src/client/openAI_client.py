from openai import OpenAI, APIError, APITimeoutError, RateLimitError
from src.model.model_image import ModelImage


class OpenAIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.client = None
        self.model = ModelImage()

    def initialize_client(self):
        try:
            self.client = OpenAI(api_key=self.api_key)
            print("testing API key...")
            # Test the API key by making a simple request
            self.client.models.list()
        except APIError as api_error:
            raise SystemExit(f"{api_error.message[:-1]}: API key not valid.")

    """ get response from OpenAI model based on a prompt """

    def get_response(self, prompt):
        try:
            response = self.client.images.generate(
                model=self.model.model_name,
                prompt=prompt,
                size=self.model.size,
                quality=self.model.quality,
                n=self.model.n,
            )
            image_url = [image.url for image in response.data]
            return image_url
        except APITimeoutError as timeout:
            raise SystemExit(
                f"Request timed out: {timeout.message} (Code: {timeout.code}). "
                "This may be due to network issues or high server load.")
        except RateLimitError as rate_limit:
            raise SystemExit(
                f"Rate limit exceeded: {rate_limit.message} (Code: {rate_limit.code}). "
                "You exceeded your current quota, please check your plan and billing details "
                "(https://platform.openai.com/settings/organization/billing/overview).")
