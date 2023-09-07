#include <iostream>
#include <unistd.h>
#include <sys/wait.h>

using namespace std;

void mostrarProceso(char proceso)
{
   cout<<"Proceso "<<proceso<<" --> "<<"PID:"<<getpid()<<"  "<<"PPID:"<<getppid()<<endl;  
}

int main(int argc, char*argv[])
{
  pid_t pidA,pidB,pidC,pidD,pidE,pidF,pidG,pidH;
  pidA=getpid();
  mostrarProceso('A');
  pidB=fork();
  if(pidB == 0)
  {
    pidB=getpid();
    mostrarProceso('B');
    pidD=fork();
    if(pidD == 0)
    {
      pidD=getpid();
      mostrarProceso('D');
      sleep(30);
      exit(0);
    }
    pidE=fork();
    if(pidE == 0)
    {
      pidE=getpid();
      mostrarProceso('E');
      pidG=fork();
      if(pidG == 0)
      {
        pidG=getpid();
        mostrarProceso('G');
        sleep(30);
        exit(0);
      }
       pidH=fork();
      if(pidH == 0)
      {
        pidH=getpid();
        mostrarProceso('H');
        sleep(30);
        exit(0);
      }
      sleep(30);
      wait(NULL);
      wait(NULL);
      exit(0);
    }
    sleep(30);
    wait(NULL);
    wait(NULL);
    exit(0);
  }
  pidC=fork();
  if(pidC == 0)
  {
    pidC=getpid();
    mostrarProceso('C');
    pidF=fork();
    if(pidF == 0)
    {
      pidF=getpid();
      mostrarProceso('F');
      sleep(30);
      exit(0);
    }
    sleep(30);
    wait(NULL);
    exit(0);
  }
  sleep(30);
  wait(NULL);
  wait(NULL);
  return 0;
}
