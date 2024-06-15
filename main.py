def conv(giris):
    try:
        sonuc = eval(giris)
        return str(sonuc)
    except Exception as e:
        return "Error"

def sonuc(giris):
    return(conv(giris))

while True:
    giris = str(input("input: "))
    print(sonuc(giris))