user_weight = int(input("Weight: "))
choice = input("(K)g or (L)bs: ")


if choice.lower() == 'k':
    result = user_weight * 0.453592
    print("Weight in Kg: {0:.3f}".format(result))
elif choice.lower() == 'l':
    result = user_weight / 2.20462
    print("Weight in Lbs: {0:.3f}".format(result))
else:
    print("Please enter the correct choice!")