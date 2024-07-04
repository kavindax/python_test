# Problem 5 : Bank Account Management

def get_accounts_dict(filename: str) -> dict[str, float]:
    #Reads account information from a file and returns it as a dictionary.

    accounts = {}
    with open(filename, 'r') as file:
        for line in file:
            account_number, balance_str = line.strip().split(',')
            accounts[account_number] = float(balance_str)
    return accounts

def write_accounts_dict(accounts: dict[str, float], filename: str):
    #Writes account information from a dictionary to a file.

    with open(filename, 'w') as file:
        for account_number, balance in accounts.items():
            file.write(f"{account_number},{balance}\n")

def get_balance(account_number: str, filename: str) -> float:
    #Get the current balance of the account.

    accounts = get_accounts_dict(filename)
    return accounts.get(account_number, 0.0)

def update_account(account_number: str, balance: float, filename: str):
    #Update the balance of an account in the file.

    accounts = get_accounts_dict(filename)
    if account_number in accounts:
        accounts[account_number] = balance
        write_accounts_dict(accounts, filename)
    else:
        print(f"Account {account_number} does not exist.")

def deposit(account_number: str, amount: float, filename: str):
   # Deposit an amount into the account.

    current_balance = get_balance(account_number, filename)
    new_balance = current_balance + amount
    update_account(account_number, new_balance, filename)

def withdraw(account_number: str, amount: float, filename: str):
    #Withdraw an amount from the account. Ensure the balance does not go negative.

    current_balance = get_balance(account_number, filename)
    if current_balance >= amount:
        new_balance = current_balance - amount
        update_account(account_number, new_balance, filename)
    else:
        print("Insufficient funds")



# Testing the functions

# Create an initial accounts.txt file
with open('accounts.txt', 'w') as file:
    file.write("12345,1000.0\n")
    file.write("67890,1500.0\n")

# Test get_balance
print(get_balance("12345", "accounts.txt"))  # Output: 1000.0

# Test deposit
deposit("12345", 500.0, "accounts.txt")
print(get_balance("12345", "accounts.txt"))  # Output: 1500.0

# Test withdraw
withdraw("12345", 200.0, "accounts.txt")
print(get_balance("12345", "accounts.txt"))  # Output: 1300.0

# Test insufficient funds
withdraw("12345", 2000.0, "accounts.txt")  # Output: Insufficient funds
print(get_balance("12345", "accounts.txt"))  # Output: 1300.0

# Test non-existent account
print(get_balance("99999", "accounts.txt"))  # Output: 0.0
deposit("99999", 1000.0, "accounts.txt")  # Output: Account 99999 does not exist.


