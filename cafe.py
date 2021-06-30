def pick():

    print("""
    =================[메뉴]==================
    1.커피                             
       1. 아메리카노(3000)           
       2. 카라멜 마키아또(4000)      
       3. 그린티(5000)             
       4. 라떼(5500)
    =========================================

    """)

    print("""
    주문하시려면 주문하기 버튼(1)을, 종료하시려면(0)을 눌러주세요
    """)

def pick_ingredient(pick):

    dict = {
        "샷" : 500,
        "투샷" : 1000,
        "우유" : 1500,
        "두유" : 1500,
        "시럽" : 2000,
        "휘핑크림" : 2000,

    }

    print("{0} 추가".format(pick))
    if not pick in dict:
        return ""
    return dict[pick]


def ask_additional_pick():
    print("재료를 추가하시겠습니까? 추가:1 추가안함:0")
    add_or_not = int(input())
    total_add = 0
    if add_or_not == 1:
        add_ingredient = 1
        print("샷(500), 투샷(1000), 우유(1500), 두유(1500), 시럽(2000), 휘핑크림(2000)중 추가하고 싶은것을 고르세요, 추가후 0 을 누르세요")
        while(True):
            add_ingredient = input()
            if add_ingredient == "0": break

            b=pick_ingredient(add_ingredient)
            if b == "":
                return ""
            total_add +=b
            print(total_add)
        return total_add   
    elif add_or_not == 0:
        return total_add
    else:
        print("1과 0중에 고르세요 추가:1 추가안함:0")

class Menu:
    def __init__(self):
        self.total = 0
        
    def price(self, cost, addition_cost):
        self.total = cost + addition_cost
        return self.total 
    
    def total_cost(self):
        print("총가격:{0}".format(self.total))

    def pick_coffee(self, coffee):
        dict = {
            "아메리카노":3000,
            "카라멜 마끼아또":4000,
            "그린티":5000,
            "라떼":5500
        }
        
        addition_cost = ask_additional_pick()
        if addition_cost == "":
            return "키에러"
        return self.price(dict[coffee], addition_cost)

    def coffee(self):
        coffee = input("커피를 골라주세요, 주문완료후 0을 눌러주세요")
        if coffee == "아메리카노":
            if self.pick_coffee(coffee)== "키에러": return "키에러"
        elif coffee == "카라멜 마끼아또":
            if self.pick_coffee(coffee)== "키에러": return "키에러"
        elif coffee == "그린티":
            if self.pick_coffee(coffee)== "키에러": return "키에러"
        elif coffee == "라떼":
            if self.pick_coffee(coffee)== "키에러": return "키에러"
        else:
            print("메뉴에 없습니다. 다른걸 선택해주세요")
        return self.total_cost() 

if __name__ == '__main__':
    drink = Menu()
    def exist_in_add():
        while(drink.coffee() == "키에러"):
            print("추가메뉴에 없습니다. 다른걸 골라주세요")
            
    while(True):
        pick()
        number = int(input())
        if number == 1:
            exist_in_add()
        elif number == 0:
            break
        else:
            print("1,0중에 선택하세요")
        print("주문을 끝내겠습니까? 끝내시려면 1 아니면 아무키나 누르세요")
        order = (input())
        try:
            if order == "1":
                break
        except KeyError:
            pass




