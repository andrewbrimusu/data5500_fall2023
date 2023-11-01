prices = [ float(line) for line in open("/home/ubuntu/environment/data5500_fall2023/week5_lists_queues_stacks/queues_plus_stock_example/AAPL.txt") ]
print(prices)


file = open("/home/ubuntu/environment/data5500_fall2023/week5_lists_queues_stacks/queues_plus_stock_example/AAPL.txt")
lines = file.readlines()
for line in lines:
    prices.append(float(line))
    
    

