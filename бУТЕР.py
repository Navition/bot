def bread(funk):
    def in_bread():
        funk()
        print("<<<______>>>")
    return in_bread
@bread
def sandwich(food="--ветчина--"):
    print(food)
sandwich()
#sandwich=bread(sandwich)
#sandwich()
#"Здоровье и болезни":"",
#"Уход и содержание":"",
#"Характер":""