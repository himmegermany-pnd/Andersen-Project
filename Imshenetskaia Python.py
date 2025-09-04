
#If the entered number is greater than 7, then print “Hello”
num = int(input("Enter the number, please:"))
if num > 7:
    print("Hello")

#If the entered name matches “John”, then output “Hello, John”, if not, then output "There is no such name"
name = str(input("Enter the name, please:"))
if name == "John":
    print("Hello, John")
else:
    print("There's no such name")

#There is a numeric array at the input, it is necessary to output array elements that are multiples of 3
arr = list(map(int, input("Enter numbers separately:").split(" ")))
divisibleBy3 = []
for i in arr:
    if i % 3 == 0:
        divisibleBy3.append(i)
print("This numbers are divided by 3: ", divisibleBy3)


