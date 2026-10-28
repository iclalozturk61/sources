using System.Data.Common;

abstract class LibraryMaterial{
    public int Id { get; set; }
    public string Title {get; set;}

    public LibraryMaterial(int id, string title)
    {
        Id = id;
        Title = title;
    }

    public abstract string GetMaterialType();

    public void DisplayInfo()
    {
        Console.WriteLine($"{this.Title} 'ı bir {this.GetMaterialType} türünden materialdir. ID'si: {this.Id}'dir");
    }
}

interface IBorrowable{
    bool IsBorrowed { get; set; }
}