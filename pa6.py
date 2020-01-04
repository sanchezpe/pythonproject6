###### PrintHeader Function ######
def PrintHeader():
    print('+------------------------------------+')
    print('+                                    +')
    print('+           SuperMarket XYZ          +')
    print('+        Where You Always Save !     +')
    print('+                                    +')
    print('+            Sales Receipt           +')
    print('+          October 23, 2015          +') 
    print('+                                    +')
    print('+------------------------------------+')

###### Compute Function ######
def ComputeTax(amount,taxRate):
    tax = amount * taxRate
    return tax 

###### MaxItems Function ######
def MaxItems(countC,countP,countH,countO):
    if countC > countP and \
        countC > countH and \
        countC > countO:
        return 'C'

    elif countP > countC and \
        countP > countH and \
        countP > countO:
        return 'P'

    elif countH > countC and \
        countH > countP and \
        countH > countO:
        return 'H'

    else:
        return 'O'

    return maxItem

###### MaxSpent Function ######
def MaxSpent(sumC,sumP,sumH,sumO):
    if sumC > sumP and \
        sumC > sumH and \
        sumC > sumO:
        return 'C'

    elif sumP > sumC and \
        sumP > sumH and \
        sumP > sumO:
        return 'P' 
        
    elif sumH > sumC and \
        sumH > sumP and \
        sumH > sumO:
        return 'H'

    else:
        return 'O'        

###### Main Function ######
def main():

    PrintHeader()

    inFile = open('pa6.input', 'r')
    
    depLetter = inFile.readline().strip()
    itemCost = eval (inFile.readline().strip())
    
    depName = ''
    subtotalNonFood = 0
    subtotalFood = 0
    countC, countP, countH, countO = 0, 0, 0, 0
    sumC,sumP,sumH,sumO = 0, 0, 0, 0
     
    while depLetter != 'X':
        
        if depLetter == 'C':
            depName = 'Clothes'
            subtotalNonFood += itemCost            
            countC +=1
            sumC +=itemCost

        elif depLetter == 'P':
            depName = 'Produce'            
            subtotalFood += itemCost
            countP +=1
            sumP +=itemCost
        
        elif depLetter == 'H':                                  
            depName = 'Hardware'
            subtotalNonFood += itemCost 
            countH +=1 
            sumH +=itemCost

        elif depLetter == 'O':
            depName = 'Other'
            subtotalNonFood += itemCost
            countO +=1
            sumO +=itemCost

        # do not use else in order to exlcude items 
        # break statement or continue statement do not work with else
                                                        
        print('   ', format(depName,'14s'), format(itemCost, '14.2f'))
        depLetter = inFile.readline().strip()
        itemCost = eval (inFile.readline().strip())
        
    inFile.close()


    print('   -------------------------------')
    print('   ',format('Subtotal (food):','14'), format(subtotalFood, '12.2f' ))
    print('   ',format('Subtotal (non-food):','14'), format(subtotalNonFood, '8.2f'))
    
    taxFood = ComputeTax(subtotalFood, 2/100)
    taxNonFood = ComputeTax(subtotalNonFood, 8.5/100)
    print('   ', format('Tax (food):', '14'), format(taxFood, '14.2f'))
    print('   ', format('Tax (non-food):', '14'), format(taxNonFood, '13.2f'))

    print('   -------------------------------')
    total = subtotalFood + subtotalNonFood + taxFood + taxNonFood
    print('   ', format('Total:', '14'), format(total, '14.2f'))
   
    
    print('---------------------------------------')
    maxItem = MaxItems(countC,countP,countH,countO)
    
    if maxItem == 'C':
        maxDep = 'Clothes'
        maxCount = countC

    elif maxItem == 'P':
        maxDep = 'Produce'
        maxCount = countP

    elif maxItem == 'H':
        maxDep = 'Hardware'
        maxCount = countH
    
    else:
         maxDep = 'Other'
         maxCount = countC

    print('Maximum Items:   ', format(maxDep, '10'), format(maxCount, '7'))
   
    
    maxCost = MaxSpent(sumC,sumP,sumH,sumO)

    if maxCost == 'C':
        maxDep = 'Clothes'
        maxSum = sumC

    elif maxCost == 'P':
        maxDep = 'Produce'
        maxSum = sumP

    elif maxCost == 'H':
        maxDep = 'Hardware'
        maxSum = sumH
    
    else:
         maxDep = 'Other'
         maxSum = sumO

    print('Maximum Cost:    ', format(maxDep, '10'), format(maxSum, '10.2f'))

main()
