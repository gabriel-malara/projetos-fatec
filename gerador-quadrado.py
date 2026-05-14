altura = int(input("Altura desejada do quadrado: "))
largura = int(input("Largura desejada do quadrado: "))

for i in range(altura+2):
    base = ""
    if i == 0 or i == altura+1:
        for _ in range(largura):
            base = base + "-"
        print(f'+' + base + '+')
    else:
        for _ in range(largura):
            base = base + " "
        print(f'|' + base +'|')