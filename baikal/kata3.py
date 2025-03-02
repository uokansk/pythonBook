# В этом небольшом задании вам дана строка чисел, разделенных пробелами,
# и вам нужно вернуть наибольшее и наименьшее число.
from natsort import natsorted


def high_and_low(numbers):
    a = numbers.split()
    int_list = [int(i) for i in a]
    int_list.sort()
    print(type(int_list))
    b = str(int_list[-1]), str(int_list[0])

    print(type(b))
    string1 = ' '.join(b)

    return string1


if __name__ == '__main__':
    sol = high_and_low("8 3 -5 42 0 0 -9 4 7 4 -4")
    print(sol)

"""
def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))

//////////////////////////////////

def high_and_low(numbers):
    nums = sorted(numbers.split(), key=int)
    return '{} {}'.format(nums[-1], nums[0])
    
    
    //////////////////////////
    
def high_and_low(numbers):
  numbers = [int(c) for c in numbers.split(' ')]
  return f"{max(numbers)} {min(numbers)}"

"""