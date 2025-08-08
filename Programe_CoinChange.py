def Fn(coins, target):
    d = [0] * (target + 1)
    d[0] = 1
    for coin in coins:
        for count in range(coin, target + 1):
            d[count] += d[count - coin]
    return d[target]


a = [1,2,5,10]
target = 10
print(Fn(a,target))
