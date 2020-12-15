using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Services;

namespace WebApplication2
{
    /// <summary>
    /// Summary description for WebService1
    /// </summary>
    [WebService(Namespace = "http://tempuri.org/")]
    [WebServiceBinding(ConformsTo = WsiProfiles.BasicProfile1_1)]
    [System.ComponentModel.ToolboxItem(false)]
    // To allow this Web Service to be called from script, using ASP.NET AJAX, uncomment the following line. 
    // [System.Web.Script.Services.ScriptService]
    public class WebService1 : System.Web.Services.WebService
    {

        [WebMethod]
        public string convertHex(int value)
        {
            string hex = Convert.ToString(value, 16);
            return hex;
        }
        [WebMethod]
        public string convertOctal(int value)
        {
            string octal = Convert.ToString(value, 8);
            return octal;
        }

        [WebMethod]
        public string convertBinary(int value)
        {
           
            string binary = Convert.ToString(value, 2);
            return binary;
        }
    }
}