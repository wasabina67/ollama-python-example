import ollama


def main():
    content = "なぜ空は青いのですか？"
    resp = ollama.chat(
        model="llama3.1", messages=[{"role": "user", "content": content}]
    )
    print(resp["message"]["content"])


if __name__ == "__main__":
    main()
