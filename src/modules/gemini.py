"""Gemini API."""

import google.generativeai as genai
import yaml

FLASH_MODEL = "gemini-1.5-flash"


def configure() -> None:
    """Configure the API key and model name."""
    with open(r".\credentials.yaml", mode="rt", encoding="utf-8") as file:
        credentials = yaml.safe_load(file)
    key = credentials["key"]
    genai.configure(api_key=key)


def list_models():
    """List available models."""
    for m in genai.list_models():
        if "generateContent" in m.supported_generation_methods:
            print(m.name)


def generate_content(
    prompt: str,
    model_name: str = FLASH_MODEL,
) -> None:
    """Generate content using the specified model."""
    model = genai.GenerativeModel(model_name)
    content = model.generate_content(prompt)
    print(content.text)


if __name__ == "__main__":
    configure()
    # generate_content(prompt="What is the meaning of life?")
