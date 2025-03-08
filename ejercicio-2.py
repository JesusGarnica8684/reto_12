def blend_dict(dictUno, dictDos : dict) -> dict:
    dictGen = dictUno.copy()  # se crea un nuevo diccionario con los mismos elementos del primer diccionario
    for key, val in dictDos.items():  # se itera sobre el segundo diccionario
        if key not in dictGen:  # si la llave no está en el nuevo diccionario, la agregamos
            dictGen[key] = val
    return dictGen

if __name__ == "__main__":
    units = {"a": 1, "b": 2, "c": 3}
    dect = {"b": 20, "c": 30, "d": 40}
    blend = blend_dict(units, dect)
    print(blend)