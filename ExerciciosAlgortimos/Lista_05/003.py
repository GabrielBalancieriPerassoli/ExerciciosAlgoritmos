a = [1, 0, 5, -2, -5, 7]

soma = a[0] + a[1] + a[5]
print(soma)

a[4] = 100
print(a)

i = 0 
while(i < len(a)): # Testando usando Loop
    print(a[i])
    i += 1

print('================')
# Testando sem Loop
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
