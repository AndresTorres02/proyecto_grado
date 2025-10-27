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
        info_detallada = "Causada por Phytophthora cinnamomi o P. nicotianae. Afecta el tallo y las raíces, provocando hojas marchitas, amarillentas y mal olor interno en la planta."

    elif enfermedad == "pudrición_de_la_raíz":
        enfermedad = "Pudrición de la raíz"
        tratamiento = "Evitar encharcamientos, mejorar drenaje del suelo."
        info_detallada = "Provocada por Phytophthora nicotianae var. parasitica. Ataca las raíces y la base del tallo, causando debilitamiento y marchitez en plantas jóvenes."

    elif enfermedad == "antracnosis":
        enfermedad = "Antracnosis"
        tratamiento = "Aplicar fungicidas a base de cobre y eliminar partes infectadas."
        info_detallada = "Causada por el hongo Colletotrichum gloeosporioides. Produce manchas oscuras en hojas, lesiones hundidas en frutos y reduce la calidad de la piña."

    elif enfermedad == "mancha_de_la_hoja":
        enfermedad = "Mancha de la hoja"
        tratamiento = "Usar fungicidas foliares específicos y mejorar ventilación entre plantas."
        info_detallada = "Originada por hongos del género Cercospora. Genera manchas marrones o grises en hojas que disminuyen la fotosíntesis y el vigor de la planta."

    elif enfermedad == "marchitez_de_la_corona":
        enfermedad = "Marchitez de la corona"
        tratamiento = "Eliminar plantas infectadas, evitar acumulación de agua."
        info_detallada = "Causada por Fusarium subglutinans f. sp. ananas. Provoca la pudrición y marchitez de la corona, afectando el crecimiento y el desarrollo del fruto."

    elif enfermedad == "roya_de_la_piña":
        enfermedad = "Roya de la piña"
        tratamiento = "Aplicar fungicidas como mancozeb y reducir humedad relativa."
        info_detallada = "Producida por Puccinia horiana. Se manifiesta con pústulas anaranjadas o marrones en el envés de las hojas, reduciendo la fotosíntesis y el rendimiento."

    else:
        enfermedad = "Sana"
        tratamiento = "Ninguno"
        info_detallada = "La planta se encuentra en buen estado y no presenta síntomas visibles de enfermedades fúngicas."

    return fecha, enfermedad, info_detallada, tratamiento
