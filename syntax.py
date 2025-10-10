try:
    number = int(input("Enter a number:"))
    print("The number enter is", number )
except ValueError as ex:
    print("Exceptinon:" , ex)