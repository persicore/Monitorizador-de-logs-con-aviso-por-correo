Programa de Monitoreo de Logs XML

Programa de Monitoreo de Logs XML
Este programa de Python monitorea un archivo XML en busca de nuevos registros de log y envía alertas por correo electrónico cuando se detectan errores. Es especialmente útil para sistemas que generan registros de actividad en formato XML y necesitan una notificación inmediata de problemas.

Requisitos
Python 3.x
Módulos estándar: xml.etree.ElementTree, smtplib, email.mime.text, datetime, time, logging
Instalación
Clona el repositorio o descarga el archivo ZIP del proyecto.

Asegúrate de tener Python 3.x instalado en tu sistema.

Instala las dependencias utilizando el administrador de paquetes pip:

Copy code
pip install -r requirements.txt
Uso
Coloca el archivo XML que deseas monitorear en el mismo directorio que el script (prueba.xml en este caso).

Configura las variables enviar_con, enviar_a, y contraseña en el script para establecer la configuración de tu servidor de correo saliente.

Ejecuta el script monitor_logs.py:

Copy code
python monitor_logs.py
El programa iniciará la monitorización del archivo XML en busca de nuevos registros de log. Cuando se detecte un nuevo error, enviará una alerta por correo electrónico.

El registro de errores se almacenará en el archivo error_log.txt.

Configuración adicional
Puedes ajustar el intervalo de tiempo entre las verificaciones del archivo XML modificando el valor de time.sleep() en el script.

Personaliza el formato y contenido del correo electrónico en la función enviar_mail_alerta() según tus necesidades específicas.
