using System;


namespace ConsoleApp1
{
    public class Train : Transport
    {
        public int Carriages { get; set; }
        public Train(int year, int weight, string color, int carriages)
            : base(year, weight, color)
        {
            Carriages = carriages;
        }

        public override void Info()
        {
            Console.WriteLine("Train");
            Console.WriteLine($"Tear:{Year}\n" +
                $"Weight:{Weight}\n" +
                $"Color{Color}\n");
            Console.WriteLine($"Carriages:{Carriages}\n");
        }
    }
}
