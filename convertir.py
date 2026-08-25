from PIL import Image

# Cargar la imagen PNG que generaste
img = Image.open("chroniobox_logo.png")

# Guardar directamente como formato ICO con múltiples resoluciones para Windows
img.save(
    "icono.ico", 
    format="ICO", 
    sizes=[(256, 256), (128, 128), (64, 64), (32, 32), (16, 16)]
)

print("[*] ¡Listo! El archivo 'icono.ico' se ha creado correctamente.")