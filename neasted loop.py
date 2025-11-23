# nested loop = A loop within another loop(outer, inner)
row = int(input("Enter the number of rows: "))
colum = int(input("Enter the number of columns:  "))
symbol= input("Enter the symbol:  ")



for x in range(row):
    for y in range(colum):
        print(symbol,end="")
    print()
