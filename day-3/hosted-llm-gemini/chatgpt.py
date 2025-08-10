from openai import OpenAI

# Correct: client must be an OpenAI instance, NOT a string
client = OpenAI(api_key="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

MODEL_NAME = "gpt-4o"

PROMPT = """
Generate an ideal Dockerfile for {language} with best practices. Just share the Dockerfile without any explanation, and place it between two lines (e.g., ---) to make copying easier.
Include:
- Base image
- Installing dependencies
- Setting working directory
- Adding source code
- Running the application
"""

def generate_dockerfile(language):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "user", "content": PROMPT.format(language=language)}
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content

if __name__ == '__main__':
    language = input("Enter the programming language: ")
    dockerfile = generate_dockerfile(language)
    print("\nGenerated Dockerfile:\n")
    print(dockerfile)
