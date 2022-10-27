import csv


def get_data(path_to_file):
    with open(path_to_file, newline="") as csvfile:
        fieldnames = ["customer", "order", "day"]
        return list(csv.DictReader(csvfile, fieldnames=fieldnames))


def get_data_by_person(customer, data):
    return [item for item in data if item["customer"] == customer]


def get_most_ordered_by_person(data):
    count = {}
    most_ordered = data[0]["order"]
    for item in data:
        if item["order"] not in count:
            count[item["order"]] = 1
        else:
            count[item["order"]] += 1

        if count[item["order"]] > count[most_ordered]:
            most_ordered = item["order"]

    return most_ordered


def get_order_qty_by_person(data, order_name):
    order_quantity = 0
    for item in data:
        if item["order"] == order_name:
            order_quantity += 1
    return order_quantity


def get_never_ordered_by_person(customer_data, data):
    orders_data = set([item["order"] for item in data])
    orders_customer = set([item["order"] for item in customer_data])

    return orders_data.difference(orders_customer)


def get_days_that_never_went(customer_data, data):
    days_data = set([item["day"] for item in data])
    days_customer = set([item["day"] for item in customer_data])

    return days_data.difference(days_customer)


def write_file(target_path, data):
    f = open(target_path, "w")
    for item in data:
        f.write(f"{item}\n")
    f.close()


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    else:
        try:
            data = get_data(path_to_file)
            maria_data = get_data_by_person("maria", data)
            arnaldo_data = get_data_by_person("arnaldo", data)
            joao_data = get_data_by_person("joao", data)
            response1 = get_most_ordered_by_person(maria_data)
            response2 = get_order_qty_by_person(arnaldo_data, "hamburguer")
            response3 = get_never_ordered_by_person(joao_data, data)
            response4 = get_days_that_never_went(joao_data, data)

            path_to_file = "data/mkt_campaign.txt"
            write_file(path_to_file, [response1,
                       response2, response3, response4])
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
