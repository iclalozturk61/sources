//copilot
using System;
using System.Collections.Generic;

public enum Department
{
    HumanResources,
    InformationTechnology,
    Finance,
    Marketing,
    Sales
}

public abstract class Employee
{
    public int Id { get; }
    public string FullName { get; }
    public Department Department { get; }

    protected Employee(int id, string fullName, Department department)
    {
        if (string.IsNullOrWhiteSpace(fullName))
        {
            throw new ArgumentException("Çalışan adı boş bırakılamaz.", nameof(fullName));
        }

        Id = id;
        FullName = fullName;
        Department = department;
    }

    public abstract decimal CalculateSalary();

    public virtual void DisplayInfo()
    {
        Console.WriteLine($"ID: {Id}");
        Console.WriteLine($"Ad Soyad: {FullName}");
        Console.WriteLine($"Departman: {Department}");
        Console.WriteLine($"Çalışma şekli: {GetWorkType()}");
        Console.WriteLine($"Maaş: {CalculateSalary():C}");
    }

    protected abstract string GetWorkType();
}

public sealed class FullTimeEmployee : Employee
{
    public decimal MonthlySalary { get; }

    public FullTimeEmployee(
        int id,
        string fullName,
        Department department,
        decimal monthlySalary)
        : base(id, fullName, department)
    {
        if (monthlySalary < 0)
        {
            throw new ArgumentOutOfRangeException(nameof(monthlySalary));
        }

        MonthlySalary = monthlySalary;
    }

    public override decimal CalculateSalary()
    {
        return MonthlySalary;
    }

    protected override string GetWorkType()
    {
        return "Full time";
    }
}

public sealed class PartTimeEmployee : Employee
{
    public decimal HourlyRate { get; }
    public int HoursWorked { get; }

    public PartTimeEmployee(
        int id,
        string fullName,
        Department department,
        decimal hourlyRate,
        int hoursWorked)
        : base(id, fullName, department)
    {
        if (hourlyRate < 0)
        {
            throw new ArgumentOutOfRangeException(nameof(hourlyRate));
        }

        if (hoursWorked < 0)
        {
            throw new ArgumentOutOfRangeException(nameof(hoursWorked));
        }

        HourlyRate = hourlyRate;
        HoursWorked = hoursWorked;
    }

    public override decimal CalculateSalary()
    {
        return HourlyRate * HoursWorked;
    }

    protected override string GetWorkType()
    {
        return "Part time";
    }

    public override void DisplayInfo()
    {
        base.DisplayInfo();
        Console.WriteLine($"Saatlik ücret: {HourlyRate:C}");
        Console.WriteLine($"Çalışılan saat: {HoursWorked}");
    }
}

public static class Program
{
    public static void Main()
    {
        List<Employee> employees = new List<Employee>
        {
            new FullTimeEmployee(
                1,
                "Ayşe Yılmaz",
                Department.InformationTechnology,
                45000m),
            new PartTimeEmployee(
                2,
                "Mehmet Demir",
                Department.Marketing,
                250m,
                80),
            new FullTimeEmployee(
                3,
                "Zeynep Kaya",
                Department.Finance,
                40000m),
            new PartTimeEmployee(
                4,
                "Ali Çelik",
                Department.Sales,
                200m,
                60)
        };

        Console.WriteLine("ŞİRKET ÇALIŞANLARI");
        Console.WriteLine(new string('=', 35));

        foreach (Employee employee in employees)
        {
            employee.DisplayInfo();
            Console.WriteLine(new string('-', 35));
        }

        Console.WriteLine($"Toplam çalışan sayısı: {employees.Count}");
        Console.WriteLine(
            $"Toplam aylık maaş maliyeti: {CalculateTotalSalary(employees):C}");
    }

    private static decimal CalculateTotalSalary(List<Employee> employees)
    {
        decimal totalSalary = 0;

        foreach (Employee employee in employees)
        {
            totalSalary += employee.CalculateSalary();
        }

        return totalSalary;
    }
}