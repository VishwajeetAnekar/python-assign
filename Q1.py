class Customer:
    def __init__(self, account_number, name, balance=0.0):
        self.__account_number = account_number
        self.__name = name
        self.__balance = balance

    def add_funds(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Added {amount} to {self.__name}'s account. New balance: {self.__balance}")
        else:
            print("Amount should be greater than zero.")

    def deduct_funds(self, amount):
        if amount > self.__balance:
            print("Insufficient funds.")
        elif amount > 0:
            self.__balance -= amount
            print(f"Deducted {amount} from {self.__name}'s account. New balance: {self.__balance}")
        else:
            print("Amount should be greater than zero.")

    def get_account_details(self):
        return {
            "Account Number": self.__account_number,
            "Name": self.__name,
            "Balance": self.__balance
        }


class Branch:
    def __init__(self, branch_name):
        self.__branch_name = branch_name
        self.__customers = {}

    def add_customer(self, account_number, name, balance=0.0):
        if account_number not in self.__customers:
            customer = Customer(account_number, name, balance)
            self.__customers[account_number] = customer
            print(f"Customer {name} added with account number {account_number} to {self.__branch_name} branch.")
        else:
            print("Account number already exists in this branch.")

    def remove_customer(self, account_number):
        if account_number in self.__customers:
            del self.__customers[account_number]
            print(f"Customer with account number {account_number} removed from {self.__branch_name} branch.")
        else:
            print("Customer not found.")

    def perform_transaction(self, account_number, transaction_type, amount):
        customer = self.__customers.get(account_number)
        if customer:
            if transaction_type == "add":
                customer.add_funds(amount)
            elif transaction_type == "deduct":
                customer.deduct_funds(amount)
            else:
                print("Invalid transaction type.")
        else:
            print("Customer not found.")

    def list_customers(self):
        if self.__customers:
            print(f"Customers in {self.__branch_name} branch:")
            for customer in self.__customers.values():
                details = customer.get_account_details()
                print(f"Account Number: {details['Account Number']}, Name: {details['Name']}, Balance: {details['Balance']}")
        else:
            print("No customers in this branch.")

    def get_customers(self):
        return self.__customers


class Bank:
    def __init__(self, name):
        self.__name = name
        self.__branches = {}

    def add_branch(self, branch_name):
        if branch_name not in self.__branches:
            branch = Branch(branch_name)
            self.__branches[branch_name] = branch
            print(f"Branch {branch_name} added to {self.__name}.")
        else:
            print("Branch already exists.")

    def remove_branch(self, branch_name):
        if branch_name in self.__branches:
            del self.__branches[branch_name]
            print(f"Branch {branch_name} removed from {self.__name}.")
        else:
            print("Branch not found.")

    def get_branch(self, branch_name):
        return self.__branches.get(branch_name)

    def display_branches(self):
        if self.__branches:
            print("Branches in", self.__name)
            for branch_name in self.__branches:
                print(f"- {branch_name}")
        else:
            print("No branches available.")

    def unique_account_check(self, account_number):
        # Ensures unique account numbers across all branches
        for branch in self.__branches.values():
            if account_number in branch.get_customers():
                return False
        return True

    def menu(self):
        while True:
            print("\n--- Bank Management System ---")
            print("1. Add Branch")
            print("2. Remove Branch")
            print("3. Add Customer to Branch")
            print("4. Remove Customer from Branch")
            print("5. Perform Transaction")
            print("6. Display Branches")
            print("7. List Customers in a Branch")
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                branch_name = input("Enter branch name: ")
                self.add_branch(branch_name)

            elif choice == '2':
                branch_name = input("Enter branch name to remove: ")
                self.remove_branch(branch_name)

            elif choice == '3':
                branch_name = input("Enter branch name: ")
                branch = self.get_branch(branch_name)
                if branch:
                    account_number = int(input("Enter account number: "))
                    if self.unique_account_check(account_number):
                        name = input("Enter customer name: ")
                        balance = float(input("Enter initial balance: "))
                        branch.add_customer(account_number, name, balance)
                    else:
                        print("Account number already exists in another branch.")
                else:
                    print("Branch not found.")

            elif choice == '4':
                branch_name = input("Enter branch name: ")
                branch = self.get_branch(branch_name)
                if branch:
                    account_number = int(input("Enter account number to remove: "))
                    branch.remove_customer(account_number)
                else:
                    print("Branch not found.")

            elif choice == '5':
                branch_name = input("Enter branch name: ")
                branch = self.get_branch(branch_name)
                if branch:
                    account_number = int(input("Enter account number: "))
                    transaction_type = input("Enter transaction type (add/deduct): ")
                    amount = float(input("Enter amount: "))
                    branch.perform_transaction(account_number, transaction_type, amount)
                else:
                    print("Branch not found.")

            elif choice == '6':
                self.display_branches()

            elif choice == '7':
                branch_name = input("Enter branch name: ")
                branch = self.get_branch(branch_name)
                if branch:
                    branch.list_customers()
                else:
                    print("Branch not found.")

            elif choice == '8':
                print("Exiting the system.")
                break

            else:
                print("Invalid choice. Please try again.")



if __name__ == "__main__":
    bank = Bank("VBI Bank")
    bank.menu()
