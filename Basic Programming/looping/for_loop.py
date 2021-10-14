# input section 
num = int(input('Enter the positive integer'))
s = 1
# logic section
for i in range(1,num+1):
    s = s * i

# output section
print('Factorial is', s)
