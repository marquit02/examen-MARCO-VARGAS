import csv
import random
trabajadores =["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanchez","Isabel Gomez","Fracisco Diaz","Elena Fernandez"]
sueldos=[]

def sueldos_aleatorios():
    for i in range(len(trabajadores)):
        sueldos.append({"nombre":trabajadores[i],"sueldo":random.randint(300000,2500000)})
    print("Sueldos Generados")
        
def clasificar_sueldos():
    print("Ordenados de mayor a menor")
    p_ordenados=sorted(sueldos,key=lambda x:x["sueldo"],reverse=True)
    for i in p_ordenados:
        print(f'{i["nombre"]}:{i["sueldo"]}')
    return
        

def estadisticas():
    total=0
    producto=1
    p_ordenados=sorted(sueldos,key=lambda x:x["sueldo"])
    print("1.-mostrar sueldo mas alto")
    print("="*30)
    print("2.-mostrar sueldo mas bajo")
    print("="*30)
    print("3.-promedio de sueldos")
    print("="*30)
    print("4.-media geometrica")
    while True:
        try:
            opcion=int(input("ingrese una opcion"))
        except ValueError:
            print("solo valores numericos")
        else:    
            match opcion:
                case 1:
                    print(max(p_ordenados,key=lambda x:x["sueldo"]))
                case 2:
                    print(min(p_ordenados,key=lambda x:x["sueldo"]))
                case 3:
                    for i in sueldos:
                        total+=i["sueldo"]
                        print(f"promedio de los sueldos es:{total/len(trabajadores)}")
                case 4:
                    m=len(trabajadores)
                    for i in sueldos:
                        producto*=sueldos["sueldo"]
                        resultado=producto**(1/m)
                        print(f"la media geometrica :{resultado.__trunc__()}")
                    return
                    
            

def reporte_sueldos():
    with open("sueldos.csv","w") as archivo_csv:
        archivo_csv.write("Nombre | Sueldo | descuento | AFP | Sueldo liquido")
    with open("sueldos.csv","a") as archivo_csv:
        for i in sueldos:
            descuento=0.07*i["sueldo"]
            AFP=0.12*i["sueldo"]
            sueldo_liquido=i["sueldo"]-descuento-AFP
            archivo_csv.write(f"{i["nombre"]},{i["sueldo"]},{descuento},{AFP},{sueldo_liquido}\n")
            
            return "reporte generado"
            

    
while True: 
    print("="*30)
    print("1.-generar sueldos aleatorios")
    print("2.-clasificar sueldos")
    print("3.-ver estadisticas")
    print("4.-reporte sueldos")
    print("5.salir-")
    print("="*30)
    while True:
        try:
            opcion_menu=int(input("ingrese la opcion que desee: "))
        except ValueError:
            print("solo valores numericos")
        match opcion_menu:
            case 1:
                sueldos_aleatorios()
            case 2:
                clasificar_sueldos()
            case 3:
                estadisticas()
            case 4:
                reporte_sueldos()
            case 5:
                print("ADIOS")
                break
                exit
    break

            
            
    

    