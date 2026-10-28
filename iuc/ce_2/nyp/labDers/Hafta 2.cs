/*

İstediğimiz yapı:

BankAccount

accountNumber
owner
balance

Deposit()
Withdraw()
ShowInfo()

	Ancak bazı kurallarımız olsun:
	- accountNumber oluşturulduktan sonra dışarıdan değiştirilemesin.
	- balance dışarıdan doğrudan değiştirilemesin.
	    - Para yatırma ve çekme methodlar üzerinden yapılsın.
	- Owner property ile yönetilsin.

*/

using System;

class BankAccount
{
    private string accountNumber;
    private string owner;
    private decimal balance;

    public BankAccount( 
        string accountNumber,
        string owner,
        decimal initialBalance)
    {
        this.accountNumber = accountNumber;
        this.owner = owner;

        if (initialBalance >= 0)
        {
            balance = initialBalance;
        }
        else
        {
            balance = 0;
        }
    }

    public string AccountNumber
    {
        get
        {
            return accountNumber;
        }
    }

    public string Owner
    {
        get
        {
            return owner;
        }

        set
        {
            if (!string.IsNullOrWhiteSpace(value))
            {
                owner = value;
            }
        }
    }

    public decimal Balance
    {
        get
        {
            return balance;
        }
    }

    public void Deposit(decimal amount)
    {
        if (amount > 0)
        {
            balance += amount;
        }
        else
        {
            throw new ArgumentException("Amount must be greater than zero.");
        }
    }

    public void Withdraw(decimal amount) //çekme
    {
        if (amount <= 0)
        {
            throw new ArgumentException("Amount must be greater than zero.");    
        }
        else if (amount > balance)
        {
            Console.WriteLine("Insufficient balance.");
        }
        else
        {
            balance -= amount;
        }
    }

    public void ShowInfo()
    {
        Console.WriteLine($"Account Number: {accountNumber}");
        Console.WriteLine($"Owner: {owner}");
        Console.WriteLine($"Balance: {balance} TL");
    }
}


public static class Program
{
    public static void Main()
    {
        BankAccount account1 =
            new BankAccount("TR1001", "Ahmet Yılmaz", 400);

        account1.ShowInfo();

        account1.Deposit(0);
        account1.Withdraw(1000);

        Console.WriteLine();

        account1.ShowInfo();

	}
}
