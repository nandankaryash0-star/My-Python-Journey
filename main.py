def day_of_week(day):
    match day:
        case 1:
            return "It's SUNDAY"
        case 2:
            return "It's MONDAY"
        case 3:
            return "It's TUESDAY"
        case 4:
            return "It's WEDNESDAY"
        case 5:
            return "It's THURSDAY"
        case 6:
            return "It's FRIDAY"
        case 7:
            return "It's SATURDAY"
        

num = int(input("Enter the No. of day "))
print (day_of_week(num))