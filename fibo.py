width = 10-2
fibo= [0, 1]
for x in range(width):
    fibo.append(fibo[-1]+fibo[-2])
print(fibo)