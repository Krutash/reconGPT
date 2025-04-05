from openai import AzureOpenAI
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

os.environ["NO_PROXY"] = "openai.azure.com"

AZURE_OPENAI_ENDPOINT = "https://gbto-hackathon-1.openai.azure.com"

openai_client = AzureOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-08-01-preview"
)