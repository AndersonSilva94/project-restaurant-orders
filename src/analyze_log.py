"""
Requisito 1: Passos a se seguir:
1 - A função recebe como parâmetro um arquivo csv que contém cliente, pedido
    e dia, um por linha.
2 - Esse arquivo de log contém informações de pedidos feitos em todos os dias
    da semana e os pratos que o restaurante oferece
3 - O objetivo da função é ler este arquivo e salvar em outro arquivo .txt, a
    resposta para as perguntas (na mesma ordem):
    3.1 - Qual o prato mais pedido por 'maria'?
    3.2 - Quantas vezes 'arnaldo' pediu 'hamburguer'?
    3.3 - Quais pratos 'joao' nunca pediu?
    3.4 - Quais dias 'joao' nunca foi na lanchonete?

Lógica a se pensar:
1 - Fazer a leitura do arquivo e converter os dados em uma lista
2 - Separar cada pergunta numa função
"""
import csv


def get_maria_food(data):
    """
    Para responder a questão de Maria:
    1 - Criar uma variável que vai armazenar uma lista com pedidos de maria
    2 - Percorrer a lista recebida como parâmetro e quando o nome for maria
    adicionar o valor de comida à variável
    3 - Criar uma variável que vai armazenar um dict com a chave, o nome
    do pedido e o valor, a quantidade de vezes pedida
    4 - Percorrer a lista criada anteriormente, e seguir a lógica na
    variável de dict:
        - Caso o pedido já tenha sido feito, adicionar + 1
        - Caso não, atribuir 1
    5 - Fazer um max() para descobrir a comida mais pedida
    6 - Entendi como usar o max com dict no link:
    https://www.programiz.com/python-programming/methods/built-in/max
    """
    list_foods_by_maria = []
    dict_total_foods = {}
    for info in data:
        if info[0] == 'maria':
            list_foods_by_maria.append(info[1])
    for food in list_foods_by_maria:
        if food in dict_total_foods:
            dict_total_foods[food] += 1
        else:
            dict_total_foods[food] = 1
    most_order = max(dict_total_foods, key=lambda f: dict_total_foods[f])
    return most_order


def count_arnaldo_order(data):
    """
    Para responder a questão de arnaldo:
    1 - Criar uma variável que vai somar toda vez que a comida de arnaldo
    for hamburguer
    2 - Percorrer a lista recebida como parâmetro e verificar se a posição
    0 é arnaldo e a 1 é hambúrguer
    3 - Caso seja, somar + 1 à variável
    """
    hamburguers = 0
    for info in data:
        if info[0] == 'arnaldo' and info[1] == 'hamburguer':
            hamburguers += 1
    return hamburguers


def analyze_log(path_to_file):
    with open(path_to_file) as csv_file:
        file_data = csv.reader(csv_file)
        list_result = [data_element for data_element in file_data]
        print(count_arnaldo_order(list_result))


analyze_log('data/orders_1.csv')
