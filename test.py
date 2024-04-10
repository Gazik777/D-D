import random

class Heroy:
    def parametr_heroy(self,name, health, power, zashita):
        self.name = name
        self.health = health
        self.power = power
        self.zashita = zashita

class Ataka(Heroy):

    def random_vrag(self):
        vrag = ["Leshy", "Vampir", "Zomby", "Sprut", "Sclet", "Leshy1", "Vampir1", "Zomby1", "Sprut1", "Sclet1"]
        result = random.randint(1, 10)
        result = vrag[result]
        print(result)




ataka = Ataka()
ataka.random_vrag()