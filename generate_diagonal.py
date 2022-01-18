import math

def main():

    def Pascal_triangle_calculation(n,k):
        if k == 0 or n == k:
            return 1
        return (math.factorial(n-1) / (math.factorial(k-1) * math.factorial(n-k)) + (math.factorial(n-1) / (math.factorial(k) * math.factorial(n-k-1))))

    def generate_diagonal(n, l):
        result = []
        for i in range(l):
            result.append(int(Pascal_triangle_calculation(n, i)))
            n = n+1
        return(result)

    def generate_diagonal_bis(n, l):
        return [int(Pascal_triangle_calculation(n, i)) for i,n in zip(range(l), range(n,l+n))]

    def sum_generate_diagonal_bis(n,l):
        return sum([int(Pascal_triangle_calculation(n, i)) for i,n in zip(range(l), range(n,l+n))])


if __name__ == '__main__':
    main()
