class Glass:
    capacity = 250

    def __init__(self):
        self.content: int = 0

    def fill(self, ml):
        free_space = self.capacity - self.content
        if ml <= free_space:
            self.content += ml
            return f"Glass filled with {ml} ml"
        return f"Cannot add {ml} ml"

    def empty(self):
        self.content = 0
        return f"Glass is now empty"

    def info(self):
        return f"{self.capacity - self.content} ml left"
