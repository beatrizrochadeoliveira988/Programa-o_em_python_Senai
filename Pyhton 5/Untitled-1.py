# #try:
#     x  =  int(input('>')) 


#     n = 10
#     n2 = 0
#     print(n/n2)
# except ValueError as erro:
#     print(erro)
# except ZeroDivisionError as erro:
#     print(erro)    
# else:
#     print('erro não identificado ')


# finally:
#     print('fim de carregamento... ')

# try:
#     numero = int(input("Digite um número inteiro: "))
#     print(f"Você digitou o número {numero}.")
# except ValueError:
#     print("Erro: você não digitou um número inteiro válido!")
# finally:
#     print("Programa finalizado.")

# try:
#     num1 = float(input("Digite o primeiro número: "))
#     num2 = float(input("Digite o segundo número: "))

#     resultado = num1 / num2
#     print(f"O resultado da divisão é: {resultado}")
# except ValueError:
#     print("Erro: não é possível dividir por zero!")
# finally:
#     print("Programa finalizado.")

# try:
#     # Criando uma lista com alguns elementos
#     lista = [10, 20, 30, 40, 50]
#     print("Lista:", lista)
#     # Pedindo ao usuário um índice
#     indice = int(input("Digite o índice que deseja acessar (0 a 10): "))

#     # Tentando acessar o elemento da lista
#     print(f"O valor no índice {indice} é {lista[indice]}")

# # Se o usuário digitar algo que não é número
# except ValueError:
#     print(" Erro: digite apenas números inteiros.")

# # Se o índice for maior ou menor que o tamanho da lista
# except IndexError:
#     print("Erro: esse índice não existe na lista.")

# # Sempre executa no final
# finally:
#     print("✅ Programa finalizado."