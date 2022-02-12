### **Curso Intro Python**
#### Módulo 2. Crear un paquete

##### Editor: Cristopher Alan.
##### Date: 06/02/2022

##### **Step 1:** Crear un entorno virtual

**Consideración:** Para crear el entorno virtual se tiene que haber instalado previamente la biblioteca de Python para los entornos virtuales (virtualenv library).
```bash
    python3 -m venv Module_2_env
```
    python -m venv env

##### **Step 2**: Activar el entorno virtual creado
Para activar el entorno en un ambiente de Linux se usa la siguiente instrucción.
```bash
    source Module_2_env/bin/activate
```
Estando en la ruta correcta del directorio creado para el proyecto al activar el entorno debe cambiar la primer parte de la línea en la terminal.
![Activar_entorno](https://github.com/CristopherA96/LaunchX_IntroPython_w1/blob/b57fbe44858ee299ca6adc7ae4daebddaaf326bc/images/launchx_module_2_s2.png)

##### **Step 3**: Instalar el paquete python-dateutil
Para instalar el paquete python-dateutil dentro del entorno virtual activado se utiliza:
```bash
pip install python-dateutil
```
Esto mostrará un mensaje de
![Instalar_paquete](https://github.com/CristopherA96/LaunchX_IntroPython_w1/blob/79f7acf0812abd67faf2bf58e272042175f272ff/Module_2/Module_2_images/launchx_module_2_s3.png)

##### **Step 4**: Verificar que python-dateutil está instalado en el env.
Para verificar que el paquete esta instalado en el entorno se utiliza:
```bash
pip freeze
```
Esto mostrará el listado de paquetes instalados en ese entorno virtual creado.

##### **Step 5**: Testear la instalación del paquete.
Para testear el paquete se realiza el ejercicio del archivo app.py en este directorio.
![Testeo](https://github.com/CristopherA96/LaunchX_IntroPython_w1/blob/79f7acf0812abd67faf2bf58e272042175f272ff/Module_2/Module_2_images/launchx_module_2_s5.png)


