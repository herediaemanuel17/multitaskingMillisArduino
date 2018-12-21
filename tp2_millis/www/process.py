from models import Medidas
from database import Database
import time
import serial
from aux_pro import Process



def inicializar(arduino):
    arduino.setDTR(False)
    time.sleep(0.5)
    arduino.flushInput()
    arduino.setDTR(True)

def main():
    db = Database()
    medidas = Medidas()
    arduino = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1.0)
    inicializar(arduino)
    reset = 0
    m = medidas
    with arduino:
        while True:
            try:
                if arduino.inWaiting() > 0:
                    cadena = arduino.readline().strip()
                    datos = cadena.split('/')
                    session = db.get_session()
                    if len(datos) == 6:
                        m.servomotor = int(datos[3])
                        m.ultrasonido = int(datos[1])
                        m.potenciometro = int(datos[5])
                        session.add(m)
                        session.commit()
                        session.close()
                        reset = reset + 1
                        if reset == 2:
                            inicializar(arduino)
            except KeyboardInterrupt:
                print ("no se pueden leer datos de arduino")
                break
        arduino.close()
        
if __name__ == "__main__":
    main()
