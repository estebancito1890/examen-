#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video], ...]

productos ={'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
};

#stock = {modelo: [precio, stock], ]
stock = {'8475HD': [387990,10], 
         '2175HD': [327990,4], 
         'JjfFHD': [424990,1],
         'fgdxFHD': [664990,21],
         '123FHD': [290890,32],
         '342FHD': [444990,7],
         'GF75HD': [749990,2], 
         'UWU131HD': [349990,1],
         'FS1230HD': [249990,0],
};

def stock_marca(marca):
    total = 0
    for codigo, datos in productos.items():
        if (datos[0].lower() == marca.lower()):
            total += stock[codigo][1];
    print(F"El stock total para {marca} es el {total}");

def busqueda_por_precio(p_min, p_max):
    resultado = [];
    for codigo, datos in productos.items():
        precio = stock[codigo][0]
        if precio >= p_min and precio <= p_max and stock [codigo][1] > 0:
            resultado.append(datos[0] + "--" + codigo);
    if resultado:
        resultado.sort();
        print("El producto encontrado es: ", resultado);
    else:
        print("No se encuentra productos en ese rango de precio!!!");

def actualizar_precio(modelo, nuevo_precio):
    if modelo in stock:
        stock[modelo][0] = nuevo_precio;
        return True;
    return False;

def main():
    while True:
        try:
            print("*** MENU PRINCIPAL ***");
            print("1. Stock marca. ");
            print("2. Búsqueda por precio. ");
            print("3. Actualizar precio. ");
            print("4. Salir.");
            opc = int(input("Ingrese una opción: "));
            if opc == 1:
                marca = input("Ingrese la marca del producto que quiere: ");
                stock_marca(marca);
            elif opc == 2:
                p_min = int(input("Ingrese el precio minimo: "));
                p_max = int(input("Ingrese el precio maximo: "));
                busqueda_por_precio(p_min, p_max);
            elif opc == 3:
                while True:
                    try:
                        nuevo_precio = int(input("Ingrese el nuevo precio: "))
                        nuevo_modelo = input("Ingrese el nuevo modelo: ")
                        if actualizar_precio(nuevo_modelo, nuevo_precio):
                            print("Precio actualizado!!")
                        else:
                            print("El modelo no existe!!")

                    except ValueError:
                        print("Debe ingresar numeros")
                    repetir = input("Desea acrualizar otro producto (s/n)?: ").lower();
                    if (repetir != "s"):
                        break;
            elif opc == 4:
                print("Programa finalizado.")
            else:
                print("La opcion que ingreso es invalida!!!!!!");
        except ValueError:
            print("Debe ingresar solo numero enteros!!!")
if __name__ == "__main__":
    main();