using System;
namespace estructura
{
    class hello
    {
        static void Main()
        {
            int[] notas = new int[5] { 4, 3.5, 3, 2.6, 4 };

            double prom = 0;
            int cont = 0;

            for (int i = 0; i < notas.length; i++)
            {
                prom += notas[i];
                cont++;
                double a = prom / (notas.length);

                if (cont == notas.length)
                    Console.WriteLine(a);
            }
        }
    }
}