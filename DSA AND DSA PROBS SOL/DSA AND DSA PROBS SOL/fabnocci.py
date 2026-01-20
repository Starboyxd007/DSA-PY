def fabonocci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fabonocci(n - 1) + fabonocci(n - 2)

print(fabonocci(7))
