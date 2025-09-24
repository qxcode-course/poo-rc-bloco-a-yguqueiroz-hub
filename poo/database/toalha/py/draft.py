class Towel:
    def __init__(self):
        self.color: str = "" 
        self.size: str = ""
        self.wetness: int = 0

print ("Qual a cor da sua toalha?")
color = input()
tower: Towel = Towel(color, "P")
print(f"Sua toalha é {towel.color}")

