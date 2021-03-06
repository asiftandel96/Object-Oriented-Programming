from Representation_Mixin import AsDictionaryMixin


class Address(AsDictionaryMixin):

    def __init__(self, street, city, state, zipcode, street2=''):
        self.street = street
        self.city = city
        self.street2 = street2
        self.state = state
        self.zipcode = zipcode

    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f'{self.city}, {self.state} {self.zipcode}')
        return '\n'.join(lines)
