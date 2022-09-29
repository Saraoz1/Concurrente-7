#Nota: Para este examen tendrá que aplicar el concepto de acquire() y release()


#Ejemplo acquire() y release() :  

import threading
# threading.Lock

# La clase que implemente los objetos de la primitiva lock. Una vez que un hilo ha adquirido un lock, intentos subsecuentes por adquirirlo bloquearán, hasta que sea liberado; cualquier hilo puede liberarlo.
# Nótese que Lock es una función de fábrica que retorna una instancia de la versión más eficiente de la clase Lock concreta soportada por la plataforma.


# acquire(blocking=True, timeout=- 1)
# Adquirir un lock, bloqueante o no bloqueante.
# Cuando se invoca con el argumento blocking establecido como True (el valor por defecto), bloquea hasta que el lock se abra, luego lo establece como cerrado y retorna True.
# Cuando es invocado con el argumento blocking como False, no bloquea. Si una llamada con blocking establecido como True bloqueara, retorna Falso inmediatamente; de otro modo, cierra el lock y retorna True.
# When invoked with the floating-point timeout argument set to a positive value, block for at most the number of seconds specified by timeout and as long as the lock cannot be acquired. A timeout argument of -1 specifies an unbounded wait. It is forbidden to specify a timeout when blocking is False.
# El valor de retorno es True si el lock es adquirido con éxito, Falso si no (por ejemplo si timeout expiró).


# release()
# Libera un lock. Puede ser llamado desde cualquier hilo, no solo el hilo que ha adquirido el lock.
# Cuando el lock está cerrado, lo restablece a abierto, y retorna. Si cualquier otro hilo está bloqueado esperando que el lock se abra, permite que exactamente uno de ellos proceda.
# Cuando se invoca en un lock abierto, se lanza un RuntimeError.
# No hay valor de retorno.
mutex = threading.Lock()
def crito(id):
    global x;
    x = x + id
    print("Hilo =" +str(id)+ " =>" + str(x))
    x=1

class Hilo(threading.Thread):
     def __init__(self, id):
        threading.Thread.__init__(self)
        self.id=id

     def run(self):
        mutex.acquire() #Inicializa semáforo , lo adquiere
        crito(self.id)
        mutex.release() #Libera un semáforo e incrementa la varibale

hilos = [Hilo(1), Hilo(2), Hilo(3)]
x=1;
for h in hilos:
    h.start()