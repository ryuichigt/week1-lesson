
def Vacation(vacation,rainy_percent,day):
	rp_sum = 100*vacation[1]

	for i in range(vacation[0]- vacation[1] + 1):
		if rp_sum > sum(rainy_percent[i:i+vacation[1]]):
			rp_sum = sum(rainy_percent[i:i+vacation[1]])
			days = [day[i],day[i+vacation[1]-1]]

	days = list(map(str,days))   
	result = " ".join(days)

	return result



vacation = [7,3]
day = [19,20,21,22,23,24,25]
rainy_percent = [0,0,60,30,10,10,90]

print(Vacation(vacation, rainy_percent, day))