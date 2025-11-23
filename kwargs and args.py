def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print()

    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')}")


shipping_label("Dr.","Steven","Strange",
               street = "45 tax St. ",
               city = "New York",
               state = "Amarica",
               pin = "4533")