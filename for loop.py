# for loops - fixed number of times

for x in (range(1,11,2)):
    print(x)


print("Happy New Year!!!")

for x in range(1,21):
    if x == 13:
        continue  # skip and if break then loop end
    else:
        print(x)