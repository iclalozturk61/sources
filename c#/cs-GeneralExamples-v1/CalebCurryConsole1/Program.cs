using System;
using System.Xml.Linq;
using static System.Runtime.InteropServices.JavaScript.JSType;
namespace CalebCurryConsole1
{
    //ÖNEMLİ: bu dosyada Nullable uyarıları kapatılmıştır. Solution explorerda <Nullable>enable</Nullable> şekilde düzeltilerek açılabilir.
    class Program
    {
        static void Main(string[] args)
        {
            Program myProgram = new Program();
            myProgram.doSomething();

        }
        
        public void doSomething()
        {
            User me = new User();
            me.FirstName = "Caleb";
            me.LastName = "Curry";

            User you = new User();
            you.FirstName = "İclal";
            you.LastName = "Öztürk";

            List<User> users = new List<User>();
            users.Add(me);users.Add(you);

            foreach (User usr in users)
                Console.WriteLine(usr.FullName);

        }


    }
}
