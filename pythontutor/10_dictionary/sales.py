dict = {}

while True:
    try:
        client, product, count = input().split()
        if client not in dict:
            dict[client] = {product: int(count)}
        else:
            dict[client][product] = dict[client].get(product, 0) + int(count)
    except:
        break


for client in sorted(dict):
    print(client + ":")
    for product in sorted(dict[client]):
        print(product, dict[client][product])
