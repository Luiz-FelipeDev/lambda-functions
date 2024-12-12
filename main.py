## Expression Lambdas in Python

'''Crie uma função lambda que receba um número e retorne o dobro do número.'''

dobro = lambda x: x**2

print(dobro(2))

'''Use uma expressão lambda com filter 
para filtrar apenas os números pares de uma lista'''

numeros = [1, 2, 3, 4, 5, 6]

pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

print("****************************")


# fazendo a função acima só com list comprehension:

numeros_pares = lambda nums:[x for x in nums if x % 2 == 0]
numeros_pares(numeros)
print(pares)


'''Utiliza uma list comprehension dentro de uma lambda para 
filtrar palavras que começam com uma letra fornecida: '''

filtra_palavras = lambda palavras, letra:[palavra for palavra in palavras if palavra.startswith(letra)]
palavras = ["joão", "joaquim", "jonas", "luiz", "felipe", "mateus"]
print(filtra_palavras(palavras, "j"))

