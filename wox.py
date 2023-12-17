import sys

def findWoxNumber(number1 = int, number2 = int):
    m = number1
    n = number2
    #####m The sum of the divisors of the numbers excluding themselves 
    divisors=[] 
    total=0  ##### sum of divisors  
    for i in range(m): 
        if(i==0 or i==m): 
           continue 
        if(m%i==0): 
           total+=i 
           divisors.append(i) 
    
    #####Does the sum of the divisors equal n?
    divisors_2 = []
    total_2 = 0
    if total == n:
        for x in range(n):
            if (x == 0 or x == n):
                continue
            if (n%x==0):
                total_2+=x
                divisors_2.append(x)

    ######
    if total == n and total_2 == m and total != 0 and m != n:
        print(f'The answer is: {m, n} numbers are wox numbers.')
        sys.exit()

def findFirstTwoWoxNumber():
    list_of_duos = []
    for x in range(0,1500):
        m = x
        for y in range(0,1500):
            n = y 
            result = (m,n)
            list_of_duos.append(result)
    for x in list_of_duos:
        findWoxNumber(x[0], x[1])
        
findFirstTwoWoxNumber()