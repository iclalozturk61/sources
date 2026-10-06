using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CalebCurryConsole1
{
    public class User
    {
        public string FullName
        {
            get{
                return FirstName + " " + LastName;
            }            
        }

        public string FirstName { get; set; }
        public string LastName { get; set; }

        public string Output (int times)
        {
            string message = "";
            for (int i = 0; i < times; i++) {
                message += FirstName + " " + LastName + "\n";
            }  
          return message;
        }
    }
}
