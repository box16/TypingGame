import random


class Question:
    def __init__(self) -> None:
        self.material()

    def put_question(self) -> str:
        pick_num = random.randint(5, 10)
        pick = random.choices(self.materials, k=pick_num)
        return "".join(pick)

    def material(self) -> None:
        with open('question_material.txt', encoding='utf-8') as file:
            read_data = file.read()
        self.materials = read_data.replace("\n", "")
