import os
from time import sleep

def padre():
    
    pidPadre = os.getpid()
    print("PID del proceso padre: %d\n" % pidPadre)

    numProcesos = int(input("introduce el número de procesos a ejecutar: "))

    while numProcesos > 0:
        pid = os.fork()
        numProcesos = numProcesos - 1

        if pid == 0:
            hijo()
     
def hijo():
    print("\n -> Proceso hijo con PID: %d a punto de terminar " % os.getpid())
    sleep(5)
    print("\nProceso %d TERMINADO" % os.getpid())
    os._exit(0)

if __name__ == "__main__": 
    padre()