def conv(expression):
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return "Error"
while True:
    expression = str(input("input: "))
    sonuc = conv(expression)
    print(sonuc)