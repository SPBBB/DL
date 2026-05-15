# 오늘문풀하고 쫑

## Lab2. Dict. 

# 1. [Parse colon pairs to dictionary]

line = input("Enter input text: ") # ex: 'name:alice age:21 dept:AI'

key_value = line.split() # [ 'key:value', 'key:value', . .]

line_dict = {}
for i in key_value:
    dict_item = i.split(':') # [key,value]
    line_dict[dict_item[0]] = dict_item[1]
    
print(line_dict)


# 2. [Group numbers by parity]

num_line = input("Enter your number set: ") # ex: '3 4 5 6 7 8'
nums = num_line.split() # ['3','4','5', .. , '8']

# conversion of the type of each nums's element (str to int) 
for i in range(len(nums)) :
    nums[i] = int(nums[i]) 

parity_dic = {'even':[],'odd':[]}

for n in nums : 
    if n%2 == 0 : # if even 
        parity_dic['even'].append(n)
    else : 
        parity_dic['odd'].append(n)

print(parity_dic)


# 3. [Address Book] : Build a command-line address book that lets the user manage contacts

Book = {}

def Add_contact() : 
    name = input("Name: ")
    Pnum = input("Phone number: ")
    if Book.get(name,None) == None : 
        print("Added", name)
    else : 
        print("Updated {name}'s number".format(name=name))        
    Book[name] = Pnum
    
    return None

def Delete_contact() : 
    name = input("Name to delete: ")
    if Book.get(name,None) == None :
        print('Not found')
    else :
        Book.pop(name)
        print('Deleted', name)
    
def Search_contact() : 
    name = input("Name to search: ")
    if Book.get(name,None) == None :
        print('Not found')
    else :  
        print("{name}'s number: {Pnum}".format(name=name,Pnum=Book[name]))

def Print_contacts() : 
    for name, Pnum in Book.items():
        print("{name}: {Pnum}".format(name=name,Pnum=Pnum))
        


while True :
    
    print("1. Add contact")
    print("2. Delete contact")
    print("3. Search contact")
    print("4. Print contacts")
    print("5. Exit")

    Choosing = input("Select a menu item: ")
    if Choosing == '1' : 
        Add_contact()
    if Choosing == '2' : 
        Delete_contact()
    if Choosing == '3' : 
        Search_contact()
    if Choosing == '4' : 
        Print_contacts()
    if Choosing == '5' : 
        print("Bye!")
        break



