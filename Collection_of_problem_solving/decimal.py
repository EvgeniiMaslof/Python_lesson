num = float(input('Enter a real nuber: '))
_, accu = input('Enter the required accuracy "0.0001": ').split('.')
print(f'{num:.{len(accu)}f}')
