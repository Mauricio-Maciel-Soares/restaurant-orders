class TrackOrders:

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def get_data_by_person(self, customer):
        return [item for item in self.data if item[0] == customer]

    def add_new_order(self, customer, order, day):
        return self.data.append((customer, order, day))

    def get_most_ordered_dish_per_customer(self, customer):
        order_list = []
        for customer, order, day in self.data:
            if (customer == customer):
                order_list.append(order)

        return max(set(order_list), key=order_list.count)

    def get_never_ordered_per_customer(self, customer):
        customer_list = []
        all_orders = []

        for pedidos in self.data:
            all_orders.append(pedidos[1])

            if pedidos[0] == customer:
                customer_list.append(pedidos[1])

        all_unique_orders = set(all_orders)
        customer_unique_orders = set(customer_list)

        return all_unique_orders.difference(customer_unique_orders)

    def get_days_never_visited_per_customer(self, customer):
        customer_data = self.get_data_by_person(customer)
        days_data = set([item[2] for item in self.data])
        days_customer = set([item[2] for item in customer_data])

        return days_data.difference(days_customer)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
