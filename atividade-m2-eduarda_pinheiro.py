import cmath

name = input('Qual o seu nome? ')

option = int(input(f'Olá {name}.\nDigite a opção desejada: \n1) Verificar triângulo \n2) Calcular equação do segundo grau \n3) Conferir data  \n4) Verificar tamanho  do texto \n5) Analisar CPF \n6) Contar caracteres \n7) Sair \n: '))

if option == 1:
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    c = int(input("Digite o terceiro valor: "))

    side1 = b-c
    side2 = a-c
    side3 = a-b

    if abs(side1) < a < b + c or abs(side2) < b < a + c or abs(side3) < c < a + b:
        if a == b == c:
            print("Triângulo equilátero")
        elif (a == b) or (b == c) or (c == a):
            print("Triângulo isósceles")
        elif (a != b) and (b != c) and (c != a):
            print("Triângulo escaleno")
    else:
        print("Os valores fornecidos não geram um triângulo")

elif option == 2:
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    c = int(input("Digite o terceiro valor: "))

    delta = (b * b - (4 * a * c))

    if a == 0:
        print("Estes valores não correspondem a uma equação de segundo grau")
    elif delta < 0:
        print("Esta equação não possui raízes reais")
    elif delta == 0:
        root = (-b/(2*a))
        print(f"Esta equação possui uma única raiz: {root}")
    elif delta > 0:
        positiveRoot = (-b+cmath.sqrt(delta))/(2*a)
        negativeRoot = (-b-cmath.sqrt(delta))/(2*a)
        print(f"As raízes da equação são: {positiveRoot} e {negativeRoot}")

elif option == 3:
    day = int(input("Digite um dia: "))
    month = int(input("Digite o mês: "))
    year = int(input("Digite o ano: "))

    if ((month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and day <= 31) or ((month == 4 or month == 6 or month == 9 or month == 11) and day <= 30) or (month == 2 and day <= 28):
        print("Data correta")
    else:
        print("Data incorreta")

elif option == 4:
    text = input("Digite o texto desejado: ")
    if len(text) < 5:
        print("Texto muito pequeno")
    elif len(text) >= 5 and len(text) < 15:
        print("Texto de tamanho médio")
    elif len(text) >= 15 and len(text) < 20:
        print("Texto grande")
    else:
        print("Texto inválido")

elif option == 5:
    cpf = input("Digite seu cpf contendo apenas os números: ")

    # teste = cpf.isdigit()
    # print(teste)

    if cpf.isdigit() and (len(cpf) == 11):
        print("CPF válido")
    else:
        print("CPF inválido")

elif option == 6:
    text = input("Digite o texto desejado: ")
    vowels = ["a", "e", "i", "o", "u", "A", "B", "C", "D", "E"]
    spaces = text.count(" ")

    vowelsNumber = 0
    otherCharacters = 0

    for letter in text:
        for vowel in vowels:
            if letter == vowel:
                vowelsNumber += 1

        otherCharacters += 1

    totalOfOtherCharacters = otherCharacters - vowelsNumber - spaces
    print(
        f"O seu texto possui {vowelsNumber} vogais, {spaces} espaços e {totalOfOtherCharacters} dos demais tipos de caracteres")

elif option == 7:
    print("Obrigado por utilizar nosso sistema.")

else:
    print("Opção inválida.")
