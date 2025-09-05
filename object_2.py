class Taiyaki:
    def __init__(self , nakami , kakaku ):
        self.flavor = nakami
        self.price = kakaku
        self.eaten = False
    def display_info(self):
        print(f"このたい焼きは{self.flavor}味で、値段は{self.price}円です")

    def bigsize(self):
        print(f"大サイズは{self.price + 100}円です")

    def eat(self):
        if not self.eaten:
            print(f"{self.flavor}味のたい焼きを美味しくいただきました")
            self.eaten = True
        else:
            print(f"{self.flavor}味のたい焼きはもうありません")

    def premium(self):
        if self.flavor == "クリーム" or self.flavor == "栗" :
            print("このたい焼きはプレミアムです")
        else :
            print("このたい焼きはプレミアムではありません")


taiyaki_1 = Taiyaki("あんこ" , 300)
taiyaki_2 = Taiyaki("クリーム" , 400)

taiyaki_1.display_info()
taiyaki_1.bigsize()
taiyaki_2.premium()
taiyaki_1.eat()
taiyaki_1.eat()

class Shirotaiyaki(Taiyaki):
    def __init__(self , nakami , kakaku):
        super().__init__(nakami , kakaku)

        self.texture = "もちもち"
        self.limit = "30分"

    def bite(self):
        print(f"{self.texture}の食感")

    def display_info(self):
        print(f"{self.flavor}味で食感は{self.texture}です")


taiyaki_3 = Shirotaiyaki("クリーム" , 450)

taiyaki_3.display_info()
taiyaki_3.bite()