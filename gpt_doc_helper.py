import os
from http.client import responses
from pyexpat.errors import messages

from click import prompt
from utility.OpenAIClient import openai_client


os.environ["NO+PROXY"] = "openai.azure.com"

def summarize_document(query, file_path):
    with open(file_path, "r") as f:
        content = f.read()

    prompt = f"""
    {query} from the following document:\n\n {content}
    """

    char_completion = openai_client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4o"
    )

    return char_completion.choices[0].message.content

def analyze_document(file_path):
    with open(file_path, "r") as f:
        content = f.read()

    prompt = f"""
    Analyse the following document and identify key insights:\n\n {content}
    """
    response = openai_client.completions.create(
        engine = "davinci-003",
        prompt=prompt,
        max_tokens = 300
    )

    return response.choices[0].text.strip()