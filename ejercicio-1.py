if __name__ == "__main__":
    dict_edades = {"julian": 29, "jesus": 19, "ale": 25}
    l_edades = list(dict_edades.values()) # se convierte el diccionario a una lista
    l_edades.sort() # se organizan ascendentemente los valores 
    print(l_edades)
