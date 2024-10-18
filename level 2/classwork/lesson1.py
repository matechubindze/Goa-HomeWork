name = "mate"
#name არის ცვლადი
# = არის ცვლადისთვის მნიშვნელობის მიმნიჭებელი სიმბოლო
# "mate" არის ცვლადისთვის მნიშვნელობა

surname = "chubinidze"

print(name)
#პრინტ ფუნქციას გადაეცემა ეკრანზე გამოსატანი ობიექტი

name = "mate"  #ეს არის სტრინგ ტიპის ცვლადი
age = 14 # ეს არის int (integer) მთელი რიხვი
height = 161.2 #ეს არის float ტიპის ცვლადი (ათწილადი)
#boolean (bool) ტიპის ცვლადი

know_programming = True
is_ugly = False

isUgly = False # ჯავასკრიპტული camelcase


print(name + " " + surname )

#სტრინგი არის ბრჭყალებში მოქეცეული სიმბოლოები
# print(name + age)

print(type(age))
print(type(name))
print(type(surname))
print(type(height))
print(type(know_programming))

print(name + " " + str(age))

print (name + " " + surname + " " + str(age) + " " + str(height))
