class Prime(object):

    def __init__(self):

        if self.is_prime() == True:
            self.__str__()
            
    def __str__(self):

        print("({}) given number is a prime number".format(self.number))

    def is_prime(self):

        self.number = int(input("Enter an integer: "))
        if self.number < 0 :
            print("Prime numbers can not be negative")
        elif self.number == 1:
            print("{} is not a prime number".format(self.number))
        else:
            for i in range(2,self.number):
                if self.number % i == 0:
                    print("({}) is not a prime number".format(self.number))
                    return False
                
            return True


        
