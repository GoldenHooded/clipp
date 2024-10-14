# README - Clipp

## Descripción
Clipp es una herramienta de línea de comandos para gestionar un portapapeles tipo lista, que permite agregar, listar, ejecutar y remover entradas. Su objetivo principal es facilitar la gestión de comandos comunes en la terminal, proporcionando funcionalidades como el autocompletado y la capacidad de ejecutar comandos almacenados de manera sencilla.

## Características
- **Agregar comandos**: Almacena comandos en una lista con o sin descripciones.
- **Listar comandos**: Muestra los comandos almacenados, con opciones para ver los índices y descripciones.
- **Ejecutar comandos**: Ejecuta un comando desde la lista utilizando su índice.
- **Eliminar comandos**: Permite remover comandos por su índice.
- **Autocompletado**: Soporte de autocompletado para una experiencia fluida en la línea de comandos.

## Instalación
### Manualmente
1. Clona este repositorio:
   ```bash
   git clone https://github.com/tuusuario/clipp.git
   cd clipp
   ```
2. Ejecuta el script de instalación:
   ```bash
   sudo ./clipp-refresh
   ```
   Este comando moverá los archivos necesarios al sistema y configurará el autocompletado.

3. Para habilitar el autocompletado de manera persistente, asegúrate de que `~/.bashrc` contenga la siguiente línea:
   ```bash
   source /home/tuusuario/Projects/Clipp/clipp-autocomplete.sh
   ```
   Luego recarga `~/.bashrc`:
   ```bash
   source ~/.bashrc
   ```

### Usando DNF (Recomendado)
1. Habilita el repositorio Copr (requiere que hayas configurado Copr):
   ```bash
   sudo dnf copr enable tuusuario/clipp
   ```
2. Instala Clipp:
   ```bash
   sudo dnf install clipp
   ```

## Uso
- **Agregar un comando sin descripción**:
  ```bash
  clipp add "echo Hola Mundo"
  ```
- **Agregar un comando con descripción**:
  ```bash
  clipp add "ls -la" "Listar directorio con detalles"
  ```
- **Listar comandos con descripciones e índices**:
  ```bash
  clipp list -d -n
  ```
- **Ejecutar un comando por su índice**:
  ```bash
  clipp ex 0
  ```
- **Remover un comando por su índice**:
  ```bash
  clipp remove 1
  ```
- **Limpiar toda la lista**:
  ```bash
  clipp clear
  ```

## Contribuir
Si deseas contribuir al proyecto, puedes hacerlo mediante Pull Requests o abriendo issues para sugerir mejoras o reportar errores. Toda contribución es bienvenida.

## Licencia
Este proyecto está licenciado bajo la Licencia Pública General de GNU v3.0 - consulta el archivo `LICENSE` para más detalles.

