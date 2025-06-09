import os
import datetime

def obtener_fecha_archivo(ruta_imagen):
    timestamp = os.path.getctime(ruta_imagen)  # También puedes usar getmtime
    fecha = datetime.datetime.fromtimestamp(timestamp)
    return fecha.strftime("%Y-%m-%d %H:%M:%S")

enfermedad = "pudrición_del_corazón"
ruta_imagen = "sana1.jpg"  # Ruta de la imagen

# Obtener fecha de la imagen (creación del archivo)
fecha_foto = obtener_fecha_archivo(ruta_imagen)
info_detallada = ""
tratamiento = ""

if enfermedad == "pudrición_del_corazón":
    #print("Tiene la enfermedad Pudrición del corazón")
    fecha_de_foto = fecha_foto
    enfermedad = "Pudrición del corazón"
    tratamiento = "Mejorar drenaje del suelo, aplicar fungicidas sistémicos a base de fosetil-Al o metalaxil son recomendados."

elif enfermedad == "pudrición_de_la_raíz":
    #print("Tiene la enfermedad Pudrición de la raíz")
    fecha_de_foto = fecha_foto
    enfermedad = "Pudrición de la raíz"
    tratamiento = "Evitar encharcamientos, mejorar drenaje del suelo."

elif enfermedad == "antracnosis":
    #print("Tiene la enfermedad Antracnosis")
    fecha_de_foto = fecha_foto
    enfermedad = "Antracnosis"
    tratamiento = "Aplicar fungicidas a base de cobre y eliminar partes infectadas."

elif enfermedad == "mancha_de_la_hoja":
    #print("Tiene la enfermedad Mancha de la hoja")
    fecha_de_foto = fecha_foto
    enfermedad = "Mancha de la hoja"
    tratamiento = "Usar fungicidas foliares específicos y mejorar ventilación entre plantas."

elif enfermedad == "marchitez_de_la_corona":
    #print("Tiene la enfermedad Marchitez de la corona")
    fecha_de_foto = fecha_foto
    enfermedad = "Marchitez de la corona"
    tratamiento = "Eliminar plantas infectadas, evitar acumulación de agua."

elif enfermedad == "roya_de_la_piña":
    #print("Tiene la enfermedad Roya de la piña")
    fecha_de_foto = fecha_foto
    enfermedad = "Roya de la piña"
    tratamiento = "Aplicar fungicidas como mancozeb y reducir humedad relativa."

else:
    #print("La planta está sana")
    fecha_de_foto = fecha_foto
    enfermedad = "Sana"
    tratamiento = "Ninguno"
