import math

def main():
    def lcm(*args):
        my_arg = [item for item in args]
        lcm = my_arg[0]
        for i in range(1,len(my_arg)):
            a = math.gcd(lcm, my_arg[i])
            try:
                lcm = lcm*my_arg[i]//math.gcd(lcm, my_arg[i])
            except:
                lcm = 0
        return lcm


    print(lcm(1,2,3,4,5))
    #print(primeFors(2))

if __name__ == '__main__':
    main()

#6,7,8

#2.3  7  2.2.2 -> 2.2.2.3.7