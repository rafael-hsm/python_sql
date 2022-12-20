import os


# 1. Escreva um programa que compare se duas sequeências digitadas pelo usuário são iguais.
def exerc1_test():
    a = input("Digite a primeira sequência: ")
    b = input("Digete a segunda sequência: ")
    if a == b:
        return "As funções são iguais."
    else:
        return "As sequências não são iguais."


# 2. Escreva um programa que abra um arquivo digitado pelo usuário e imprima seu conteúdo na tela.
directory_ = input("Type directory path or press enter to save in current directory: ")
print(directory_)
if directory_ is not None:
    file = open(directory_)
    line = file.readlines()
    print(line)
else:
    directory_ = os.getcwd() + os.sep + "arquivo_teste.txt"
    print(directory_)
    #
    # file = open("C:\Users\EBJB\Cursos\python_sql\python_intermediario\arquivo_teste.txt")
    line = file.readlines()


# 3 Escreva um programa que receba uma sequência digitada pelo usuário e a salve num arquivo no formato.

seq = input("Digite uma sequência: ")
file = open("seq.fasta", "w")
file.write("seq\n")
file.write(seq)

file.close()

# 4 Escreva um programa que exiba um menu e pergunte o que o usuário deseja fazer. Se o usuário digitar 1, o programa deve chamar uma função que lê um arquivo de texto. Se o usuário apertar 2, o programa dev


if __name__ == '__main__':
    assert exerc1_test() == "As funções são iguais."
    