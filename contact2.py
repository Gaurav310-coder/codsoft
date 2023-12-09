try :
    import pandas as pd
except :
	print("Please include neceesarry libarires :  pandas , openpyxl")

class Contact:
    name = []
    phone = []
    email = []
    address = []

    task = {
        "Name": [],
        'Phone': [],
        "Email": [],
        "Address": []
    }

    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.task["Name"].append(name)
        self.task["Phone"].append(phone)
        self.task["Email"].append(email)
        self.task["Address"].append(address)
        self.df = pd.DataFrame(self.task)

    def add(self, Name, Phone, Email, Address):
        self.task["Name"].append(Name)
        self.task["Phone"].append(Phone)
        self.task["Email"].append(Email)
        self.task["Address"].append(Address)
        self.df = pd.DataFrame(self.task)

    def search(self):
        try:
        	Name = input("Enter Contact Name  : ")
        	index = self.task["Name"].index(Name)
        except:
        	print("Contact Not Found ")
        return self.df.loc[index]
       

    def delete(self, Name):
        index = self.task["Name"].index(Name)
        self.df = self.df.drop(index)
        self.df = self.df.reset_index(drop=True)
        self.task["Name"].pop(index)
        self.task["Phone"].pop(index)
        self.task["Email"].pop(index)
        self.task["Address"].pop(index)

    def edit(self, Name, NewPhone, NewEmail, NewAddress):
        index = self.task["Name"].index(Name)
        self.df.at[index, "Phone"] = NewPhone
        self.df.at[index, "Email"] = NewEmail
        self.df.at[index, "Address"] = NewAddress
        self.task["Phone"][index] = NewPhone
        self.task["Email"][index] = NewEmail
        self.task["Address"][index] = NewAddress
        
        
    def save(self):
    	if  not ((self.df).empty):
    		df = pd.DataFrame(self.df)
    		excel_file_path = 'contact.xlsx'
    		df.to_excel(excel_file_path, index=False)



    	else :
    		print("No Contacts !!")

    
    def show(self):
    	try:
    	    excel_file_path = 'contact.xlsx'
    	    df = pd.read_excel(excel_file_path)
    	    print(df)
    	except:
    		print("Please Save Data First To see Conatcts .....")
    	
con = Contact(name="Gaurav", phone="755872482", email="gaurav@example.com", address="IND")
def Add():
	print("===========Enter New Contact =============")
	nm = input("Enter Contact Name : ")
	phn = input("Enter Contact Phone Number : ")
	eml = input("Enter Contact Email : ")
	adres = input("Enter Contact Address : ")
	con.add(Name=nm, Phone=phn, Email=eml, Address=adres)

def Edit():
	print("===========Enter New Contact =============")
	nm = input("Enter Contact Name : ")
	newPhone = input("Enter Contact Phone Number : ")
	newEmail = input("Enter Contact Email : ")
	newAdd = input("Enter Contact Address : ")	
	con.edit(Name=nm, NewPhone=newPhone, NewEmail=newEmail, NewAddress=newAdd)

def dlt():
	name = input("Enter Contact Name You Want to Delete : ")
	try:
		con.delete(Name=name)
		print("Contact Deleted Successfully !!!!!")
	except:
		print("No Such Contact!!")
	

print("___________________CONTACT BOOK__________________")

def intro():
	print('''
--------------------------------------------------------
Show Conatact List : 1
Add Contact : 2
Edit Conatct : 3
Delete Contact : 4
Save Contact Book :5
Menu : 6
Search Conatct : 7
Exit Conatct Book : quit or q
---------------------------------------------------------------
''')
intro()

while True :
	choise = input("Enter Your Choise : ")
	if choise == 'quit ' or choise =='q':
		print('''
=========Thanks For Using Contact Book ==========
		''')
		break
	try :
		choise = int(choise)
	except :
		print("Enter a valid Chosie  ")
	if choise  == 1:
		con.show()
	elif choise == 2:
		Add()
	elif choise ==3:
		Edit()
	elif choise ==4:
		dlt()
	elif choise ==5:
		con.save()
		print("Contact Saved Successfully !!!! ")
	elif choise == 6:
		intro()
	elif choise == 7:
		print(con.search())
	else:
		print("Invalid Input !!!!")