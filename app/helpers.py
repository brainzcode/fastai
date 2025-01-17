import argparse
from typing import List
import re
from openai import OpenAI
from dotenv import load_dotenv
import os
# from blogs_gen import generateBlogTopicIdeas

load_dotenv()

api_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

MAX_INPUT_LENGTH = 32
model = "gpt-3.5-turbo"


def main_func():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input

    if validate_length(user_input):
        generate_branding_snippet(user_input)
        generate_keywords(user_input)
    else:
        raise ValueError(
            f"Input length is too long. Must be under {MAX_INPUT_LENGTH}. Submitted input is {user_input}"
        )


def validate_length(prompt: str) -> bool:
    return len(prompt) <= MAX_INPUT_LENGTH


def generate_keywords(prompt: str) -> List[str]:
    content = f"Generate SEO, related branding keywords for {prompt}"
    print(content)
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": content},
        ],
        max_tokens=32,
    )

    # Extract output text.
    keywords_text: str = completion.choices[0].message.content

    # Strip whitespace.
    keywords_text = keywords_text.strip()
    keywords_array = re.split(",|\n|;|-", keywords_text)
    keywords_array = [k.lower().lstrip() for k in keywords_array]
    keywords_array = [k for k in keywords_array if len(k) > 0]

    print(f"Keywords: {keywords_array}")
    return keywords_array


def generate_branding_snippet(prompt: str) -> str:
    content = f"Generate upbeat branding snippet for {prompt}"
    print(content)
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": content},
        ],
        max_tokens=32,
    )

    # Extract output text.
    branding_text: str = completion.choices[0].message.content

    # Strip whitespace.
    branding_text = branding_text.lstrip('"')

    # # Add ... to truncated statements.
    last_char = branding_text[-1]

    if last_char not in {".", "!", "?"}:
        branding_text += "..."

    print(f"Snippet: {branding_text}")
    return branding_text
