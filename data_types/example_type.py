from data_types.default_type import Default


class Example(Default):

    def __init__(self, name: str, money: float):
        super().__init__()
        self.name = name
        self.money = money

    def json(self) -> dict:
        return {"name": self.name, "money": self.money}