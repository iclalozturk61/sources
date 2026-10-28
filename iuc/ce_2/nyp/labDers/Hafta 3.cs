using System;
using System.Collections.Generic;

// Base Class
public class Person
{
    // Protected field
    protected int age;

    // Auto-implemented property
    public string Name { get; set; }

    // Property
    public int Age //get methodu gibi
    {
        get
        {
            return age;
        }
        set
        {
            if (value < 0)
                value = 0;

            age = value;
        }
    }

    // Constructor
    public Person(string name, int age)
    {
        Name = string.IsNullOrWhiteSpace(name) ? "Unknown" : name;
        Age = age;
    }

    // Virtual methods
    public virtual void ShowInfo()
    {
        Console.WriteLine($"[Person] Name: {Name}, Age: {Age}");
    }

    public virtual void Work()
    {
        Console.WriteLine($"{Name} is doing generic tasks at the university.");
    }
}


// Derived Class 1: Student
public class Student : Person
{
    public string StudentID { get; }
    public double GPA { get; set; }

    // Student Constructor
    public Student(string name, int age, string studentId, double gpa)
        : base(name, age)
    {
        StudentID = string.IsNullOrWhiteSpace(studentId) ? "S-000" : studentId;

        GPA = gpa < 0 ? 0 : (gpa > 4.0 ? 4.0 : gpa);
    }

    public override void ShowInfo()
    {
        Console.WriteLine(
            $"[Student] Name: {Name}, Age: {Age}, " +
            $"ID: {StudentID}, GPA: {GPA}");
    }

    public override void Work()
    {
        Console.WriteLine(
            $"{Name} studies, attends lectures, and completes assignments.");
    }
}


// Derived Class 2: Teacher
public class Teacher : Person
{
    public string EmployeeID { get; }
    public string Department { get; set; }

    // Teacher Constructor
    public Teacher(string name, int age, string employeeId, string department)
        : base(name, age)
    {
        EmployeeID = string.IsNullOrWhiteSpace(employeeId) ? "T-000" : employeeId;

        Department = string.IsNullOrWhiteSpace(department) ? "N/A" : department;
    }

    public override void ShowInfo()
    {
        Console.WriteLine(
            $"[Teacher] Name: {Name}, Age: {Age}, " +
            $"ID: {EmployeeID}, Dept: {Department}");
    }

    public override void Work()
    {
        Console.WriteLine(
            $"{Name} prepares lectures, teaches students and grades exams.");
    }
}


// Derived Class 3: Graduate Student
public class GraduateStudent : Student
{
    public string ThesisTitle { get; set; }

    // GraduateStudent Constructor
    public GraduateStudent(
        string name,
        int age,
        string studentId,
        double gpa,
        string thesisTitle)
        : base(name, age, studentId, gpa)
    {
        ThesisTitle = string.IsNullOrWhiteSpace(thesisTitle) ? "TBD": thesisTitle;
    }

    public override void ShowInfo()
    {
        Console.WriteLine(
            $"[GradStudent] Name: {Name}, Age: {Age}, " +
            $"ID: {StudentID}, GPA: {GPA}, Thesis: {ThesisTitle}");
    }

    public override void Work()
    {
        Console.WriteLine(
            $"{Name} conducts research, writes thesis, and assists in labs.");
    }
}


// Main Program
class Program
{
    static void Main()
    {
        // Nesne oluşturma
        Person p1 = new Person("Ali Yılmaz", 40);

        Student s1 = new Student(
            "Ayşe Demir", 22, "S123", 3.6);

        Teacher t1 = new Teacher(
            "Dr. Ali", 45, "T001", "Comp. Eng.");

        GraduateStudent g1 = new GraduateStudent(
            "Elif Kaya", 25, "S555", 3.9, "AI in Education");

        // Polymorphic collection
        List<Person> people = new List<Person>
        {
            p1,
            s1,
            t1,
            g1
        };

        Console.WriteLine("ShowInfo (virtual / override)");

        foreach (var person in people)
        {
            person.ShowInfo();
        }

        Console.WriteLine("\nWork (virtual / override)");

        foreach (var person in people)
        {
            person.Work();
        }
    }
}