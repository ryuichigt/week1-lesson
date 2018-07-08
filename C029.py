# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

vacation = input().split()
vacation = list(map(int,vacation))

rainy_percent = []
day = []

for i in range(vacation[0]):
    rainy = input().split()
    rainy = list(map(int,rainy))
    rainy_percent.append(rainy[1])
    day.append(rainy[0])

#rainy_percent rpの略

rp_sum = 100*vacation[1]

days = []

for i in range(vacation[0]- vacation[1] + 1):
    if rp_sum > sum(rainy_percent[i:i+vacation[1]]):
        rp_sum = sum(rainy_percent[i:i+vacation[1]])
        days = [day[i],day[i+vacation[1]-1]]

days = list(map(str,days))   
print(" ".join(days))