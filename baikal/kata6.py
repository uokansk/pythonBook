def numbers(n):
    if n < 0:
        n = 0

    elif n > 255:
        n = 255
    print(n)
    return n



def rgb(r, g, b):
    result = ("{:02X}" * 3).format(numbers(r), numbers(g), numbers(b))

    return result.upper()


if __name__ == '__main__':
    sol = rgb(1, 2, 3)
    print(sol)
