import json
import re

import cohere


def get_api_key():
    with open("./api_key.txt", "r", encoding="utf-8") as fil:
        api_key = fil.read().strip()
    return api_key


def get_todos():
    # TODO: query DB
    todos = [
        "Buy tomatoes at M&S",
        "Be in a real relationship by 35",
        "Complete the intial project proposal",
        "Finish Cohere internship application",
    ]
    return todos


def update_todos(todos: list):
    # TODO: update DB
    pass


def extract_json(text: str):
    patt = r"```json((.|\n)*)```"
    mat = re.search(patt, text)
    if mat is None:
        raise ValueError("Match is None")
    json_str = mat.group(1)
    json_obj = json.loads(json_str)
    return json_obj


def main():
    api_key = get_api_key()
    coh = cohere.Client(api_key)

    todos = get_todos()
    instruction = (
        "Evaluate the todos based on the SMART criteria"
        " and if the criteria is not fullfilled"
        " propose a rephrase of the todo or a split into sub-todos."
        " Return the new todos in a JSON list."
    )
    todo_list = "\n- ".join(todos)
    message = f"{instruction}\n- {todo_list}"
    print(message)
    response = coh.chat(message=message)
    polished_todos = extract_json(response.text)
    print(polished_todos)
    update_todos(polished_todos)


if __name__ == "__main__":
    main()
