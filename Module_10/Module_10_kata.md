## **Curso Intro Python**
### Módulo 10: Manejo de errores
Se realizan los ejercicios en el archivo Markdown del Módulo 10.

#### Intentando abrir el archivo mars.jpg dentro de path y de to.
open("/path/to/mars.jpg")

#### Creando un archivo de Python asignandole el nombre open.py
```python
def main():
    open("/path/to/mars.jpg")

if __name__ == '__main__':
    main()
```
El error se muestra:
![Error_1]()

#### Creando el archivo config.py para saber su error y entenderlo
```python
def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")


if __name__ == '__main__':
    main()
```
El error que sale es:
![Error_2]()
Este error hace referencia a que no se encontró el archivo config.txt.

#### Controlando el error sería
```python
def main():
    try:
        configuration = open('config.txt')
    except Exception:
        print("Couldn't find the config.txt file!")
```
En mí caso ya no marcó error porque cree un archivo en la ruta del programa que se llama config.txt.

#### Generación de excepciones
* La generación de excepciones también puede ayudar en la toma de decisiones para otro código.
* En este caso los astronautas limitan su uso de agua a unos 11 litros al día. Creando una función para que con base al número de astronautas, pueda calcular la cantidad de agua que quedará después de un día o más.
```python
def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    return f"Total water left after {days_left} days is: {total_water_left} liters"
```
Probando con 5 astronautas, 100 litros de agua restante y 2 días restantes. Se tiene:
![Output]()

Si se modifica el programa, ya que una carencia en los litros sería un error.
```python
def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"
```
La salida es la siguiente, donde se muestra un error:
![Output_2]()

Maneobrando el error TypeError, se modifica el archivo de austronauts.py.
```python
def water_left(astronauts, water_left, days_left):
    for argument in [astronauts, water_left, days_left]:
        try:
            # If argument is an int, the following operation will work
            argument / 10
        except TypeError:
            # TypError will be raised only if it isn't the right type 
            # Raise the same exception but with a better error message
            raise TypeError(f"All arguments must be of type int, but received: '{argument}'")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"
```
La salida es la siguiente:
![Error_5]()
![Error_6]()