using System;


namespace ConsoleApp1
{
    public class Car : Transport
    {
        public double Speed { get; set; }
        public Car(int year, int weight, string color, double speed) 
            : base(year, weight, color)
        {
            Speed = speed;
        }

        public override void Info()
        {
            Console.WriteLine("Train");
            Console.WriteLine($"Tear:{Year}\n" +
                $"Weight:{Weight}\n" +
                $"Color{Color}\n");
            Console.WriteLine($"Speed:{Speed:0.00}\n");
        }
    }
}