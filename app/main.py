from fastapi import FastAPI, HTTPException
import uvicorn
from helpers import generate_branding_snippet, generate_keywords
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from blog_gen import (
    generate_blog_topic_ideas,
    generate_blog_section_titles,
    generate_blog_section_details,
)


app = FastAPI()


MAX_INPUT_LENGTH = 32

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/generate_snippet/{prompt}/")
async def generate_snippet(prompt: str):
    validate_input_length(prompt)
    snippet = generate_branding_snippet(prompt)
    return {"snippet": snippet, "keywords": []}


@app.get("/generate_keywords/{prompt}/")
async def generate_branding_keywords(prompt: str):
    validate_input_length(prompt)
    keywords = generate_keywords(prompt)
    return {"snippet": None, "keywords": keywords}


@app.get("/generate_blog/{topic}/{audience}/{keywords}/")
async def generate_blog_topic(topic: str, audience: str, keywords: str):
    # validate_input_length(prompt)
    snippet = generate_blog_topic_ideas(
        topic=topic, audience=audience, keywords=keywords
    )
    # keywords = generate_keywords(prompt)
    return {"snippet": snippet}


@app.get("/generate_blog_titles/{topic}/{audience}/{keywords}/")
async def generate_blog_titles(topic: str, audience: str, keywords: str):
    # validate_input_length(prompt)
    snippet = generate_blog_section_titles(
        topic=topic, audience=audience, keywords=keywords
    )
    # keywords = generate_keywords(prompt)
    return {"snippet": snippet}


@app.get("/generate_blog_section/{topic}/{section}/{audience}/{keywords}/")
async def generate_blog_section(topic: str, section: str, audience: str, keywords: str):
    # validate_input_length(prompt)
    snippet = generate_blog_section_details(
        blogTopic=topic, sectionTopic=section, audience=audience, keywords=keywords
    )
    # keywords = generate_keywords(prompt)
    return {"snippet": snippet}


@app.get("/generate_snippet_and_keywords/{prompt}/")
async def generate_snippet_and_keywords(prompt: str):
    validate_input_length(prompt)
    snippet = generate_branding_snippet(prompt)
    keywords = generate_keywords(prompt)
    return {"snippet": snippet, "keywords": keywords}


def validate_input_length(prompt: str):
    if len(prompt) >= MAX_INPUT_LENGTH:
        raise HTTPException(
            status_code=400,
            detail=f"Input length is too long. Must be under {MAX_INPUT_LENGTH} characters.",
        )


handler = Mangum(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
