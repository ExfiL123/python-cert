n = 462825624
digits_str = str(n)
result = []

result.append(False)

for i in range(1, len(digits_str)):
    current_digit = int(digits_str[i])
    left_digit = int(digits_str[i - 1])
    
    if left_digit != 0 and current_digit % left_digit == 0:
        result.append(True)
    else:
        result.append(False)

print(result)
