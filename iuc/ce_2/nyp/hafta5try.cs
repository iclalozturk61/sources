using System.IO;
enum Department
{
    Software, 
    HumanResources,
    Finance,
    Sales
}

abstract class Employee
{
    public string Name {get; set;}
    public Department Department {get; set;}

    public Employee (string  name, Department department)
    {
        if (string.IsNullOrWhiteSpace(name))
            throw new ArgumentException("isim değeri boş bırakılamaz");
        
        Name = name;
        Department = department;
    }

    public abstract int CalculateSalary();

    public virtual void DisplayInfo()
    {
        Console.WriteLine($"{Name}, {Department} alanında çalışmaktadır.");
    }
}

class FullTimeEmployee : Employee
{
    public int MounthlySalary{get; set;}

    public FullTimeEmployee(string name, Department department, int salary) : base(name, department)
    {
        if(salary <=0)
            throw new ArgumentException("aylık maaş değeri 0 dan büyük olmalıdır");

        MounthlySalary = salary;
    }

    public override int CalculateSalary()
    {
        return MounthlySalary;
    }

    public override void DisplayInfo()
    {
        Console.WriteLine($"{Name}, {Department} alanındda {MounthlySalary} maaşına çalışmaktadır.");
    }
}

class PartTimeEmployee : Employee
{
    public int Hour {get;}
    public int HourlyRate { get;}

    public PartTimeEmployee(string name, Department department, int hourlyRate, int hour) : base(name, department)
    {
        if (hourlyRate <= 0)
            throw new ArgumentException("saatlik ücret 0'dan küçük olamaz.");

        if(hour < 0)
        {
            throw new ArgumentException("saatlik ücret 0'dan büyük olmalıdır.");
        }

        HourlyRate = hourlyRate;
        Hour = hour;
    }

    public override int CalculateSalary()
    {
        int totalSalary = Hour*HourlyRate;
        return totalSalary;
    }

    public override void DisplayInfo()
    {
        Console.WriteLine($"{Name}, {Department}, alanında saat başı {HourlyRate} ücretine, {Hour} saat çalışmaktadır.");
    }
}

class Program
{
    static void Main()
    {
        List<Employee> employees = new List<Employee>
        {
            new FullTimeEmployee("ahmet", Department.Software, 50000),
            new PartTimeEmployee("ayşe", Department.HumanResources, 300, 80),
        };

        string report = "";

        foreach(Employee employee in employees)
        {
            employee.DisplayInfo();
            Console.WriteLine(employee.CalculateSalary());
            report += $"{employee.Name} - {employee.Department} - {employee.CalculateSalary()} TL" + Environment.NewLine;
        }
        File.WriteAllText("salary_report.txt", report);


        string fileContent = File.ReadAllText("salary_report.txt");
        Console.WriteLine(fileContent);
        Console.WriteLine(Path.GetFullPath("salary_report.txt"));
    }
}