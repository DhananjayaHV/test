'''ATM'''

people = {"123456": {'name': 'Marie', 'age': '22', 'Gender': 'Female', 'password': '2424', 'Balance': 2000}}


def account():

    people = {"123456": {'name': 'Marie', 'age': '22', 'Gender': 'Female', 'password': '2424', 'Balance': 2000}}

    for i in range(3):
        ac_nur = input("enter any 6 digits to create new account : ")
        if len(ac_nur)==6:
            if ac_nur not in people.keys():
                people[ac_nur] = {}
                people[ac_nur]['name'] = input("enter your name : ")
                people[ac_nur]['age'] = int(input("enter the age : "))
                people[ac_nur]['Gender'] = input("enter the Gender : ")
                people[ac_nur]['password']=input("Enter 4 digit pin : ")
                people[ac_nur]['Balance'] = int(input("Enter Initial amount to deposit : "))
                print(people)
                return people

            else:
                print("Accounr number already exists!!!")
            return people
        else:
            print("Please enter vallid account number..Try again")
        i+=1

def debit(account_dict):
    list1 = []
    for x, y in account_dict.items():
        list1.append(int(x))

    for i in range(3):
        acc_numr=int(input("Please enter again your 6 digit account number : "))
        if acc_numr in list1:
            password=int(input("Please enter your 4 digits PIN : "))
            if password==int(account_dict[f'{acc_numr}']['password']):
                print("Your current balance is : ", account_dict[f'{acc_numr}']['Balance'])
                amonut_debit = int(input("Enter amount to debit : "))
                if amonut_debit <=account_dict[f'{acc_numr}']['Balance']:
                    account_dict[f'{acc_numr}']['Balance']=account_dict[f'{acc_numr}']['Balance']-amonut_debit
                    print("Balance amount",account_dict[f'{acc_numr}']['Balance'])
                    print("Your transaction successfully completed.")
                    break
                else:
                    print("Sorry!! Your transaction has declined due to insufficient balance")
        else:
            print("Please enter valid account number.")
user_type=input("New user>>'y' or 'n' : ")
if user_type=='y':
    a = account()
    print("Prcocessing.........")
    print("Prcocessing.........")
    print("Prcocessing.........")
    print("Prcocessing.........")
    print("Prcocessing.........")
    print("Prcocessing.........")
    print("Prcocessing.........")
    print("Congratulations your New account created.")
    debit(a)
elif user_type=='n':
    debit(people)





        # else:
        #     print("please enter correct Account number.")
        # i+=1
