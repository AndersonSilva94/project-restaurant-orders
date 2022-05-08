"""
Requisito 2: Passos a se seguir:
1 - Extrair do sistema as seguintes informações:
    1.1 - Prato favorito por cliente;
    1.2 - Pratos nunca pedidos por cada cliente;
    1.3 - Dias nunca visitados por cada cliente;
    1.4 - Dia mais movimentado;
    1.5 - Dia menos movimentado.
2 - Criar a classe TrackOrders, a qual será lida pelo arquivo src/main.py
3 - A classe retorna alguns métodos:
    3.1 - Conta a quantidade de pedidos
    3.2 - Registra um pedido
    3.3 - Registra o prato mais pedido
    3.4 - Retorna o conjunto de pratos nunca pedidos pela pessoa
    3.5 - Retorna o conjunto de dias que a pessoa nunca visitou
    3.6 - Retorna o dia mais movimentado
    3.7 - Retorna o dia menos movimentado

Lógica a se pensar:
1 - Fazer um constructor de pedidos
2 - Verificar a quantidade de pedidos no método len()
3 - Para adicionar um novo pedido, é preciso fazer um append na lista de
pedidos, com o conjunto de cliente, pedido e dia (nessa ordem)
"""


class TrackOrders:

    def __init__(self):
        self.orders_list = []

    def __len__(self):
        return len(self.orders_list)

    def add_new_order(self, customer, order, day):
        return self.orders_list.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        """
        Utilizei a mesma estrutura usada para veriricar o prato mais pedido
        por maria no requisito anterior
        A diferença aqui que o parametro
        """
        order_by_customer = []
        dict_total_foods = {}
        for info in self.orders_list:
            if info[0] == customer:
                order_by_customer.append(info[1])
        for food in order_by_customer:
            if food in dict_total_foods:
                dict_total_foods[food] += 1
            else:
                dict_total_foods[food] = 1
        most_order = max(dict_total_foods, key=lambda f: dict_total_foods[f])
        return most_order

    def get_never_ordered_per_customer(self, customer):
        pass

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
