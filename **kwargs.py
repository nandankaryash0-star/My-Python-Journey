def print_address(**kwargs):
    for key,values in kwargs.items():
        print(f"{key}: {values}")

print_address(street="54 Ave",
              city="Nagpur",
              state="Maharashtra",
              pin="4399")