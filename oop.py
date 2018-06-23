# Classes & Objects
class Person:
    # __ means private
    __name = ''
    __email = ''

    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def to_string(self):
        return '{} can be contacted at {}'.format(self.__name, self.__email)


person = Person('vuk samardžić', 'samardzic.vuk@gmail.com')


# person.set_name('vuk')
# person.set_email('samardzic.vuk@gmail.com')

# print(person.get_name(), person.get_email())
# print(person.to_string())

class Customer(Person):
    __balance = 0

    def __init__(self, name, email, balance):
        super().__init__(name, email)
        self.__balance = balance

    def set_balance(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def to_string(self):
        return '{} has the balance of {} and can be contacted at {}'.format(self.get_name(), self.__balance,
                                                                            self.get_email())


customer = Customer('John Doe', 'jdoe@gmail.com', 100)
print(customer.to_string())
