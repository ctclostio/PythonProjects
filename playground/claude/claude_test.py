import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="sk-ant-api03-daYPpClDtjV0BzFQZ8EVNL3MkgK1Ztxo0hMaK6iNuB5EaLkUHsoTCaPsepc_YOC-GggXFKpPp2PHKlqgXzF0Pw-NNRgdg",
)

message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    temperature=0.0,
    system="Respond only in Yoda-speak.",
    messages=[
        {"role": "user", "content": "How are you today?"}
    ]
)

print(message.content)
