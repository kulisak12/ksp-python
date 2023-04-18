import sys

# jméno programu
print(sys.argv[0])

sum = 0
for arg in sys.argv[1:]:
    sum += int(arg)
print(sum)
