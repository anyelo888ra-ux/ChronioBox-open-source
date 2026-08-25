from PIL import Image, ImageDraw

# Crear una imagen cuadrada de alta resolución para el icono (512x512)
size = (512, 512)
image = Image.new("RGBA", size, (0, 0, 0, 0))
draw = ImageDraw.Draw(image)

# Dibujar cubos estilizados superpuestos (Inspiración VirtualBox / Estilo Moderno)
# Caja base exterior (Sombra / Contorno tecnológico)
draw.rounded_rectangle([40, 40, 472, 472], radius=80, fill=None, outline=(40, 40, 40, 255), width=24)

# Cubo posterior principal (Gris oscuro elegante)
draw.rounded_rectangle([90, 90, 420, 420], radius=50, fill=(30, 30, 30, 255), outline=(60, 60, 60, 255), width=10)

# Cubo flotante delantero (Color Naranja ChronioBox con efecto neón/brillo)
draw.rounded_rectangle([160, 160, 450, 450], radius=50, fill=(255, 123, 0, 230), outline=(255, 165, 50, 255), width=12)

# Detalle interno simulando una pantalla o núcleo de virtualización
draw.rounded_rectangle([210, 210, 400, 400], radius=25, fill=(18, 18, 18, 255))

# Guardar como PNG
image.save("chroniobox_logo.png")
print("[*] ¡Logo generado con éxito como 'chroniobox_logo.png'!")