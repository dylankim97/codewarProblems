def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

answer = create_phone_number(n)
print(answer)




#format with {}
string = "{program} is so {1}".format("great", "good", program = "python")
print(string)

#real application

#-------

#Asterisk unpacks iterable objects. Double asterisks is used for dictionary

#unpack list
L = [1, 2, 3, 4, 5, 6]
print(*L)
#prints 1 2 3 4 5 6 BUT WHAT IS THE DATA TYPE?? 

#divide lists
a, *b, c = L
print(b) 
#prints [2, 3, 4, 5]

#merger lists
L_1 = [1, 2, 3]
L_2 = [4, 5, 6]
L_F = [*L_1, *L_2]
print(L_F) 
#prints [1, 2, 3, 4, 5, 6]

#unpack dict and merge them using double asterisk
dict_1 = {'one':1, 'two':2}
dict_2 = {'three':3, 'four':4}
dict_F = {**dict_1, **dict_2}
print(dict_F) 
#prints {'one': 1, 'two': 2, 'three': 3, 'four': 4}

#unpack string
ex = 'what is up'
print(*ex) 
#prints w h a t   i s   u p


print("what is the number, {0:10f}?".format(30))