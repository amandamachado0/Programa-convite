idade = int(input("Digite sua idade: "))
convite = input("Você tem convite? (sim/nao): ").strip().lower()

if idade >= 18:
    if convite == 's':
        print("Entrada permitida! Aproveite o evento")
    else:
        print("Desculpe, você precisa de um convite para entrar")
else:
    print("Entrada negada! O evento é apenas para maiores de idade")