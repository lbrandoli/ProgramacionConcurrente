import java.util.*;
import java.util.concurrent.*;


class Main 
{
  public static void main(String[] args) 
  {
    int N = Integer.parseInt(args[0]);
    ArrayBlockingQueue<Integer> colaBloq = new ArrayBlockingQueue<>(N);
    
    System.out.println();
    System.out.println("La cantidad de numeros ingresados es de: "+N);
    
    Thread productor = new Thread(new Producer(colaBloq, N));
    Thread consumidor = new Thread(new Consumer(colaBloq, N));
    
    productor.start();
    consumidor.start();
  }
}


class Producer implements Runnable 
{
  private final BlockingQueue<Integer> cola;
  private final int N;
  public Producer(BlockingQueue<Integer> colaBloq, int N) 
  {
    this.cola = colaBloq;
    this.N = N;
  }

  @Override
  public void run() 
  {
    try
    {
      for (int i = 0; i < N; i++) 
      {
        int valor = new Random().nextInt(100);
        System.out.println("Producido: " + valor);
        cola.put(valor);
      }
      cola.put(-1); 
    }
    catch (InterruptedException e) 
    {
      Thread.currentThread().interrupt();
    }
  }
}


class Consumer implements Runnable
{
  private final BlockingQueue<Integer> cola;
  private final int N;
  private final Map<Integer,Integer> frecuencia=new HashMap<>();
  public Consumer (BlockingQueue<Integer>cola, int N)
  {
    this.cola=cola;
    this.N=N;
  }
  @Override
  public void run()
  {
    try
      {
        int sum=0;
        int min=Integer.MAX_VALUE;
        int max=Integer.MIN_VALUE;

        for(int i=0;i<N;i++)
        {
          int valor=cola.take();
          if(valor == -1)
            break;
          sum+=valor;
          min=Math.min(min,valor);
          max=Math.max(max,valor);
          frecuencia.put(valor,frecuencia.getOrDefault(valor,0)+1);
        }

        float promedio=(float) sum/N;

        List<Integer>masFrecuenteValores=new ArrayList<>();
        int maxFrecuente=Collections.max(frecuencia.values());
        for(Map.Entry<Integer,Integer> entry:frecuencia.entrySet())
        {
          if(entry.getValue()==maxFrecuente)
          {
            masFrecuenteValores.add(entry.getKey());
          }
        }

        System.out.println();
        System.out.println("Promedio: "+ promedio);
        System.out.println("Min: " + min);
        System.out.println("Max: " + max);
        System.out.println("Sum: " + sum);
        System.out.println("Mas frecuente valores: " + masFrecuenteValores);
      }
    catch(InterruptedException e)
      {
        Thread.currentThread().interrupt();
      }
  }
}
