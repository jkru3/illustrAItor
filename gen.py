import io
import os
import warnings

from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

# API setup
os.environ['STABILITY_HOST'] = 'grpc.stability.ai:443'
# To get your API key, visit https://beta.dreamstudio.ai/membership

os.environ['STABILITY_KEY'] = 'sk-ApVWI7G5GMiVWkkjOHlcXuDBsmvwYKWjJEou3ell68H0WOaU'

stability_api = client.StabilityInference(
    key=os.environ['STABILITY_KEY'],
    verbose=True,
)


# Makes AI generated picture and displays it to screen
def make_image(title, p, style):
    # the object returned is a python generator
    answers = stability_api.generate(
        prompt=title + ": " + p + ", in the style of " + style,
        steps=50,  # defaults to 50 if not specified
    )
    # iterating over the generator produces the api response
    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                warnings.warn(
                    "Your request activated the API's safety filters and could not be processed."
                    "Please modify the prompt and try again.")
            if artifact.type == generation.ARTIFACT_IMAGE:
                # img = Image.open(io.BytesIO(artifact.binary))
                # img.show()
                img = Image.open(io.BytesIO(artifact.binary))
                return img  # I think this returns a Jpeg


def display_image(img):
    img.show()


def get_inputs():
    title = input("Book Title: ")
    p = input("Enter prompt for generation: ")
    style = input("In the style of: ")
    return title, p, style


def main():
    title, p, style = get_inputs()
    img = make_image(title, p, style)
    display_image(img)
