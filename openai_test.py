import openai

openai.api_key = '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'

response = openai.Completion.create(
  engine="davinci",
  prompt="This is a test prompt",
  max_tokens=50
)

print(response.choices[0].text)