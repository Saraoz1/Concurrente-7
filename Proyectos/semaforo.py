from threading import Thread, Semaphore
semaforo = Semaphore(1) #Crea la variable semáforo

def crito(id):
    global x;
    x = x + id
    print("Hilo =" +str(id)+ " =>" +str(x))
    x=1

class Hilo(Thread):
    def __init__(self,id):
        Thread.__init__(self)
        self.id=id

def run(self):
    semaforo.acquire() #inicializa el semaforo, lo adquiere
    crito(self.id)
    semaforo.release() #libera un semáforo e incrementa la variable semáforo

threads_semafore = [Hilo(1),Hilo(2),Hilo(3)]
x=1;
for t in threads_semafore:
    t.start()