from PIL import Image
import os

def resize_images(input_folder, output_folder, width, height):
    # Verificar y crear la carpeta de salida si no existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Obtener la lista de archivos en la carpeta de entrada
    files = os.listdir(input_folder)

    for file in files:
        # Construir la ruta completa de la imagen de entrada
        input_path = os.path.join(input_folder, file)

        # Verificar si es un archivo de imagen (por la extensión)
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            print(f'Procesando {file}...')  # Mensaje de depuración

            try:
                # Abrir la imagen utilizando PIL
                img = Image.open(input_path)

                # Redimensionar la imagen
                resized_img = img.resize((width, height), Image.LANCZOS)

                # Construir la ruta completa de la imagen de salida
                output_path = os.path.join(output_folder, file)

                # Guardar la imagen redimensionada en la carpeta de salida
                resized_img.save(output_path)

                print(f'{file} redimensionado y guardado correctamente en {output_folder}.')

            except Exception as e:
                print(f'Error al procesar {file}: {e}')

    print("Todas las imágenes han sido redimensionadas y guardadas correctamente.")

# Ejemplo de uso
if __name__ == "__main__":
    input_folder = input("Dime la carpeta origen: ")  # Ruta de la carpeta de entrada
    output_folder = input("Dime la carpeta destino: ") # Ruta de la carpeta de salida
    width = 512  # Ancho deseado en píxeles
    height = 512  # Alto deseado en píxeles

    resize_images(input_folder, output_folder, width, height)