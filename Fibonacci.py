class Fibonacci:
    def printFibonacci(self, n):
        if n < 0:
            print("Invalid input")
            return
        elif n == 1:
            print("1 ")
            return
        elif n == 2:
            print("1 1 ")
            return
        print("1 1", end=" ")
        n1, n2 = 1, 1
        for _ in range(n - 2):
            n3 = n1 + n2
            print(n3, end=" ")
            n1 = n2
            n2 = n3
        print()

    def getFibonacciValue(self, n):
        if n < 2:
            print("Invalid input")
            return
        elif n == 1 or n == 2:
            print("1")
            return

        n1, n2 = 1, 1
        for _ in range(n - 2):
            n3 = n1 + n2
            n1, n2 = n2, n3
        print(n3)


fib = Fibonacci()
n = int(input("Enter the value of n: "))
print("Fibonacci series : ", end=" ")
fib.printFibonacci(n)
print("Fibonacci value of " + str(n) + " is: ", end=" ")
fib.getFibonacciValue(n)
