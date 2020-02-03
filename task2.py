class CoffeeMachine:
    def __init__(self):
        self.milk = 1000
        self.coffee = 1000
        self.sugar = 1000


    def __subtrack_milk(self, milk):
        self.milk -= milk


    def __subtrack_coffee(self, coffee):
        self.coffee -= coffee

    def __subtrack_sugar(self, sugar):
        self.sugar -= sugar

    def make_coffee(self, gr, ml,gramm):
        if self.milk >= milk and self.coffee >= coffee and self.sugar >= sugar:
            self.__subtrack_milk(gr)
            self.__subtrack_coffee(ml)
            self.__subtrack_sugar(gramm)
            print("Процесс приготовления кофе завершен!")

        else:
            if self.milk < milk:
                print(f"Пополните запасы молока на {-self.milk + milk} мл!")
            if self.coffee < coffee:
                print(f"Пополните запасы кофе на {-self.coffee + coffee} мл!")
            if self.sugar < sugar:
                print(f"Пополните запасы сазара на {-self.sugar + sugar} гр!")



if __name__ == '__main__':
    milk = int(input("Введите количество молока : "))
    coffee = int(input("Введите количество кофе : "))
    sugar = int(input("Введите количество сахара: "))
    cofe = CoffeeMachine()
    cofe.make_coffee(milk,coffee,sugar)
