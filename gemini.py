def reverse(x):
    sign = -1 if x < 0 else 1
    rev = int(str(abs(x))[::-1])
    return sign * rev


print(reverse(120))