/*
Senaryo
Bir kütüphanede kitap, DVD ve yalnızca kütüphane içinde kullanılabilen referans kitapları bulunmaktadır.
Bütün materyallerin ortak özellikleri vardır; ancak yalnızca bazı materyaller ödünç alınabilir. 
Kitaplar 14 gün, DVD’ler 7 gün ödünç verilebilir. Referans kitapları ise dışarı çıkarılamaz.

Görevler
1. LibraryMaterial isimli bir abstract sınıf oluşturunuz.
2. LibraryMaterial sınıfına aşağıdaki property’leri ekleyiniz:
   - Id
   - Title
3. Bu property’leri alan bir constructor yazınız.
4. LibraryMaterial sınıfında materyal türünü döndürecek aşağıdaki abstract metodu tanımlayınız:
    
    public abstract string GetMaterialType();
    
6. LibraryMaterial sınıfına materyal bilgilerini ekrana yazdıran çalışan bir DisplayInfo() metodu ekleyiniz.
7. Ödünç alınabilen materyalleri temsil etmek üzere IBorrowable isimli bir interface oluşturunuz.
8. Interface içerisinde aşağıdaki üyeleri tanımlayınız:
   - IsBorrowed
   - LoanPeriodDays
   - DueDate
   - Borrow()
   - Return()
   
9. Book sınıfını oluşturunuz.
   - LibraryMaterial sınıfından kalıtım almalıdır.
   - IBorrowable interface’ini uygulamalıdır.
   - Ödünç alma süresi 14 gün olmalıdır.
   - Zaten ödünç alınmışsa tekrar ödünç verilmemelidir.
10. Dvd sınıfını oluşturunuz.
    - LibraryMaterial sınıfından kalıtım almalıdır.
    - IBorrowable interface’ini uygulamalıdır.
    - Ödünç alma süresi 7 gün olmalıdır.
11. ReferenceBook sınıfını oluşturunuz.
    - LibraryMaterial sınıfından kalıtım almalıdır.
    - IBorrowable interface’ini uygulamamalıdır.
    - Bu nedenle ödünç alınamamalıdır.
    
12. Program.cs içerisinde bütün materyalleri bir List<LibraryMaterial> koleksiyonunda tutunuz.
13. Döngü kullanarak bütün materyallerin bilgilerini ekrana yazdırınız.
14. Materyalin IBorrowable interface’ini uygulayıp uygulamadığını kontrol ediniz.
15. Ödünç alınabilen materyalleri ödünç veriniz ve son iade tarihlerini ekrana yazdırınız.
16. Ödünç alınamayan materyaller için aşağıdaki mesajı gösteriniz:
    
        "Bu materyal yalnızca kütüphane içinde kullanılabilir."
  
*/




using System;
using System.Collections.Generic;

public abstract class LibraryMaterial
{
    public int Id { get; }
    public string Title { get; }

    protected LibraryMaterial(int id, string title)
    {
        if (id <= 0)
        {
            throw new ArgumentException(
                "Materyal numarası sıfırdan büyük olmalıdır.");
        }

        if (string.IsNullOrWhiteSpace(title))
        {
            throw new ArgumentException(
                "Materyal başlığı boş bırakılamaz.");
        }

        Id = id;
        Title = title;
    }

    public abstract string GetMaterialType();

    public void DisplayInfo()
    {
        Console.WriteLine($"Numara: {Id}");
        Console.WriteLine($"Başlık: {Title}");
        Console.WriteLine($"Tür: {GetMaterialType()}");
    }
}

public interface IBorrowable
{
    bool IsBorrowed { get; }

    int LoanPeriodDays { get; }

    DateTime? DueDate { get; }

    void Borrow(DateTime borrowDate);

    void Return();
}

public class Book : LibraryMaterial, IBorrowable
{
    public string Author { get; }

    public bool IsBorrowed { get; private set; }

    public int LoanPeriodDays => 14;

    public DateTime? DueDate { get; private set; }

    public Book(
        int id,
        string title,
        string author)
        : base(id, title)
    {
        Author = author;
    }

    public override string GetMaterialType()
    {
        return "Kitap";
    }

    public void Borrow(DateTime borrowDate)
    {
        if (IsBorrowed)
        {
            throw new InvalidOperationException(
                $"{Title} zaten ödünç alınmış.");
        }

        IsBorrowed = true;
        DueDate = borrowDate.AddDays(LoanPeriodDays);
    }

    public void Return()
    {
        if (!IsBorrowed)
        {
            throw new InvalidOperationException(
                $"{Title} zaten kütüphanede.");
        }

        IsBorrowed = false;
        DueDate = null;
    }
}

public class Dvd : LibraryMaterial, IBorrowable
{
    public int DurationMinutes { get; }

    public bool IsBorrowed { get; private set; }

    public int LoanPeriodDays => 7;

    public DateTime? DueDate { get; private set; }

    public Dvd(
        int id,
        string title,
        int durationMinutes)
        : base(id, title)
    {
        DurationMinutes = durationMinutes;
    }

    public override string GetMaterialType()
    {
        return "DVD";
    }

    public void Borrow(DateTime borrowDate)
    {
        if (IsBorrowed)
        {
            throw new InvalidOperationException(
                $"{Title} zaten ödünç alınmış.");
        }

        IsBorrowed = true;
        DueDate = borrowDate.AddDays(LoanPeriodDays);
    }

    public void Return()
    {
        if (!IsBorrowed)
        {
            throw new InvalidOperationException(
                $"{Title} zaten kütüphanede.");
        }

        IsBorrowed = false;
        DueDate = null;
    }
}

public class ReferenceBook : LibraryMaterial
{
    public string ShelfNumber { get; }

    public ReferenceBook(
        int id,
        string title,
        string shelfNumber)
        : base(id, title)
    {
        ShelfNumber = shelfNumber;
    }

    public override string GetMaterialType()
    {
        return "Referans Kitabı";
    }
}

public static class Program
{
    public static void Main()
    {
        List<LibraryMaterial> materials = new()
        {
            new Book(
                1,
                "Nesne Yönelimli Programlama",
                "Ahmet Yazar"),

            new Dvd(
                2,
                "C# Eğitim Videoları",
                180),

            new ReferenceBook(
                3,
                "Bilgisayar Bilimleri Ansiklopedisi",
                "R-102")
        };

        DateTime borrowDate = DateTime.Today;

        foreach (LibraryMaterial material in materials)
        {
            Console.WriteLine("-------------------------");

            material.DisplayInfo();

            if (material is IBorrowable borrowable)
            {
                try
                {
                    borrowable.Borrow(borrowDate);

                    Console.WriteLine("Ödünç alma başarılı.");
                    Console.WriteLine(
                        $"Ödünç süresi: " +
                        $"{borrowable.LoanPeriodDays} gün");

                    Console.WriteLine(
                        $"Son iade tarihi: " +
                        $"{borrowable.DueDate:dd.MM.yyyy}");
                }
                catch (InvalidOperationException exception)
                {
                    Console.WriteLine(
                        $"İşlem başarısız: {exception.Message}");
                }
            }
            else
            {
                Console.WriteLine(
                    "Bu materyal yalnızca kütüphane " +
                    "içinde kullanılabilir.");
            }
        }
    }
}