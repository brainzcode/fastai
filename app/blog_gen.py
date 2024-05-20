import argparse
from typing import List
import re
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

MAX_INPUT_LENGTH = 32
model = "gpt-3.5-turbo"


def validate_length(prompt: str) -> bool:
    return len(prompt) <= MAX_INPUT_LENGTH


# def generate_keywords(prompt: str) -> List[str]:
#     content = f"Generate SEO, related branding keywords for {prompt}"
#     print(content)
#     completion = client.chat.completions.create(
#         model=model,
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": content},
#         ],
#         max_tokens=32,
#     )

#     # Extract output text.
#     keywords_text: str = completion.choices[0].message.content

#     # Strip whitespace.
#     keywords_text = keywords_text.strip()
#     keywords_array = re.split(",|\n|;|-", keywords_text)
#     keywords_array = [k.lower().lstrip() for k in keywords_array]
#     keywords_array = [k for k in keywords_array if len(k) > 0]

#     print(f"Keywords: {keywords_array}")
#     return keywords_array


def generate_blog_topic_ideas(topic, audience, keywords):
    content = f"Generate 6 Blog Topic Ideas on the following Topic: {topic} Audience: {audience} Keywords: {keywords}"
    print(content)
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": content},
        ],
        max_tokens=256,
    )

    # Extract output text.
    blog_list: str = completion.choices[0].message.content

    # Strip whitespace.
    blog_list = blog_list.strip()
    blog_topics = re.split(",|\n|;|-", blog_list)
    blog_topics = [k.lower().lstrip() for k in blog_topics]
    blog_topics = [k for k in blog_topics if len(k) > 0]

    print(f"Blog_Topic_Ideas: {blog_topics}")
    return blog_topics


def generate_blog_section_titles(topic, audience, keywords):
    content = f"Generate adequate blog section titles for the provided blog topic, audience, and keywords: {topic}\nAudience: {audience}\nKeywords: {keywords}\n"
    print(content)
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": content},
        ],
        max_tokens=256,
    )

    # Extract output text.
    blog_list: str = completion.choices[0].message.content

    # Strip whitespace.
    blog_list = blog_list.strip()
    blog_topics = re.split(",|\n|;|-", blog_list)
    blog_topics = [k.lower().lstrip() for k in blog_topics]
    blog_topics = [k for k in blog_topics if len(k) > 0]

    print(f"Blog_Section_Titles: {blog_topics}")
    return blog_topics


def generate_blog_section_details(blogTopic, sectionTopic, audience, keywords):
    content = f"Generate detailed blog section write up for the following blog section heading, using the blog title, audience, blog section heading and keywords provided.\nBlog Title: {blogTopic}\nBlog Section Heading: {sectionTopic}\nAudience: {audience}\nKeywords:  {keywords}\n\n"
    print(content)
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": content},
        ],
        max_tokens=500,
    )

    # Extract output text.
    blog_section_details: str = completion.choices[0].message.content

    # Strip whitespace.
    blog_section_details = blog_section_details.lstrip('"')

    # # Add ... to truncated statements.
    last_char = blog_section_details[-1]

    if last_char not in {".", "!", "?"}:
        blog_section_details += "..."

    print(f"Blog-Details: {blog_section_details}")
    return blog_section_details

    # if "choices" in response:
    #     if len(response["choices"]) > 0:
    #         res = response["choices"][0]["text"]
    #         if not res == "":
    #             cleanedRes = res.replace("\n", "<br>")
    #             if profile.monthlyCount:
    #                 oldCount = int(profile.monthlyCount)
    #             else:
    #                 oldCount = 0

    #             oldCount += len(cleanedRes.split(" "))
    #             profile.monthlyCount = str(oldCount)
    #             profile.save()
    #             return cleanedRes
    #         else:
    #             return ""
    #     else:
    #         return ""
    # else:
    #     return ""


# def checkCountAllowance(profile):
#     if profile.subscribed:
#         type = profile.subscriptionType
#         if type == "free":
#             max_limit = 5000
#             if profile.monthlyCount:
#                 if int(profile.monthlyCount) < max_limit:
#                     return True
#                 else:
#                     return False
#             else:
#                 True
#         elif type == "starter":
#             max_limit = 40000
#             if profile.monthlyCount:
#                 if int(profile.monthlyCount) < max_limit:
#                     return True
#                 else:
#                     return False
#             else:
#                 True
#         elif type == "advanced":
#             return True
#     else:
#         max_limit = 5000
#         if profile.monthlyCount:
#             if int(profile.monthlyCount) < max_limit:
#                 return True
#             else:
#                 return False
#         else:
#             True
