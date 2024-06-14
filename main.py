def conv(giris):
    try:
        sonuc = eval(giris)
        return str(sonuc)
    except Exception as e:
        return "Error"
while True:
    giris = str(input("input: "))
    sonuc = conv(giris)
    print(sonuc)