#Name: Taylor Welton
#Assignemt: Lab 6
#Description: A Functioning ATM that the user can use to check their balance, make deposits, and withdrawls. Also keeps track of the number of transactions until the User exits the program.


class BankAccount:
    #constructor
    def __init__(self, bal):
        #keeps track of balance
        self.__balance = bal
        #keeps track of transactions
        self.__transCount = 0


    #deposit method
    def deposit(self, amount):
        self.__balance = self.__balance + amount

        #+1 to number of transactions
        self.__transCount = self.__transCount + 1

    #withdrawl method
    def withdrawal(self, amount):

        #If/else statement to make sure amount is divisible by 10
        if((amount % 10) == 0):
            #if/else statement to make sure withdrawl amount < balance
            if (self.__balance >= amount):
                self.__balance = self.__balance - amount

                #+1 to number of transactions
                self.__transCount = self.__transCount + 1

            else:
                print("ERROR: Insufficient Funds")
        else:
            print("ERROR: Withdrawl Amount Must be in Denominations of $10")

    #balance inquiry method
    def getBalance(self):
        #+1 to number of transactions
        self.__transCount = self.__transCount + 1

        return self.__balance

    #tracking # of transactions method
    def numofTrans(self):
        return self.__transCount


#Header/Title
print()
print("~ Welcome to The National Bank of LTU ATM ~")


#Menu/User Selection
def menu() :
    print()
    print("1. Balance Inquiry")
    print("2. Make a Deposit")
    print("3. Make a Withdrawal")
    print("4. Display Number of Transactions")
    print("5. Exit")
    print()
    choice = int(input ("Select an Option ==> "))
    return choice


#Main Program
def main() :
    #initializing variable
    initialBalance = 1000.0

    #create an instance of the BankAccount class
    savings = BankAccount(initialBalance)

    choice = menu()
    while choice != "5":
        
        if (choice == 1) :
            #See account balance
            print("Account Balance: $",format(savings.getBalance(),',.2f'),sep="")

        elif (choice == 2) :
            #make a deposit"
            depAmount = float(input("Deposit Amount: $"))
            savings.deposit(depAmount)

        elif (choice == 3) :
            #make a withdrawl
            withdrawlAmount = float(input("Withdrawal Amount: $"))
            savings.withdrawal(withdrawlAmount)
            
        elif (choice == 4) :
            #see total number of transactions
            print("Transactions Completed:",savings.numofTrans())

        elif (choice == 5) :
            #Exit program
            EndProgram()

        else:
            print("Please Select Another Option.")
    
        print()
        choice = menu()


#End Program Function
def EndProgram() :
    exit()
    
#calling the main function
main()