class Solution:
    def tempConv(self):
        curr = int(input("What is your temperature scale? Enter 1: Celsius, 2: Kelvin, 3: Rankine, 4: Fahrenheit "))
        next = int(input("What scale do you want to convert to? Enter 1: Celsius, 2: Kelvin, 3: Rankine, 4: Fahrenheit "))
        val = int(input("What is the temperature? "))

        if curr == 1:
            answer = (val * 9/5) + 32
            return f"Your converted temperature is {answer} Fahrenheit"

        if curr not in range(1, 5) or next not in range(1, 5) or val < 0:
            return "Invalid input. Please select numbers 1-4 for your respective scale."

        # Add other conversion calculations for different scales here

        return "Conversion completed."

solution = Solution()
print(solution.tempConv())