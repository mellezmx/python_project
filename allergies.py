
def main():
    class Allergies():

        def __init__(self, name, score):
            self.dict_of_allergies = {1:'eggs', 2:'peanuts', 4:'shellfish', 8:'strawberries' ,16:'tomatoes',32:'chocolate',64:'pollen',128:'cats'}
            self.name = name
            self.score = score

        def reverse_string(self, st):
            str1 = ""   # Declaring empty string to store the reversed string
            for i in st:
                str1 = i + str1
            return str1    # It will return the reverse string to the caller function


        def define_allergie_to(self):
            list_of_allergie = []
            allergie_to = self.reverse_string(bin(self.score).replace('0b', ''))
            for index, allergie in enumerate(allergie_to):
                if allergie == '1':
                    list_of_allergie.append(self.dict_of_allergies[2**int(index)])
                if index == 7:
                    break
            return list_of_allergie


    a = Allergies('p', 43568)
    print(a.define_allergie_to())




if __name__ == '__main__':
    main()
