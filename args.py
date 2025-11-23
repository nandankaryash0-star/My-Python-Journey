def shipping_lable(*args,**kwargs):
    for arg in args:
        print (arg,end=" ")
    print()
    for values in kwargs.values():
        print(values,end=" ")


shipping_lable("Dr.","Steven","Strange",
               street="34 A",
               city="NYC",
               state="washington",
               pin = "5677")