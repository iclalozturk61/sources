using System;
// Class (Sınıf) tanımı
// Sınıf, nesneler için bir taslaktır (template). Arabaların ortak özelliklerini ve davranışlarını içerir.
class Car
{
    // Fields (Alanlar): Nesnenin verilerini tutar.
    public string brand; // Marka
    public string model; // Model
    public int year; // Üretim yılı
    public double speed; // Hız (km/h)


    // Method (Metot): Nesnenin gerçekleştirdiği davranışları tanımlar.
    public void Start()
    {
        Console.WriteLine($"{brand} {model} çalıştırıldı.");
    }


    public void Accelerate(double increase)
    {
        speed += increase;
        Console.WriteLine($"Hız artırıldı. Yeni hız: {speed} km/h");
    }


    public void Brake(double decrease)
    {
        speed -= decrease;
        if (speed < 0) speed = 0; // Negatif hız olmaması için kontrol
        Console.WriteLine($"Fren yapıldı. Yeni hız: {speed} km/h");
    }


    public void ShowInfo()
    {
        Console.WriteLine($"Marka: {brand}, Model: {model}, Yıl: {year}, Anlık Hız: {speed} km/h");
    }
}


// Main metodu: Programın başlangıç noktasıdır.
class Program
{
    static void Main(string[] args)
    {
        // Object (Nesne) oluşturma
        // 'Car' sınıfından bir nesne (örnek) oluşturuyoruz.
        Car myCar = new Car();


        // Nesne alanlarını (fields) doldurma
        myCar.brand = "Tesla";
        myCar.model = "Model 3";
        myCar.year = 2022;
        myCar.speed = 0;


        // Nesne metotlarını çağırma
        myCar.ShowInfo();
        myCar.Start();
        myCar.Accelerate(50);
        myCar.Accelerate(30);
        myCar.Brake(40);
        myCar.ShowInfo();
    }
}
