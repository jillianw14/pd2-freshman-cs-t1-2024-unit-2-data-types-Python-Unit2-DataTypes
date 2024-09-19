""" x = 3
y = float(3)
print(x,y) """
""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)
    print(values[7]) """

""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """

""" sentence = input("This_is_a_sentence: ")
print(len(sentence.split()))

 """

""" verb1=input("Enter verb1: ")
verb1 = ("scootering")
print(verb1)
verb2=input("Enter verb2: ")
verb2 = ("brushing")
print(verb2)
noun=input("Enter noun: ")
noun = ("pencil")
print(noun)
number=input("Enter number: ")
number = ("4")
print(number)
celebrity=input("Enter celebrity: ")
celebrity = ("SZA")
print(celebrity) """
""" 
verb1 = input("Enter verb1: ")
print("Your first verb is: " + verb1) """
""" verb2 = 'brushing'
noun = 'vaccuum cleaners'
number = '4'
celebrity = 'SZA'

print(f"I went {verb1} after getting a {number} {noun} from the store. When I got home, I listened to {celebrity} while {verb2} my hair.") """

""" verb1 = input("Enter verb1: ")
verb2 = input("Eneter verb2: ")
noun = input("Enter noun: ")
number = input("Enter number: ")
celebrity = input("Enter celebrity: ")
print(f"I went {verb1} after getting a {number} {noun} from the store. When I got home, I listened to {celebrity} while {verb2} my hair.")
 """

""" day_of_week = input("what day is it? ")
if day_of_week == "Wednesday":
    print("correct")
else:
    print("incorrect") """

""" x = "class"
print(f"hello {x}") """

""" num = int(input("Enter number: "))
if (num%2) == 0:
    print('even')
else:
    print('odd') """

""" num = int(input("Enter bill amount:"))
service = input("Enter how the service was: " )
if  service == ("bad"):
    print('tip 0%')
elif service == ("okay"):
    print('tip 15%')
elif service == ("good"):
    print('tip 20%')
else:
    print('tip 25%') """

def print_factors(x):
    print("The factors of",x,"are:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)


num = int(input("Enter number: "))
print_factors(num)
