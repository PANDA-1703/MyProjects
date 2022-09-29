using System;


namespace ConsoleApp1
{
    public class Truck : Car
    {
        public double BodyLength { get; set; }
        public Truck(int year, int weight, string color, double speed, double bodyLength)
            : base(year, weight, color, speed)
        {
            BodyLength = bodyLength;
        }

        public override void Info()
        {
            Console.WriteLine("Train");
            Console.WriteLine($"Tear:{Year}\n" +
                $"Weight:{Weight}\n" +
                $"Color{Color}\n"+
                $"Speed{Speed:0.00}\n");
            Console.WriteLine($"BodyLength:{BodyLength:0.00}\n");
        }
    }
}