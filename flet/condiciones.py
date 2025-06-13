# condiciones.py
import os
import datetime

def obtener_condiciones(nombre_foto, enfermedad_detectada):
    ruta_imagen = os.path.join("imagenes_tomadas", nombre_foto)
    timestamp = os.path.getctime(ruta_imagen)
    fecha = datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")

    enfermedad = enfermedad_detectada.lower().replace(" ", "_")
    tratamiento = ""
    info_detallada = ""  # Puedes personalizar esto si lo deseas

    if enfermedad == "pudrición_del_corazón":
        enfermedad = "Pudrición del corazón"
        tratamiento = "Mejorar drenaje del suelo, aplicar fungicidas sistémicos a base de fosetil-Al o metalaxil son recomendados."

    elif enfermedad == "pudrición_de_la_raíz":
        enfermedad = "Pudrición de la raíz"
        tratamiento = "Evitar encharcamientos, mejorar drenaje del suelo."

    elif enfermedad == "antracnosis":
        enfermedad = "Antracnosis"
        tratamiento = "Aplicar fungicidas a base de cobre y eliminar partes infectadas."

    elif enfermedad == "mancha_de_la_hoja":
        enfermedad = "Mancha de la hoja"
        tratamiento = "Usar fungicidas foliares específicos y mejorar ventilación entre plantas."

    elif enfermedad == "marchitez_de_la_corona":
        enfermedad = "Marchitez de la corona"
        tratamiento = "Eliminar plantas infectadas, evitar acumulación de agua."

    elif enfermedad == "roya_de_la_piña":
        enfermedad = "Roya de la piña"
        tratamiento = "Aplicar fungicidas como mancozeb y reducir humedad relativa."

    else:
        enfermedad = "Sana"
        tratamiento = "Ninguno"

    return fecha, enfermedad, info_detallada, tratamiento
