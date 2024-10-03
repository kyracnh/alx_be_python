def safe_divide(numerator, denominator):
    try:
        numerator = float(num1)
        denominator = float(num2)

        result = num1 / num2
        return result
    except ValueError:
        return "Error: Both inputs must be numbers."
    
    except ZeroDivisionError:
        print("Error: You can not divide by Zero.")
    