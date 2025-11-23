def hello(greeting , title , first , last ):
    print (f" {greeting} {title} {first} {last}")

hello("Hello","Mr.",last="Squarepant",first="Spongebob" )

def phone_num(country,area,first,last):
    return f" {country} {area} {first} {last}"

get_phone = phone_num(country=1,area=44,first=1234,last=5678)

print(get_phone)