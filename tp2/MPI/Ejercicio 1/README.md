a) ¿Que funcion realiza la instancia maestra?¿Que funcion realiza las instancias esclavas?

La instancia maestra genera una lista de tareas y las distribuye entre los procesos esclavos. Cada proceso esclavo realiza su tarea y devuelve el resultado al proceso maestro.

b) ¿Cuantas de esas instancias ejecuta la funcion main(), initWork() y doWork()?

La funcion main() se ejecuta en la instancia maestra, mientras que la funcion dowork() se ejecuta en las instancias esclavas. La funcion initWork() se llama desde la funcion main(), pero no se ejecuta en una instancia separada, sino que se llama desde la funcion main().

c)¿Como se diferencian los mensajes de trabajo o de finalizacion?

Se utilizan dos constantes de comunicacion para diferenciar los mensajes de trabajo, estan constantes son WORK_FLAG y END_WORK_FLAG. El proceso maestro envia mensajes de trabajo a los procesos esclavos utilizando la constante WORK_FLAG. El mensaje contiene el tiempo de espera correspondiente a la tarea asignada. Los procesos esclavos envian el resultado de su tarea al proceso maestro utilizando la misma constante WORK_FLAG. Por otro lado, el proceso maestro envia mensajes de finalizacion a los procesos esclavos utilizando la constante END_WORK_FLAG. Cuando un proceso esclavo recibe un mensaje con esta constante, sabe que debe finalizar su trabajo y terminar su ejecucion.

d)¿Como implementaria la funcion BLAS axpy() con este patron?¿Seria eficiente?Tips:Pide solo el planteo, no la implementacion.

La funcion axpy de BLAS es una operacion vectorial que calcula el producto de un vector por un escalar y lo suma a otro vector, asi que si utilizamos el patron maestro-esclavo, se podria dividir el vector en subvectores y distribuirlos entre los procesos esclavos. Cada proceso esclavo calcularia el producto de su subvector por el escalar y lo sumaria al subvector correspondiente. Luego, los resultados parciales se enviarian al proceso maestro para que los ume y obtenga el resultado final.

d)¿Que sucede cuando solo ejecuta con una sola instancia?

Cuando se ejecuta con una sola instancia el proceso maestro y el proceso esclavo se ejecutan en la misma instancia, en este caso, el proceso maestro generara una lista de tareas aleatorias y las asignara al mismo proceso que se esta ejecutando.