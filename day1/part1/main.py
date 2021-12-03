count = 0
previousNum = int(input())

for i in range(1999):
    currentNum = int(input())

    if currentNum > previousNum:
        count += 1
    previousNum = currentNum

print(count)