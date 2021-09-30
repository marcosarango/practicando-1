def main():
    nombre = saludo("marco")
    print("Welcome to our collaborative program")
    saludo(nombre)
def saludo(y):
    nombre = y
    full_name = nombre
    return full_name 
resultado = saludo("marco")
print(resultado)