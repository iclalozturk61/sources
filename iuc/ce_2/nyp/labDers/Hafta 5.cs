using System;
using System.Collections.Generic;
using System.IO;



// ENUM

// Çalışanın departmanı sadece burada tanımlanan
// değerlerden biri olabilir.
enum Department
{
    Software,
    HumanResources,
    Finance,
    Sales
}



// BASE CLASS


// FullTimeEmployee ve PartTimeEmployee sınıflarında
// ortak olan özellikleri Employee sınıfında topluyoruz.
class Employee
{
    // Dışarıdan okunabilir ve değiştirilebilir property.
    public string Name { get; set; }

    // Department bir string değil, oluşturduğumuz enum türündedir.
    public Department Department { get; set; }


    // Constructor
    // Employee oluşturulurken isim ve departman verilmesini istiyoruz.
    public Employee(string name, Department department)
    {
        // İsim boş olamaz.
        if (string.IsNullOrWhiteSpace(name))
        {
            // Geçersiz veri geldiğinde exception oluşturuyoruz.
            throw new ArgumentException(
                "Employee name cannot be empty."
            );
        }

        Name = name;
        Department = department;
    }


    // Bu method alt sınıflarda değiştirileceği için virtual.
    public virtual decimal CalculateSalary()
    {
        return 0;
    }


    // Çalışan bilgilerini gösteren method.
    public virtual void DisplayInfo()
    {
        Console.WriteLine($"Name: {Name}");
        Console.WriteLine($"Department: {Department}");
    }
}



// FULL TIME EMPLOYEE


// FullTimeEmployee bir Employee'dir. (IS-A)

class FullTimeEmployee : Employee
{
    // private field
    private decimal monthlySalary;


    // Property üzerinden maaşa kontrollü erişim sağlıyoruz.
    public decimal MonthlySalary
    {
        get
        {
            return monthlySalary;
        }

        set
        {
            // Maaş 0 veya negatif olamaz.
            if (value <= 0)
            {
                throw new ArgumentException(
                    "Monthly salary must be greater than zero."
                );
            }

            monthlySalary = value;
        }
    }


    // Constructor
    public FullTimeEmployee(
        string name,
        Department department,
        decimal monthlySalary
    )
        // Base class constructor'ına name ve department gönderiyoruz.
        : base(name, department)
    {
        // Property üzerinden atama yaptığımız için
        // yukarıdaki kontrol burada da çalışacaktır.
        MonthlySalary = monthlySalary;
    }


    // Employee içerisindeki CalculateSalary methodunu değiştiriyoruz.
    public override decimal CalculateSalary()
    {
        return MonthlySalary;
    }


    public override void DisplayInfo()
    {
        Console.WriteLine("FULL TIME EMPLOYEE");

        // Employee sınıfındaki DisplayInfo methodunu çağırıyoruz.
        base.DisplayInfo();

        Console.WriteLine(
            $"Monthly Salary: {MonthlySalary} TL"
        );
    }
}



// PART TIME EMPLOYEE


class PartTimeEmployee : Employee
{
    public decimal HourlyRate { get; private set; }

    public int WorkedHours { get; private set; }


    public PartTimeEmployee(
        string name,
        Department department,
        decimal hourlyRate,
        int workedHours
    )
        : base(name, department)
    {
        // Saatlik ücret geçerli mi?
        if (hourlyRate <= 0)
        {
            throw new ArgumentException(
                "Hourly rate must be greater than zero."
            );
        }

        // Çalışma saati negatif olamaz.
        if (workedHours < 0)
        {
            throw new ArgumentException(
                "Worked hours cannot be negative."
            );
        }

        HourlyRate = hourlyRate;
        WorkedHours = workedHours;
    }


    // Part-time çalışan için maaş farklı hesaplanıyor.
    public override decimal CalculateSalary()
    {
        return HourlyRate * WorkedHours;
    }


    public override void DisplayInfo()
    {
        Console.WriteLine("PART TIME EMPLOYEE");

        base.DisplayInfo();

        Console.WriteLine(
            $"Hourly Rate: {HourlyRate} TL"
        );

        Console.WriteLine(
            $"Worked Hours: {WorkedHours}"
        );
    }
}



// PROGRAM


class Program
{
    static void Main()
    {
        // Bütün çalışanları Employee tipindeki listede tutuyoruz.
        
        List<Employee> employees =
            new List<Employee>();


        try
        {
            
            // OBJECT CREATION
            

            // Tam zamanlı çalışan oluşturuyoruz.
            FullTimeEmployee employee1 =
                new FullTimeEmployee(
                    "Ahmet",
                    Department.Software,
                    50000
                );


            // Yarı zamanlı çalışan oluşturuyoruz.
            PartTimeEmployee employee2 =
                new PartTimeEmployee(
                    "Ayşe",
                    Department.HumanResources,
                    300,
                    80
                );


            // Farklı class'lardan olmalarına rağmen
            // ikisi de Employee olduğu için aynı listeye eklenebilir.
            employees.Add(employee1);
            employees.Add(employee2);


            Console.WriteLine(
                "===== EMPLOYEE INFORMATION ====="
            );


            // Dosyaya yazacağımız metni hazırlıyoruz.
            string report = "";


            
            // POLYMORPHISM
            

            foreach (Employee employee in employees)
            {
                Console.WriteLine("----------------------");

                // employee değişkeninin tipi Employee.
                //
                // Ancak gerçek nesne FullTimeEmployee ise
                // FullTimeEmployee.DisplayInfo()
                //
                // PartTimeEmployee ise
                // PartTimeEmployee.DisplayInfo()
                //
                // çalışacaktır.
                employee.DisplayInfo();


                // Aynı şey CalculateSalary için de geçerli.
                decimal salary =
                    employee.CalculateSalary();


                Console.WriteLine(
                    $"Calculated Salary: {salary} TL"
                );


                // Dosyaya yazılacak raporu oluşturuyoruz.
                report +=
                    $"{employee.Name} - " +
                    $"{employee.Department} - " +
                    $"{salary} TL" +
                    Environment.NewLine;
            }


            
            // FILE WRITE
           

            // Oluşturduğumuz raporu dosyaya yazıyoruz.
            //
            // Dosya yoksa oluşturulur.
            // Dosya varsa eski içerik değiştirilir.
            File.WriteAllText(
                "salary_report.txt",
                report
            );


            Console.WriteLine();
            Console.WriteLine(
                "Salary report was saved to file."
            );


            
            // FILE READ
           

            Console.WriteLine();
            Console.WriteLine(
                "===== SALARY REPORT FROM FILE ====="
            );


            // Dosyanın tamamını okuyup string değişkenine alıyoruz.
            string fileContent =
                File.ReadAllText("salary_report.txt");


            // Dosyadan okuduğumuz içeriği ekrana yazıyoruz.
            Console.WriteLine(fileContent);
        }


        
        // EXCEPTION HANDLING
       

        // Eğer hatalı isim, maaş, saatlik ücret veya
        // çalışma saati verilirse ArgumentException yakalanır.
        catch (ArgumentException exception)
        {
            Console.WriteLine();
            Console.WriteLine("DATA ERROR");

            Console.WriteLine(
                exception.Message
            );
        }


        // Dosyaya erişirken problem çıkarsa
        // IOException yakalanabilir.
        catch (IOException exception)
        {
            Console.WriteLine();
            Console.WriteLine("FILE ERROR");

            Console.WriteLine(
                exception.Message
            );
        }


        // Beklemediğimiz başka bir hata oluşursa
        // genel Exception tarafından yakalanır.
        catch (Exception exception)
        {
            Console.WriteLine();
            Console.WriteLine("UNEXPECTED ERROR");

            Console.WriteLine(
                exception.Message
            );
        }


        // Hata olsa da olmasa da çalışır.
        finally
        {
            Console.WriteLine();
            Console.WriteLine(
                "Program finished."
            );
        }
    }
}