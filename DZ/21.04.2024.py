class Color:
    def __init__(self):
        self.name = "Green"
        self.lg = self.LightGreen()

    def show(self):
        print("Name:", self.name)

    class LightGreen:
        def __init__(self):
            self.name = "Light Green"

        def display(self):
            print("Name:", self.name)


outer = Color()
outer.show()
g = outer.lg
g.display()
