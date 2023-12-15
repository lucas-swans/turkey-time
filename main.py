cooking = input("would you like to estimate a cook time?(yes/no) ")

if cooking == "yes":
    cook = True

while cook:
    turkeyType = input("Is the turkey stuffed or unstuffed?(s/un) ")
    turkeyTime = float(input("How much does the turkey weigh? "))

    if turkeyType == "s":
        turkeyTime = turkeyTime * 15
    elif turkeyType == "un":
        turkeyTime = turkeyTime * 13
    
    minutes = turkeyTime % 60
    turkeyTime = turkeyTime - minutes
    turkeyTime = turkeyTime/60

    turkeyTime = int(turkeyTime)
    minutes = int(minutes)

    print("The turkey will take " + str(turkeyTime) + ":" + str(minutes))

    cooking = input("would you like to estimate another cook time?(yes/no) ")

    if cooking == "yes":
        continue
    elif cooking == "no":
        break