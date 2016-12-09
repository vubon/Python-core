class Student:

    def __init__(self, first, last, fee):
        self.fname = first
        self.lname = last
        self.fee = fee
        self.email = first + '.' + last + '@' + 'edu.bd'

stu_one = Student('Vubon', 'Roy', 7000)
stu_two = Student('Smrity', 'Roy', 5000)

print('Name: ' +stu_one.fname +' '+ stu_one.lname + '\n'+ 'Fee: '+str(stu_one.fee) + '\n' + 'E-mail: ' + stu_one.email )
print('Name: ' +stu_two.fname +' '+ stu_two.lname + '\n'+ 'Fee: '+str(stu_two.fee) + '\n' + 'E-mail: ' + stu_two.email )
