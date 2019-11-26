perfects = []

def perfect_number_tester(n):
    div = []
    for i in range(1, (n-1)):
        if n % i == 0:
            div.append(i)
    if sum(div) == n:
        perfects.append(n)
        return perfects


for item in range(500):
    perfect_number_tester(item)

print(perfects)  
        

