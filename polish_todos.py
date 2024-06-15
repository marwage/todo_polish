import cohere


def get_api_key():
    with open("./api_key.txt", "r", encoding="utf-8") as fil:
        api_key = fil.read().strip()
    return api_key


def main():
    api_key = get_api_key()
    coh = cohere.Client(api_key)
    response = coh.chat(message="Is this API call working?")
    print(response)


if __name__ == "__main__":
    main()
