def func_abs(num):
    if type(num) == type(1) or type(num) == type(1.0):
        if num >= 0:
            return num
        else: return -num
    elif type(num) == type(1j):
        return (num.real **2 + num.imag ** 2) ** (1/2)
    else:
        raise TypeError()
    
A=func_abs(-3)
print(A)