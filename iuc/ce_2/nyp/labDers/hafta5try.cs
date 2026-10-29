using System.ComponentModel.DataAnnotations;
using System.Reflection.PortableExecutable;

enum Department
{
    Software, 
    HumanResources,
    Finance,
    Sales
}

abstract class Employee
{
    public string name {get; set;}
    public Department department {get; set;}

    public Employee (string  name, Department department)
    {
        if (string.IsNullOrWhiteSpace(name))
            throw new ArgumentException("isim değeri boş bırakılamaz");
        
        name = name;
        department = department;
    }

    public abstract int CalculateSalary(){} 

    public virtual void DisplayInfo()
    {
        Console.WriteLine($"{name}, {department} alanında çalışmaktadır.");
    }
}

class FullTimeEmployee : Employee
{
    public int mounthlySalary{get; set;}

    public FullTimeEmployee(string name, Department department, int salary) : base(name, department)
    {
        if(salary <=0)
            throw new ArgumentException("aylık maaş değeri 0 dan büyük olmalıdır");

        mounthlySalary = salary;
    }

    public override int CalculateSalary()
    {
        return mounthlySalary;
    }

    public override void DisplayInfo()
    {
        Console.WriteLine($"{name}, {department} alanındda {mounthlySalary} maaşına çalışmaktadır.");
    }
}

class PartTimeEmployee : Employee
{
    public int hour {get;}
    public int hourlyRate { get;}

    public PartTimeEmployee(string n, Department d, int hourlyRate, int hour) : base(name, department)
    {
        if (hourlyRate <= 0)
            throw new ArgumentException("saatlik ücret 0'dan küçük olamaz.");

        if(hour < 0)
        {
            throw new ArgumentException("saatlik ücret 0'dan büyük olmalıdır.");
        }
    }

    public override int CalculateSalary()
    {
        int totalSalary = hour*hourlyRate;
        return totalSalary;
    }

    public override void DisplayInfo()
    {
        Console.WriteLine($"{name}, {department}, alanında saat başı {hourlyRate} ücretine, {hour} saat çalışmaktadır.");
    }
}

class Program
{
    static void Main()
    {
        List<Employee> employees = new List<Employee>
        {
            new emp1 ("ahmet", Software, 50000),
            new emp2 ("ayşe", Department.HumanResources, 300, 80),
        };

        foreach(Employee employee in employees)
        {
            employee.DisplayInfo();
            employee.CalculateSalary();
        }
    }
}