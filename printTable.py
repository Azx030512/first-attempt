tableData = [['apples','oranges','cherries','banana'],
                     ['Alice','Bob','Carol','David'],
                     ['dogs','cats','moose','goose']]
def printTable(exampleTable):
    colWidths=[]
    for x in range(len(exampleTable)):
        colWidths.append(len(exampleTable[x][0]))
        for y in range(len(exampleTable[x])):
            if len(exampleTable[x][y])>=colWidths[x]:
                colWidths[x]=len(exampleTable[x][y])
    for y in range(len(exampleTable[0])):
        printTable=''
        for x in range(len(exampleTable)):
            printTable+=exampleTable[x][y].rjust(colWidths[x]+3)
        print(printTable)
printTable(tableData)            
