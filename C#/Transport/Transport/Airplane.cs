using System;


namespace ConsoleApp1
{
    public class Airplane : Transport
    {
        public double WingLenght { get; set; }
        public Airplane(int year, int weight, string color, double wingLenght) 
            : base(year, weight, color)
        {
            WingLenght = wingLenght;
        }

        public override void Info()
        {
            Console.WriteLine("Train");
            Console.WriteLine($"Tear:{Year}\n" +
                $"Weight:{Weight}\n" +
                $"Color{Color}\n");
            Console.WriteLine($"WingLenght:{WingLenght:0.00}\n");
        }
    }
}
