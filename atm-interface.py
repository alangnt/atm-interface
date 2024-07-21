class BankOperators:
    def __init__(self):
        self.balance = 0
        self.accounts = {}

    # Welcome Interface
    def welcome_interface(self):
        print('=================================')
        print('  Welcome to Golden Banking Co.')
        print('=================================')

        while True:
            # Different Choices
            print('\n1. Login')
            print('\n2. Sign Up')
            print('\n3. Exit')

            # Redirect User to appropriate interface based on their choice
            user_choice = int(input('\nEnter your choice: '))

            if user_choice == 1:
                self.sign_in_interface()
            elif user_choice == 2:
                self.sign_up_interface()
            elif user_choice == 3:
                quit()
            else:
                print('\nInvalid choice. Please try again.')

    # Sign In Interface
    def sign_in_interface(self):
        while True:
            user_password = int(input('Enter your 4-digit password: '))

            if user_password < 1000 or user_password > 9999:
                print('\nInvalid password. Please try again.')
            else:
                if user_password not in self.accounts:
                    print('\nAccount not found. Please try again.')
                else:
                    while True:
                        user_key = int(input('\nAccount found. Please enter your key: '))
                        if user_key != self.accounts[user_password][1]:
                            print('\nInvalid key. Please try again.')
                        else:
                            print('\nWelcome back to Golden Banking Co.')
                            self.atm_interface()
                            return

    # Sign Up Interface
    def sign_up_interface(self):
        while True:
            user_createpassword = int(input('Create a 4-digit password: '))

            if user_createpassword < 1000 or user_createpassword > 9999:
                print('\nInvalid password. Please try again.')
            else:
                while True:
                    user_confirmpassword = int(input('Confirm your password: '))

                    if user_confirmpassword != user_createpassword:
                        print('\nPasswords do not match. Please try again.')
                    else:
                        while True:
                            user_createkey = int(input('Enter a 2-digit Key to secure your Account: '))

                            if user_createkey < 10 or user_createkey > 99:
                                print('\nInvalid key. Please try again.')
                            else:
                                self.accounts[user_createpassword] = (user_createpassword, user_createkey)
                                print('\nAccount created successfully.')
                                self.atm_interface()
                                return

    # ATM Interface
    def atm_interface(self):
        while True:
            print('\nATM Menu:')
            print('1. Deposit')
            print('2. Withdraw')
            print('3. Check Balance')
            print('4. Change Password')
            print('5. Back')
            print('6. Exit')

            user_choice = int(input('\nEnter your choice: '))

            if user_choice == 1:
                self.deposit()
            elif user_choice == 2:
                self.withdraw()
            elif user_choice == 3:
                self.check_balance()
            elif user_choice == 4:
                self.change_password()
            elif user_choice == 5:
                self.welcome_interface()
                return
            elif user_choice == 6:
                quit()
            else:
                print('\nInvalid choice. Please try again.')

    # Deposit Method
    def deposit(self):
        user_deposit = int(input('Enter the amount to deposit: '))
        self.balance += user_deposit
        print(f'\nDeposit successful. Your new balance is: {self.balance}')

    # Withdraw Method
    def withdraw(self):
        user_withdraw = int(input('Enter the amount to withdraw: '))
        if user_withdraw <= self.balance:
            self.balance -= user_withdraw
            print(f'\nWithdrawal successful. Your new balance is: {self.balance}')
        else:
            print('\nInsufficient balance.')

    # Check Balance Method
    def check_balance(self):
        print(f'\nYour current balance is: {self.balance}')

    # Change Password Method
    def change_password(self):
        while True:
            user_oldpassword = int(input('Enter your old password: '))
            if user_oldpassword in self.accounts:
                while True:
                    user_newpassword = int(input('Enter your new password: '))
                    if user_newpassword < 1000 or user_newpassword > 9999:
                        print('\nInvalid password. Please try again.')
                    else:
                        self.accounts[user_newpassword] = (user_newpassword, self.accounts.pop(user_oldpassword)[1])
                        print('\nPassword changed successfully.')
                        return
            else:
                print('\nOld password is incorrect. Please try again.')

if __name__ == "__main__":
    bank = BankOperators()
    bank.welcome_interface()