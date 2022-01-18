from decorators import timer
import math

def main():
    def primeFactors(n):
        prime_list = []

        # Print the number of two's that divide n
        while n % 2 == 0:
            prime_list.append(2)
            n = n / 2

        # n must be odd at this point
        # so a skip of 2 ( i = i + 2) can be used
        for i in range(3,int(math.sqrt(n))+1,2):

            # while i divides n , print i and divide n
            while n % i== 0:
                prime_list.append(i)
                n = n / i

        # Condition if n is a prime
        # number greater than 2
        if n > 2:
            prime_list.append(n)
        return prime_list


    @timer
    def my_count_Kprimes(k, start, nd):#5, 500, 600
        result = []
        count = 0
        x = 2

        for num in range(start, nd+1):
            temp_num = num

            while(x <= temp_num):
                if temp_num % x == 0:
                    temp_num = int(temp_num / x)
                    count += 1
                    if temp_num == 1:
                        if count == k:
                            result.append(num)
                        count = 0
                        x = 2
                        break
                else:
                    x+=1
        return result
    @timer
    def count_Kprimes(k, start, nd):
        result = []

        for num in range(start, nd+1):
            if len(primeFactors(num)) == k:
                result.append(num)
        return result

    @timer
    def puzzle(s):
        prime_1 = []
        prime_3 = []
        prime_7 = []
        count = 0

        prime_1 = count_Kprimes(1, 2, s)
        prime_3 = count_Kprimes(3, 8, s)
        prime_7 = count_Kprimes(7, 128, s)
        for z in prime_7:
            for y in prime_3:
                for x in prime_1:
                    if sum([z,y,x]) == s:
                        count +=1
                        break
                    elif sum([z,y,x]) > s:
                        break
                if sum([z,y]) > s:
                    return count # [3 + 12 + 128] and [7 + 8 + 128]


    #print(count_Kprimes(1, 2, 138))
    #print(puzzle(1234565))
    #primeFactors(6)


if __name__ == '__main__':
    main()
