import java.io.IOException;

public class javaProcessTree {
    static int cantHijosA = 2;
    static int cantHijosB = 2;
    static int cantHijosC = 1;
    static int cantHijosE = 2;

    public static void main(String[] args) 
    {
        int cantHijos = 0;
        char nombreNodo = 'A';
        Process procesos[] = null;
        String procesoActual = "A";
        if (args.length != 0)
            procesoActual = args[0];

        ProcessHandle obtenerPID = ProcessHandle.current();

        System.out.println("soy el proceso " + procesoActual + " de PID: " + obtenerPID.pid() + " y PPID: "
                + obtenerPID.parent().get().pid());

        if (procesoActual.equals("A")) 
        {
            cantHijos = cantHijosA;
            procesos = new Process[cantHijosA];
        } else if (procesoActual.equals("B")) 
        {
            cantHijos = cantHijosB;
            procesos = new Process[cantHijosB];
            nombreNodo += cantHijosA;
        } else if (procesoActual.equals("C")) 
        {
            cantHijos = cantHijosC;
            procesos = new Process[cantHijosC];
            nombreNodo = (char) ('C' + cantHijosB);
        } else if (procesoActual.equals("E")) 
        {
            cantHijos = cantHijosE;
            procesos = new Process[cantHijosE];
            nombreNodo = (char) ('E' + cantHijosC);
        } else 
        {
            try 
            {
                Thread.sleep(10000);
            } catch (InterruptedException e) 
            {
                e.printStackTrace();
            }
            return;
        }

        for (int i = 1; i <= cantHijos; i++) 
        {
            ProcessBuilder proceso = new ProcessBuilder("java", "ArbolDeProcesos.java",
                    Character.toString(nombreNodo + i));
            proceso.inheritIO();
            try 
            {
                procesos[i - 1] = proceso.start();
            } catch (IOException e) 
            {
                e.printStackTrace();
            }
        }
        for (int i = 0; i < cantHijos; i++) 
        {
            try 
            {
                procesos[i].waitFor();
            } catch (InterruptedException e) 
            {
                e.printStackTrace();
            }
        }
    }
}
