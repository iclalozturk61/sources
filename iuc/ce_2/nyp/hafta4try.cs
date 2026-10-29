
abstract class LibraryMaterial{
    public int Id { get; set; }
    public string Title {get; set;}

    protected LibraryMaterial(int id, string title)
    {
        if(id <= 0)
        {
            throw new ArgumentException($"{id} değeri 0 dan büyük olmalıdır");
        }

        if(string.IsNullOrWhiteSpace(title))
        {
            throw new ArgumentException($"{title} değeri boş olamaz");
        }

        Id = id;
        Title = title;
    }

    public abstract string GetMaterialType();

    public void DisplayInfo()
    {
        Console.WriteLine($"{Title} 'ı bir {GetMaterialType()} türünden materialdir. ID'si: {Id}'dir"); //this. yazmaya gerek yok c# zaten anlıyor 
    }
}

interface IBorrowable{
    bool IsBorrowed { get; set; }
    int LoanPeriodDays {get;} //kaç günlüğüne ödünç verilebilir?
    DateTime? DueDate {get; set;}   

    void Borrow();
    void Return();

}

class Book : LibraryMaterial, IBorrowable
{
    public Book(int id, string title) : base(id, title){}
    public bool IsBorrowed {get; set; }
    public int LoanPeriodDays
    {
        get{ return 14; }
    }
    
    public DateTime? DueDate {get; set;}

    public void Borrow()
    {   
        if (!IsBorrowed) //verilmemişse girdi
        {
            IsBorrowed = true;
            DueDate = DateTime.Today.AddDays(LoanPeriodDays);
        }
        else
        {
            throw new InvalidOperationException($"{Title} ödünç verilmiş alınamaz");
        }
    }

    public override string GetMaterialType()
    {
        return "kitap";
    }

    public void Return()
    {
        if (IsBorrowed) //verilmişse içeri gir
        {
            IsBorrowed = false;
            DueDate = null;
        }
        else
        {
            throw new InvalidOperationException($"{Title} zaten geri verilmiş");
        }
    }
}

class Dvd: LibraryMaterial, IBorrowable
{
    public Dvd(int id, string title): base(id, title){}

    public bool IsBorrowed{get; set;}
    public int LoanPeriodDays => 7;

    public DateTime? DueDate {get; set;}

    public override string GetMaterialType() => "dvd";
    public void Borrow()
    {
        if (!IsBorrowed)//verilmemişse içeri gir
        {
            IsBorrowed = true;
            DueDate = DateTime.Today.AddDays(LoanPeriodDays);
        }
        else
        {
            throw new InvalidOperationException($"{Title} ödünç verilmiş alınamaz");
        }
    }

    public void Return()
    {
        if (IsBorrowed) //verilmişse içeri gir
        {
            IsBorrowed = false;
            DueDate = null;
        }
        else
        {
            throw new InvalidOperationException($"{Title} zaten geri verilmiş");
        }
    }
}

class ReferenceBook : LibraryMaterial
{
    public ReferenceBook(int id, string title) : base(id,title){}

    public override string GetMaterialType() => "reference book";

}

class Program
{
    static void Main()
    {
        List<LibraryMaterial> materials = new List<LibraryMaterial>
        {
            new Book(1001, "beyoglunun en güzel abisi"),
            new Book(1002, "martı jonathan livingston"),
            new Dvd(2001, "winy the poo"),
            new Dvd(2002, "arkadaşım hoşgeldin"),
            new ReferenceBook(3001, "elementary linear algebra"),
            new ReferenceBook(3002, "fizik 2")
        };
 

        foreach (LibraryMaterial material in materials)
        {
            material.DisplayInfo();
            if (material is IBorrowable borrowable) // IBorrowable implemente ettiyse borrowable adında bir değişkende tut
            {
                try
                {
                borrowable.Borrow();
                Console.WriteLine($"Ödünç verildi, iade tarihi: {borrowable.DueDate}");
                }

                catch(InvalidOperationException ex)
                {
                    Console.WriteLine(ex.Message);
                }
            }
            else
            {
                Console.WriteLine("bu materyal ödünç verilemiyor");
            }
            Console.WriteLine();

        }




    }
}

