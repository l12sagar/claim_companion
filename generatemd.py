from langchain_openai import ChatOpenAI
import httpx
import os

# TCS API client
client = httpx.Client(verify=False)

llm = ChatOpenAI(
    base_url="https://genailab.tcs.in",
    model="genailab-maas-Opus-4.6",
    api_key="sk-VHold_zIX3VuaK-xkAc8rw",
    http_client=client,
)

# Read instructions.txt
with open("instructions.txt", "r", encoding="utf-8") as f:
    instructions = f.read()

# Basic size information
line_count = len(instructions.splitlines())
char_count = len(instructions)

print(f"Read {line_count} lines ({char_count:,} characters)")

prompt = f"""
You are given an instructions.txt file.

Your task is to create the Markdown document requested by the instructions.

IMPORTANT:
- Read ALL of the instructions before generating the document.
- The input contains {line_count} lines.
- Do not skip, summarize, or ignore any part of the instructions.
- Follow the instructions exactly.
- Preserve important technical details, commands, filenames, requirements,
  constraints, and examples.
- Return ONLY the final Markdown content.
- Do not wrap the entire response in ```markdown fences.
- Make the output a complete, well-structured Markdown document.

Here is the complete instructions.txt:

---------------- BEGIN instructions.txt ----------------

{instructions}

----------------- END instructions.txt -----------------
"""

response = llm.invoke(prompt)

markdown_content = response.content

# Save generated Markdown
with open("output.md", "w", encoding="utf-8") as f:
    f.write(markdown_content)

print(f"Created output.md ({len(markdown_content):,} characters)")
