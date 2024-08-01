# For this project, I noticed a significant difference in quality between DALL·E 2 and DALL·E 3.
# That's why, only DALL·E 3 is used to maintain a high level of quality.
class ModelImage:
    def __init__(self, model_name="dall-e-3", size="1024x1024", quality="standard", n=1):
        self.model_name = model_name
        self.size = size
        self.quality = quality
        self.n = n

    # Since DALL·E 3 can only generate one image per request, the 'n' parameter is not updatable.
    def update_model(self, size=None, quality=None):
        if size is not None:
            self.size = size
        if quality is not None:
            self.quality = quality

    def __str__(self):
        return (f"{self.model_name}:\n"
                f"  size: {self.size}\n"
                f"  quality: {self.quality}\n"
                f"  number of images: {self.n}")