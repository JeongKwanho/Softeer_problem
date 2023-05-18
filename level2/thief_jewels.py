import sys

w, n = map(int, input().split())

weight_price = [list(map(int, input().split())) for _ in range(n)]

price = 0

weight_price.sort(key = lambda x : x[1], reverse = True)

for i in range(n):
    if w > weight_price[i][0]:
        price += weight_price[i][0]*weight_price[i][1]

        w -= weight_price[i][0]
    
    else:
        price += w*weight_price[i][1]
        
        break
        
print(price)
