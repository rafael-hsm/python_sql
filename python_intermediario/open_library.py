# -*- coding: utf-8 -*-

file = open("C:\\Users\\rafam\\Projects\\python_sql\\python_intermediario\\arquivo_teste.txt")

lines = file.readlines()

for line in lines:
    print(line)
    
w = open("file2.txt", "w")
w.write("Esse é o meu arquivo")
w.close()