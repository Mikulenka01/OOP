from Stack import Stack

"""-> datova struktura
-> zlozitost
-> asymptoticka zlozitost
-> amortizovna zlozitost
-> najhorsi pripad


adresa + index * velkost pametovej bunky

class Node:
    def __init__(self, value):
        self.value = value
        self.neighboors = [( 2 ,n1), n2, n3]


n4.neighboors = [n3]
n3.neighboors = [( 2 ,n1), n2]"""

s = Stack()
print(s.is_empty())
print(s)

s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.is_empty())
print(s)
print(s.pop())
print(s.pop())
print(s.pop())
print(s)