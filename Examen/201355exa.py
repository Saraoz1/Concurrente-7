import threading
import time

cantidad_personas = 8;
palillos= []

def estadoP(persona):
    
    pa_izq = palillos[persona]                       
    p_der = palillos[(persona - 1) % cantidad_personas] 
    pa_izq.acquire()
    if p_der.acquire(blocking=False):              
        print(f"persona {persona} tiene los dos palillos")
        return True
    else:
        pa_izq.release()
        print(f"persona {persona} comparte palillo")      
        return False


def liberacion(persona):

    palillos[persona].release()
    palillos[(persona - 1) % cantidad_personas].release()   
    print(f"liberacion {persona} de palillos")

def Comida(persona):
    tiempoC = 0
    while tiempoC < 10:
        if estadoP(persona):                       
            
            tiempo_comer = min(4, 10 - tiempoC)
            tiempoC += tiempo_comer
            print(f"persona {persona} comiendo")
            time.sleep(tiempoC)
            liberacion(persona)
            
            print(f"persona {persona} termino de comer")
            time.sleep(5)
        else:            
            
            print(f"persona {persona} en espera ")
            time.sleep(3)
        



if __name__ == '__main__':
    for _ in range(cantidad_personas):
        palillos.append(threading.Lock()) 
    hilos = []
    for i in range(cantidad_personas):
        nuevo_hilo = threading.Thread(target=Comida, args=(i,))
        hilos.append(nuevo_hilo)
    
    for hilo in hilos:
        hilo.start()
    
    for hilo in hilos:
        hilo.join()
