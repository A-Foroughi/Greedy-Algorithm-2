# This program shows you the most amount of cake you can buy with your money.
# It takes weight and price of cakes in order.
money = int(input("How much money you have? "))
weights = [int(i) for i in input("Enter the cakes' weights in order. ").split()]
prices = [int(i) for i in input("Enter the cakes' prices in order. ").split()]
p_w = [0] * len(weights)
for i in range(len(weights)):
    p_w[i] = prices[i] / weights[i]
for j in range(len(p_w)):
    for y in range(1, len(p_w)):
        if p_w[y] < p_w[y - 1]:
            p_w[y], p_w[y - 1] = p_w[y - 1], p_w[y]
            prices[y], prices[y - 1] = prices[y - 1], prices[y]
            weights[y], weights[y - 1] = weights[y - 1], weights[y]
n = 0
for i in range(len(p_w)):
    if money >= prices[i]:
        money -= prices[i]
        print(f"You can buy all of the {p_w[i]} Dollors per Kilo cake. and your remaining money is {money}")
        n += weights[i]
    if 0 < money < prices[i]:
        print(f"You can buy {money / prices[i]} of the {p_w[i]} Dollors per Kg cake. and you have no more money.")
        n += money / prices[i] * weights[i]
        print(f"You have totally bought {n} kg cake.")
        break