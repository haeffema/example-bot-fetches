import requests

from fetch.config import BACKEND, EXAMPLE
from data_types.example_type import Example


def create_example(example: Example):
    requests.post(url=BACKEND + EXAMPLE, json=example.json())


def get_example(id: int):
    return requests.get(url=BACKEND + EXAMPLE + "/" + str(id)).json()


def get_all_examples():
    return requests.get(url=BACKEND + EXAMPLE).json()
