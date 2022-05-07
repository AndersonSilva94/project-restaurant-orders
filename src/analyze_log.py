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
3 - Com as informações em mãos, fazer um print dos dados num arquivo txt
4 - Fazer um try, except para caso a extensão seja inválida, ou o
arquivo inexistente, retorne uma mensagem de erro
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


def verify_orders_by_joao(data):
    """
    Para responder a primeira questão de joão:
    1 - Criar variáveis que vão armazenar conjuntos de alimentos em geral e
    pedidos de joão
    2 - Esses valores tem que ser únicos, por isso usar o set()
    3 - Percorrer a lista passada como parâmetro, adicionando a comida
    à variável de alimentos em geral
    4 - Ao mesmo tempo, verificar se quem fez o pedido foi joão. Caso sim
    adicionar a comida aos pedidos de joão
    5 - Verificar quais são as comidas não pedidas, fazendo uma subtração do
    total pelos pedidos de joão usando symmetric_difference()
    6 - Método symmetric_difference encontrado no link:
    https://www.w3schools.com/python/python_sets_join.asp
    """
    orders_foods = set()
    joao_orders = set()
    for info in data:
        orders_foods.add(info[1])
        if info[0] == 'joao':
            joao_orders.add(info[1])
    orders_not_made = orders_foods.symmetric_difference(joao_orders)
    return orders_not_made


def verify_days_by_joao(data):
    """
    Para responder a segunda pergunta de joão:
    1 - Utilizar os mesmos princípios da lógica da pergunta anterior
    2 - A diferença é que aqui, vamos armazenar os dias totais e os que
    joão foi à lanchonete.
    3 - Depois ver a diferença entre esses valores
    """
    days = set()
    joao_days = set()
    for info in data:
        days.add(info[2])
        if info[0] == 'joao':
            joao_days.add(info[2])
    days_did_not_go = days.symmetric_difference(joao_days)
    return days_did_not_go


def analyze_log(path_to_file):
    try:
        with open(path_to_file) as csv_file:
            file_data = csv.reader(csv_file)
            list_result = [data_element for data_element in file_data]
            string_result = (
                f"{get_maria_food(list_result)}\n"
                f"{count_arnaldo_order(list_result)}\n"
                f"{verify_orders_by_joao(list_result)}\n"
                f"{verify_days_by_joao(list_result)}"
            )
        with open('data/mkt_campaign.txt', 'w') as new_file:
            print(string_result, file=new_file)
    except FileNotFoundError:
        if not path_to_file.endswith('csv'):
            raise FileNotFoundError(f"Extensão inválida: {path_to_file}")
        else:
            raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")


# analyze_log('data/orders_1.csv')
