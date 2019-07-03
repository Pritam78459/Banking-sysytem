#Minor banking system
print('\t\t*** Welcome to minor banking system ***')
user_name = input('Enter user name = ')
print('Welcome Mr/Ms. ' + user_name + '.')
active = True
while active :
    print('------Main menu------ ')
    print('1. Create an account.')
    print('2. Show user details')
    print('3. Update user details')
    print('4. Cash withdrawl ')
    print('5. Cash deposit')
    print('6. Quit')
    choice = int(input('Enter your choice = '))
    if choice == 1:
        print('------Account Creation------')
        new_user_name = input('Enter your user name = ')
        acc_number = input('Create your account number = ')
        address = input('Enter your address = ')
        acc_balance = int(input('Enter your account balance = '))
        acc_type = input('Enter which type of account you want to make = ')
    elif choice == 2:
        print('------Account Details------')
        print(f'The user name is {new_user_name} .')
        print(f'The account no. is {acc_number}.')
        print(f'The address is {address}.')
        print(f'The account balance is {acc_balance}.')
        print(f'The account type is {acc_type}.')
    elif choice == 3:
        print('------Update account details------')
        new_user_name = input('Enter your user name = ')
        acc_number = input('Create your account number = ')
        address = input('Enter your address = ')
        acc_balance = int(input('Enter your account balance = '))
        acc_type = input('Enter which type of account you want to make = ')
        print('Your account is successfully updated.... ')
    elif choice == 4:
        print('------Cash Withdrawl------')
        print(f'The current balance on your account is {acc_balance}. ')
        withdraw_amount = int(input('How much would you like to withdraw? = '))
        current_balance = acc_balance - withdraw_amount
        print(f'Your account balance is {current_balance}.')
    elif choice == 5:
        print('------Cash deposit------')
        print(f'The current balance on your account is {acc_balance}. ')
        deposit_amount = int(input(f'How much would you like to deposit? = '))
        current_balance = acc_balance + deposit_amount
        print(f'Your account balance is {current_balance}.')
    elif choice == 6:
        active = False
        print('This session has ended.')