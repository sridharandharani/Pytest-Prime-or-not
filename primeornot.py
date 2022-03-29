def primeornot(x):
    for i in range(2, x):
        if (x % i == 0):
            return False
            break
        else:
            return True

if __name__ == "__main__":
    x = int(input("Enter the number :"))
    result = primeornot(x)
    print(result)