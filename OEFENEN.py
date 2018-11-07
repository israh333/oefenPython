fruit = {"banaan": "geel", "aardbei": "rood", "kiwi": "groen"}

def toevoegen():
    toevoegen = input("Wat wil je toevoegen als key?")
    toevoegen1 = input("Wat wil je als value?")
    fruit[toevoegen] = toevoegen1
    print(fruit)


def verwijder():
    delete = input("Welke key wil je deleten?")
    del fruit[delete]

def controleren():
    woord = input("Welk woord wil je checken?")
    if woord in fruit:
        print(fruit[woord])
    else:
        print("Neen aanschouw")
        print("""""")

def alles():
    print(fruit.values())
    print(fruit.keys())

def samenvoegen():
    dict = {'gegroet': 'hello', 'hai': 'wat'}
    dict2 = {'hey': 'yo' }
    dict.update(dict2)
    print ("updated dict : ", dict)


def teller():
    d = {}
    for i in range(10):
        d[i]=1*1
        print(d)

teller()
