
# 1.Przypomnienie
#   0. Napisz program ukrywający hasło

def hide():
    inp=input('Co zaszyfrować? ')
    x = len(inp)
    beg = inp[0]
    end = inp[x-1]
    if x < 3:
        print('***')
    elif x==3:
        print(beg+'**')
    else:
        print(beg+('*'*(x-2))+end)
hide()

#   1. Napisz funkcję zmieniającą klucz _name_ na _nazwa_
def print_dict(d):
    d['nazwa'] = d['name']
    d.pop('name')
    for key in samolot:
        print("{0}:{1}".format(key,d[key]))
if __name__ == "__main__":
    samolot = {'name':'boeing',
                'przebieg':10000,
                'type':'pasazerski'}

    print_dict(samolot)

#   2. Uzupełnij funkcję liczącą VAT

def calculate_vat(netto):
    vat=netto*0.23
    
    return(vat)

if __name__ == "__main__":
    vat = calculate_vat(1000)
    print("{0}".format(vat))