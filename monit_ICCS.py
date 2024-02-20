import xml.etree.ElementTree as ET
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import time
import logging

# Configuración básica del registro de errores, esto crea un fichero que registra los errores del programa
logging.basicConfig(filename='error_log.txt', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s:%(message)s')

def enviar_mail_alerta(log_entry):
    try:
        # Configuración del mail
        enviar_con = ""
        enviar_a = ""
        contraseña = ""
        # Configuramos el contenido del mail
        msg = MIMEText(f"Nuevo log de error detectado en SRVWEB2: '{log_entry}'")
        msg['Subject'] = "Nuevo XML log de error"
        msg['From'] = enviar_con
        msg['To'] = enviar_a
        # Enviamos el mail
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        server.starttls()
        server.login(enviar_con, contraseña)
        server.sendmail(enviar_con, enviar_a, msg.as_string())
        server.quit()
        print("Email de alerta enviado")
    except Exception as e:
        logging.error(f"Error enviando el mail de alerta: {e}")

def main():
    try:
        # Inicialmente, carga el archivo XML y encuentra el log más reciente
        tree = ET.parse('prueba.xml')
        root = tree.getroot()
        # Encuentra el timestamp más reciente en el archivo al momento de iniciar el programa
        ultimavez_procesado = max([datetime.strptime(msg.get('time'), '%Y-%m-%d %H:%M:%S') for msg in root.findall('msg')], default=datetime.min)
    except ET.ParseError as e:
        logging.error(f"Error al parsear XML inicialmente: {e}")
        ultimavez_procesado = datetime.min
    except Exception as e:
        logging.error(f"Error inesperado al iniciar: {e}")
        ultimavez_procesado = datetime.min

    while True:
        try:
            tree = ET.parse('prueba.xml')
            root = tree.getroot()
            nuevo_ultimavez_procesado = ultimavez_procesado

            for msg in root.findall('msg'):
                log_time_str = msg.get('time')
                try:
                    log_time = datetime.strptime(log_time_str, '%Y-%m-%d %H:%M:%S')
                    if log_time > ultimavez_procesado:
                        enviar_mail_alerta(msg.text)
                        if log_time > nuevo_ultimavez_procesado:
                            nuevo_ultimavez_procesado = log_time
                except ValueError as e:
                    logging.error(f"Error al convertir el tiempo: {e}")

            ultimavez_procesado = nuevo_ultimavez_procesado
        except ET.ParseError as e:
            logging.error(f"Error al parsear XML: {e}")
        except Exception as e:
            logging.error(f"Error inesperado: {e}")

        time.sleep(10)  # Pausa de 10 segundos para el ejemplo, ajusta según sea necesario

if __name__ == "__main__":
    main()

