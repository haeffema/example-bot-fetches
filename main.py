from data_types.example_type import Example
from fetch.fetch import create_example, get_example, get_all_examples

example = Example("name", 12.5)
create_example(example)
print(get_example(0))
print(get_all_examples())
