def pick():

    print("""
    =================[메뉴]==================
    1.커피                     2.티          
        아메리카노(3000)           녹차(2000)   
        카라멜 마키아또(4000)      둥글레차(2500)
        그린티(5000)               레몬차(3500)
        라떼(5500)
    =========================================

    """)

    print("""
    1.커피 2.티 0.종료 - 선택하세요
    """)

class Menu:
    def __init__(self):
        self.total = 0
        
    def price(self, cost):
        self.total+= cost
        print("가격은 {0} 입니다".format(self.total))    
    
    def total_cost(self):
        print("총가격:{0}".format(self.total))

    def coffee(self):
        coffee = input("커피를 골라주세요, 주문완료후 0을 눌러주세요")
        if coffee == "아메리카노":
            self.cost = 3000
            self.price(self.cost)
        elif coffee == "카라멜 마키아또":
            self.cost = 4000
            self.price(self.cost)
        elif coffee == "그린티":
            self.cost = 5000
            self.price(self.cost)
        elif coffee == "라떼":
            self.cost = 5500
            self.price(self.cost)
        else:
            print("메뉴에 없습니다. 다른걸 선택해주세요")

    def tea(self):
        tea = input("티를 골라주세요")
        if tea == "녹차":
            self.cost = 2000
            self.price(self.cost)
        elif tea == "둥글레차":
            self.cost = 2500
            self.price(self.cost)
        elif tea == "레몬차":
            self.cost = 3500
            self.price(self.cost)
        else:
            print("메뉴에 없습니다. 다른걸 선택해주세요")

if __name__ == '__main__':
    drink = Menu()

    while(True):
        pick()
        number = int(input())
        if number == 1:
            drink.coffee()
        elif number == 2:
            drink.tea()
        elif number == 0:
            drink.total_cost()
            break
        else:
            print("1,2,0중에 선택하세요")



