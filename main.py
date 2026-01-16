class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.exp = 0

    def gain_exp(self, amount):
        self.exp += amount
        self.check_level()

    def check_level(self):
        while self.exp >= 100:
            self.exp -= 100
            self.level += 1
            print(f"{self.name} LEVEL UP! 🎉")

    def status(self):
        return f"{self.name} | Level: {self.level} | EXP: {self.exp}"


player = Player("Jahongir")
player.gain_exp(50)
player.gain_exp(80)
player.gain_exp(120)

print(player.status())
