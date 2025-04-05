import os
import json
from utility.OpenAIClient import openai_client
from git import Repo
import requests
import shlex


def getGitRequests(query, owner = "Krutash", repo_name = "ml-machine-learning.test"):
    response = requests.get(f"https://api.github.com/repos/{owner}/{repo_name}/commits")
    data = json.loads(response.text)

    prompt = f"""
    {query}, for this provided json form gitHUB API response just
    give the answer, no code required:
    
    {data}    
    """

    responses = openai_client.chat.completions.create(
        messages=[
            {
                "role":"user",
                "content": prompt
            }
        ],
        model = "gpt-4o"
    )

    print(responses.choices[0].message.content)
    return response.choices[0].message.content


