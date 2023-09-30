#include <iostream>
#include <thread>
#include <vector>
#include <string>
#include <mutex>

std::mutex mtx;

// Est función la utilizmos para convertir el caracter en su valor numérico
int charToNumber(char c)
{
    return c - 'A' + 1; // Le restamos A ya que representa el numero ascii de esa letra y luego le sumamos 1 para saber cual seria el numero correspondiente en el alfabeto
}

// Esta funcion la utilizamos para recorrer la parte del string que le corresponde a cada hilo
void convertCharacters(const std::string& input, std::vector<int>& result, int start, int end)
{
    for (int i = start; i <= end; i++)
    {
        char c = input[i];
        if (c >= 'a' && c <= 'z')
        {
            c = std::toupper(c);
        }
        result[i] = charToNumber(c);
    }
}

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        std::cout << "Uso: " << argv[0] << " <cadena_de_caracteres>" << std::endl;
        return 1;
    }

    std::string input(argv[1]);
    int length = input.length();
    std::vector<int> result(length);

    int threadCount = 2; // Cantidad de hilos que vamos a crear
    int charsPerThread = length / threadCount; // Cantidad de caracteres que va a convertir cada hilo
    int extraChars = length % threadCount; // Si la cantidad de caracteres es par vale 0 y si es impar vale 1

    //Creamos un vector de hilos de forma tal que el manejo de hilos sea mas facil
    std::vector<std::thread> threads;

    //Creamos los dos hilos
    for (int i = 0; i < threadCount; i++)
    {
        // Si i es cero el punto de inicio es el primer caracter, si i es 1 el punto de inicio será la mitad de la cadena
        int start = i * charsPerThread;
        
        // Si i es 0 tiene que convertir hasta el caracter anterior que la mitad de la cadena y si i es 1 convierte hasta el ultimo sea par o impar la cadena
        int end = (i != threadCount - 1) ? (start + charsPerThread - 1) : (start + charsPerThread + extraChars - 1); 
  
        // Utilizamos este metodo para crear un hilo y agregarlo al vector de hilos y ademas utilizamos una funcion lamda para el trabajo que necesitamos que haga cada hilo
        threads.emplace_back
        ([&, start, end]() 
          {
              convertCharacters(input, result, start, end);
          }
        );
    }

    // Recorremos el vector de hilos y esperamos a ambos hilos
    for (std::thread& thread : threads)
    {
        thread.join();
    }

    for (int i = 0; i < length; i++)
    {
        std::cout << result[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
