"""
Функция rgb неполная. Завершите ее так, чтобы передача десятичных значений RGB приводила к возврату
шестнадцатеричного представления. Допустимые десятичные значения для RGB: 0 - 255. Любые значения,
выходящие за пределы этого диапазона, должны быть округлены до ближайшего допустимого значения.

Примечание: Ваш ответ всегда должен состоять из 6 символов, сокращение с 3 здесь не подойдет.

Примеры (вход -> выход):
255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"
"""


# def rgb(r, g, b):
#     if r < 0:
#         r = 0
#     elif r > 255:
#         r = 255
#     if g < 0:
#         g = 0
#     elif g > 255:
#         g = 255
#     if b < 0:
#         b = 0
#     elif b > 255:
#         b = 255
#
#     r_hex = (hex(r)[2:])
#     if len(r_hex) < 2:
#         r_hex=('0'+r_hex)
#     g_hex = (hex(g)[2:])
#     if len(g_hex) < 2:
#         g_hex = ('0'+ g_hex)
#     b_hex = (hex(b)[2:])
#     if len(b_hex) < 2:
#         b_hex = ('0'+ b_hex )
#     result = (r_hex + g_hex + b_hex)
#
#     return result.upper()
#
#
# if __name__ == '__main__':
#     sol = rgb(255, 255, 255)
#     print(sol)
#     print(type(sol))

"""
def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))
"""


def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))


if __name__ == '__main__':
    sol = rgb(1, 2, 3)
    print(sol)

