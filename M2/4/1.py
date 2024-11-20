class Person:
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

person = Person()
person.first_name = 'John'
person.last_name = 'Doe'
person.id = 5566
# i++ <=> i += 1 <=> i = i + 1
# --i, i--
print(person.full_name())