contacts = []
while True:
    choice = input("""What would you like to do? (Type the number of the action, then the contact you want to use!)
    1 Enter a contact,
    2 Check all contacts,
    3 Stop this program
    > """)

    if choice == '1':
        person_name = input('Enter a Name...')
        person_surname = input('Enter a Surname...')
        person_phone = input('Enter a Phone Number...')
        person_email = input('Enter an Email...')
        
        print('Done! Check your contacts by typing 2! \n')

        contact_person = {
   
            'Name' : person_name,
            'Surname' : person_surname,
            'Phone' : person_phone,
            'Email' : person_email
        }

        contacts.append(contact_person)

    elif choice == '2':
        #for i in contact_person:
            #print(i + ': ' + contact_person[i])
        for i in contacts:    
            print('---Contact---'),
            print(contact_person['Name'] + ' ' + contact_person['Surname']),
            print('Phone Number: ' + contact_person['Phone']),
            print('Email: ' + contact_person['Email'])

    elif choice == '3':
        break

    else:
        print('Wrong Choice! Check what you have typed! (' + choice + ')\n' )



#UZDEVUMS(IZPILDĪTS):
#izveido izvēlni lai lietotājs var izvēlēties ko darīs:
#1. Ievadīt jaunu kontaktu
#2. Izvadīt kontaktus
#3. Pārtraukt darbības un iziet no programmas

#UZDEVUMS:
#1Formatēt sarakstu
#---CONTACT---
#Vārds Uzvārds
#Phone: Numurs
#Email: pasts