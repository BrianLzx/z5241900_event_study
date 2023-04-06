n = input('hours')
n = int(n)
rate = 0
if n <= 35:
    rate = 51.45
    weeklypay = n*rate
else:
    n1 = n-35
    rate = 88.9
    weeklypay = (n1 * rate+35*51.45)
print(weeklypay)