costprice = int (input("Please enter the cost price"))
sellingprice = int (input("Please enter the selling price"))
answer = sellingprice - costprice 
if sellingprice > costprice :
    print("It is a PROFIT" , answer)
elif sellingprice < costprice :
    print("It is a LOSS ", answer)
 
