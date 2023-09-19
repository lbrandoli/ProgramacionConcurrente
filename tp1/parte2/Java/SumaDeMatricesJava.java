import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class SumaDeMatricesJava
{

    private static int FILS = 5;
    private static int COLS = 5;
    public static int maxNumero = 32;
    public static int minNumero = -32;

    public int[][] matrizA = new int[FILS][COLS];
    public int[][] matrizB = new int[FILS][COLS];
    public int[][] matrizCS = new int[FILS][COLS];
    public int[][] matrizCC = new int[FILS][COLS];

    public SumaDeMatricesJava()
    {
        matrizA = new int[FILS][COLS];
        matrizB = new int[FILS][COLS];
        matrizCS = new int[FILS][COLS];
        matrizCC = new int[FILS][COLS];
    }

    public void inicializarMatrices()
    {
        Random random = new Random();
        int cantElementos = FILS * COLS;
        for (int i = 0; i < cantElementos; i++)
        {
            int numero = random.nextInt(maxNumero - minNumero + 1) + minNumero;
            matrizA[i / FILS][i % COLS] = numero;
            matrizB[i / FILS][i % COLS] = numero;
        }
    }

    public void sumaMatrizSecuencial()
    {
        for (int i = 0; i < matrizA.length; i++)
        {
            for (int j = 0; j < matrizA[0].length; j++)
            {
                matrizCS[i][j] = matrizA[i][j] + matrizB[i][j];
            }
        }
    }

    public void sumaMatrizConcurrente()
    {
        List<SumaFilaThread> threads = new ArrayList<SumaFilaThread>();
        SumaFilaThread.setSumaDeMatricesJava(this);
        for (int i = 0; i < SumaDeMatricesJava.FILS; i++)
        {
            threads.add(new SumaFilaThread(i));
        }
        for (SumaFilaThread sumaFilaThread : threads)
        {
            sumaFilaThread.start();
        }
        for (SumaFilaThread sumaFilaThread : threads)
        {
            try
            {
                sumaFilaThread.join();
            }
            catch (InterruptedException e)
            {
                e.printStackTrace();
            }
        }
    }

    public static void mostrarMatriz(int[][] matriz, String nombre)
    {
        System.out.println("\nmatriz " + nombre);
        for (int i = 0; i < matriz.length; i++)
        {
            System.out.print("[ ");
            for (int j = 0; j < matriz[0].length; j++)
            {
              System.out.printf("%3d ", matriz[i][j]);
            }
        System.out.println(" ]");
        }
    }


    public void compararMatrices()
    {
      for(int i=0; i < SumaDeMatricesJava.FILS; i++)
        for(int j=0; j < SumaDeMatricesJava.COLS; j++)
        {
          if(matrizCS[i][j] != matrizCC[i][j])
          {
            System.out.println("\nlas matrices no son iguales en la posicion: (" + i + "; " + j + ")" );
            return;
          }
        }
      System.out.println("\nlas matrices CS y CC son iguales.");
    }

    public static void main(String[] args)
    {
        SumaDeMatricesJava sumaDeMatrices = new SumaDeMatricesJava();
        sumaDeMatrices.inicializarMatrices();
        sumaDeMatrices.sumaMatrizSecuencial();
        sumaDeMatrices.sumaMatrizConcurrente();
        mostrarMatriz(sumaDeMatrices.matrizA, "A");
        mostrarMatriz(sumaDeMatrices.matrizB, "B");
        mostrarMatriz(sumaDeMatrices.matrizCS, "CS");
        mostrarMatriz(sumaDeMatrices.matrizCC, "CC");
        sumaDeMatrices.compararMatrices();
    }

    public static class SumaFilaThread extends Thread
    {
        public static SumaDeMatricesJava matrices = null;
        private int fila;

        public SumaFilaThread(int fila)
        {
            this.fila = fila;
        }

        @Override
        public void run()
        {
            for (int i = 0; i < matrices.matrizA[0].length; i++)
            {
                matrices.matrizCC[this.fila][i] = matrices.matrizA[this.fila][i] + matrices.matrizB[this.fila][i];
            }
        }

        public static void setSumaDeMatricesJava(SumaDeMatricesJava s)
        {
            SumaFilaThread.matrices = s;
        }
    }
}