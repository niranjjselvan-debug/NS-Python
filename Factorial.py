class Factorial:
    # Using regular while loop logic
    def findFactorial(self, n):
        result = 1
        if n == 0 or n == 1:
            return 1
        while n > 1:
            result *= n
            n -= 1
        return result

    # Using for loop logic
    def factorial_loop(self, num):
        if num < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result

    # Using recursive logic
    def factorial_recursive(self, num):
        if num < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if num == 0 or num == 1:
            return 1
        return num * self.factorial_recursive(num - 1)

# Driver code
f = Factorial()
input_01 = int(input("Enter the value of n to find the factorial: "))

print(f"Using while loop: {f.findFactorial(input_01)}")
print(f"Using for loop: {f.factorial_loop(input_01)}")
print(f"Using recursion: {f.factorial_recursive(input_01)}")
