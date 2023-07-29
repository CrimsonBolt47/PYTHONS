coins = [2,202,2,3,200,4,5]

pro = []

for i in coins :
    pro.append(i)



for i in range (1,len(coins)):

    for j in range (0,i):
      if coins[j] + pro[i] > pro[i] and  coins[i]>coins[j]: 
        pro[i]=pro[j] + coins[i]
        
print(pro)
