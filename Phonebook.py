#py3DNS
#validate_email
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from validate_email import validate_email

file_name='phonebook.txt'
file1=open(file_name,'a+')
file1.close

def show_main_menu():
    print('1,2,3,4')
    choice=input('Enter your choice: ')
    if(choice=='1'):
        file1=open(file_name,'r+')
        file_contents=file1.read()
        if(len(file_contents)==0):
            print('Phone Book is empty')
        else:
            print (file_contents)
        file1.close
        ent = input('Press Enter to continue ...')
    elif(choice=='2'):
        enter_contact_record()
        ent=input('Press Enter to continue ...')
    elif(choice=='3'):
        search_contact_record()
        ent=input('Press Enter to continue ...')
    elif(choice=='4'):
        print('Thank you')
        return
    else:
        print('Wrong choice, Please Enter [1 to 4]')
        ent=input('Press Enter to continue ...')
    show_main_menu()

def search_contact_record():
    search_name = input('Enter First name for Searching contact record: ')
    if(not all(x.isalpha or x=='' for x in search_name)):
        return

    search_name=search_name.title()
    file1=open(file_name,'r+')
    file_contents=file1.readlines()

    found=False
    for line in file_contents:
        if(search_name in line):
            print('Your Required Contact Record is:',end=' ')
            print (line)
            found=True
            break
    if(found == False):
        print('No contact Record in Phone Book with name = ' + search_name )

def enter_contact_record():
    first = input('Enter First Name: [name]')
    if(not all(x.isalpha)or(x==str()for x in first)):
        return
    first = first.title()
    last = input('Enter Last Name: [surname]')
    if(not all(x.isalpha))or(x==str()for x in last):
        return
    last = last.title()
    phone = input('Enter Phone number: [000-000-0000]')
    if(len(phone)==12)and(phone[3]=='-')and(phone[7]=='-')and(phone[:3].isdigit())and(phone[4:7].isdigit())and(phone[8:].isdigit()):
        print('Valid Phone Number')

        ch_number = phonenumbers.parse(phone, 'CH')
        print(geocoder.description_for_number(ch_number, 'en'))

        service_provider = phonenumbers.parse(phone, 'RO')
        print(carrier.name_for_number(service_provider, 'en'))
    else:
        return
    email=input('Enter E-mail: [www.me@email.com]')
    if(validate_email(email, verify=True, smtp_timeout=60) is None):
        return
    contact = ('['+first+' '+last+', '+phone+', '+email+']')
    file1 = open(file_name,'a')
    file1.write(contact)
    file1.close()
    print( 'This contact ' + contact + 'has been added successfully!')

show_main_menu()