number=1
limit=int(input('Max value= '))
for number in range(1,100,1):
    squareValue=number*number
    print (number, squareValue)
    if squareValue>=limit:
        break
