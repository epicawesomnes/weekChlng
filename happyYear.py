def happyYear(year):
    year = str(year)
    for i in range(len(year)):
        for j in range (i+1, len(year)):
            if year[i] == year[j]:
                return False
    return True
   
year = int(input('enter year'))
while not happyYear(year):    
    year += 1
print(year)