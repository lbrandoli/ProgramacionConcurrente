#include <iostream>
#include <cstdlib>
#include <ctime>
#include <thread>

void cargarMatriz(int matriz[5][5])
{
  for(int i=0;i<5;i++)
  {
    for(int j=0;j<5;j++)
    {
      int numero_random=(std::rand()%65)-32;
      matriz[i][j]=numero_random;
    }
  }
}

void mostrarMatriz(int matriz[5][5])
{
  for(int i=0;i<5;i++)
  {
    for(int j=0;j<5;j++)
    {
      std::cout.width(5);
      std::cout<< matriz[i][j]<<" ";
    }
    std::cout<<std::endl;
  }
}

void sumarMatrices(int matriz[5][5],int matriz2[5][5],int resultado[5][5])
{
  for(int i=0;i<5;i++)
  {
    for(int j=0;j<5;j++)
    {
      resultado[i][j]=matriz[i][j]+matriz2[i][j];
    }
  }
}

void sumarFila(int fila,int matriz[5][5],int matriz2[5][5],int resultado[5][5])
{
  for(int j=0;j<5;j++)
  {
    resultado[fila][j]=matriz[fila][j]+matriz2[fila][j];
  }
}

int main() 
{
  std::srand(std::time(0));
  
  int A[5][5],B[5][5],CS[5][5],CC[5][5];
  std::cout<<std::endl;
  
  cargarMatriz(A);
  std::cout<<"MATRIZ A"<<std::endl;
  mostrarMatriz(A);
  std::cout<<std::endl;
  
  cargarMatriz(B);
  std::cout<<"MATRIZ B"<<std::endl;
  mostrarMatriz(B);
  std::cout<<std::endl;

  std::cout<<"SUMA SECUENCIAL"<<std::endl;
  sumarMatrices(A,B,CS);
  mostrarMatriz(CS);
  std::cout<<std::endl;

  std::cout<<"SUMA CONCURRENTE"<<std::endl;
  std::thread hilos[5];
  for(int i=0;i<5;i++)
  {
    hilos[i]=std::thread(sumarFila,i,A,B,CC);
  }
  for(int i=0;i<5;i++)
  {
    hilos[i].join();
  }
  mostrarMatriz(CC);
  std::cout<<std::endl;

  return 0;
}
