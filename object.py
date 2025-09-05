class Taiyaki:
    def __init__(self , nakami , kizi , size):
        self.flavor = nakami
        self.kizi = kizi
        self.size = size
        #print (f"{self.flavor}味のたい焼きが焼き上がりました！")
        #print (f"皮は{self.kizi}です。")

taiyaki_1 = Taiyaki("あんこ" , "クリスピー" , "普通")
taiyaki_2 = Taiyaki("クリーム" , "もちもち" , "大")

print(f"1つ目のたい焼きは、{taiyaki_1.flavor}味です。皮は{taiyaki_1.kizi}です")
print(f"2つ目のたい焼きは、{taiyaki_2.flavor}味です。皮は{taiyaki_2.kizi}です。サイズは{taiyaki_2.size}です")