using System;


namespace ConsoleApp1
{
    public class Passenger : Car
    {
        public string PassengerType { get; set; }
        public Passenger(int year, int weight, string color, double speed, string passenger)
            : base(year, weight, color, speed)
        {
            PassengerType = passenger;
        }

        public override void Info()
        {
            Console.WriteLine("Train");
            Console.WriteLine($"Tear:{Year}\n" +
                $"Weight:{Weight}\n" +
                $"Color{Color}\n" +
                $"Speed{Speed:0.00}\n");
            Console.WriteLine($"PassengerType:{PassengerType}\n");
        }
    }
}