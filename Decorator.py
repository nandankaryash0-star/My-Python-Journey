


def add_sprinkles(func):
    def wrapper(*args,**kwargs):
        print("You have added sprinkles 🍇")
        func(*args,**kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args,**kwargs):
        print("You have added fudge 🍪")
        func(*args,**kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavour):
    print(f"Here is your {flavour} icecream 🍨")


get_ice_cream("Vanilla")