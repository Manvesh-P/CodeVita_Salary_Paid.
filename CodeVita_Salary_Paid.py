
tax = []
salaries = []

n = 4

S1, S2, S3 = map(int, input("Enter the amount in each slab: ").split(" "))
P1, P2, P3 = map(int, input("Enter the percentage of tax in each salb: ").split(" "))
rebate = int(input("Enter the rebate amount: "))


for i in range(0, n):
    tax.append(int(input("Enter the tax paid by employee %d: "%(i+1))))

for j in range(0, len(tax)):
    
    if tax[j] == 0:
        x = 300000 + rebate
        
    elif tax[j] > 0 and tax[j] <= 30000:
        
        a = 300000 + rebate
        
        x = (tax[j] * (100 / P1)) + a
        
    elif tax[j] > 30000 and tax[j] <= 90000:
        
        a = 300000 + rebate
        b = 300000
        
        x = ((tax[j] - 30000) * (100 / P2)) + (a + b)
        
    elif tax[j] > 90000:
        
        a = 300000 + rebate
        b = 300000
        c = 300000
        
        x = ((tax[j] - (30000 + 60000)) * (100 / P3)) + (a + b + c)
        
    salaries.append(round(x))
    
    
    
    
# print(salaries)

print("\nThe salariy paid to each employee is: ")

for i in range(0, len(salaries)):
    print(salaries[i], end=' ')
    
    
print("\n\nThe total salary paid to all the employees in that year is: ", sum(salaries))
