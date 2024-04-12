import os
import sys
sys.path.append(r"C:/Users/MathiusZ/Desktop/ConexiónBD2")  # Reemplaza "/ruta/a/ConexionBD" con la ruta real a tu proyecto
from dao import daoConnection
from models import clases as c

os.system('cls')
conex = daoConnection.Connection("localhost", "root", "", "bdregisters")
conex.connect()

#funcion para validar que el status sea valido (solamente puede ser 1 o 2)
def validar_status(status):
    if status == 1 or status == 2:
        return True
    else:
        return False
    
#CIUDAD FULL
def InsertarCiudad():
    os.system('cls')
    name = input("Nombre ciudad: ")
    ciudad = c.City(name, 1, any)
    daoCity = daoConnection.DaoCity(conex)
    #insertar
    daoCity.insert(ciudad)

def MostrarCiudad():
    os.system('cls')
    daoCity = daoConnection.DaoCity(conex)
    print("Ciudades de la base de datos: ")
    #mostrar
    cities = daoCity.get_all()
    for city in cities:
        print(city)

def ElimiarCiudad():
    os.system('cls')
    MostrarCiudad()
    NameElimiar = input("escoja el id de la ciudad que quiere eliminar:")
    
    daoCity = daoConnection.DaoCity(conex)
    #eliminar
    daoCity.delete(NameElimiar)

def EditarCiudad():
    os.system('cls')
    MostrarCiudad()
    oldID = input("ID de la ciudad a editar: ")
    newName = input("Nuevo Nombre: ")
    newStatus = int(input("Ingrese el nuevo estado: 1) Activo || 2) Inactivo: "))

    if validar_status(newStatus):
        print("Status valido")
        daoCity = daoConnection.DaoCity(conex)
        ciudad = c.City(newName, newStatus, oldID)
        #actualizar
        daoCity.update(ciudad)
    else:
        print("Status inválido. Debe ser 1 o 2.")

def BuscarCiudad():
    os.system('cls')
    nameBuscar = input("escriba el nombre de la ciudad que quiere buscar:")
    
    daoCity = daoConnection.DaoCity(conex)
    #buscar
    cities = daoCity.get_by_id(nameBuscar)
    print(cities)

def MenuCiudad():
    os.system('cls')
    print("----MENU CIUDAD----")
    print("1. Ingresar ciudad")
    print("2. mostrar ciudades")
    print("3. eliminar ciudad")
    print("4. editar ciudad")
    print("5. buscar ciudad")
    print("6. salir")
    print("-------------------")

def mainCiudad():
    opcion= 0
    while(opcion != 6):
        MenuCiudad()
        opcion = int(input("dime tu opcion:"))
        if (opcion == 1):
            InsertarCiudad()
            os.system("pause")
        elif (opcion == 2):
            MostrarCiudad()
            os.system("pause")
        elif (opcion == 3):
            ElimiarCiudad()
            os.system("pause")
        elif (opcion == 4):
            EditarCiudad()
            os.system("pause")    
        elif (opcion == 5):
            BuscarCiudad()
            os.system("pause")





#TRABAJO FULL
def InsertarTrabajo():
    os.system('cls')
    name = input("Nombre Trabajo: ")
    trabajo = c.Job(name, 1, any)

    daoJob = daoConnection.DaoJob(conex)
    #insertar
    daoJob.insert(trabajo)

def MostrarTrabajo():
    os.system('cls')
    daoJob = daoConnection.DaoJob(conex)
    print("Trabajos de la base de datos: ")
    #mostrar
    jobs = daoJob.get_all()
    for job in jobs:
        print(job)

def ElimiarTrabajo():
    os.system('cls')
    MostrarTrabajo()
    NameElimiar = input("escoja el id del trabajo que quiere eliminar:")
        
    daoJob = daoConnection.DaoJob(conex)
    #eliminar
    daoJob.delete(NameElimiar)

def EditarTrabajo():
    os.system('cls')
    MostrarTrabajo()
    oldId = int(input("ID del Trabajo a editar: "))
    newName = input("Nuevo Nombre: ")
    newStatus = int(input("Ingrese el nuevo estado: 1) Activo || 2) Inactivo: "))

    
    if validar_status(newStatus):
        print("Status valido")
        daoJob = daoConnection.DaoJob(conex)
        trabajo = c.Job(newName, newStatus, oldId)
        #actualizar
        daoJob.update(trabajo)
    else:
        print("Status inválido. Debe ser 1 o 2.")    

def BuscarTrabajo():
    os.system('cls')
    NameBuscar = input("escriba el nombre del trabajo que quiere buscar:")
    
    daoJob = daoConnection.DaoJob(conex)
    #buscar e imprimir
    job = daoJob.get_by_id(NameBuscar)
    print(job)

def MenuTrabajo():
    os.system('cls')
    print("----MENU TRABAJOS----")
    print("1. Ingresar trabajo")
    print("2. mostrar trabajos")
    print("3. eliminar trabajo")
    print("4. editar trabajo")
    print("5. buscar trabajo")
    print("6. salir")
    print("--------------------")

def mainTrabajo():
    opcion= 0
    while(opcion != 6):
        MenuTrabajo()
        opcion = int(input("dime tu opcion:"))
        if (opcion == 1):
            InsertarTrabajo()
            os.system("pause")
        elif (opcion == 2):
            MostrarTrabajo()
            os.system("pause")
        elif (opcion == 3):
            ElimiarTrabajo()
            os.system("pause")
        elif (opcion == 4):
            EditarTrabajo()
            os.system("pause")    
        elif (opcion == 5):
            BuscarTrabajo()
            os.system("pause")





#EMPLEADOS FULL
def InsertarEmpleado():
    os.system('cls')
    nombre = input("Nombre Del Empleado: ")
    MostrarCiudad()
    ciudadid = input("Ingrese el ID de la ciudad del empleado: ")
    MostrarTrabajo()
    jobid = input("Ingrese el ID del cargo del empleado: ")
    salario = input("ingrese el salario del empleado: ")

    empleado = c.Employee(nombre, ciudadid, jobid, salario, 1, any)
    daoEmployee = daoConnection.DaoEmployee(conex)
    #insertar
    daoEmployee.insert(empleado)

def MostrarEmpleado():
    os.system('cls')

    daoEmployee = daoConnection.DaoEmployee(conex)
    print("Empleados de la base de datos: ")
    #mostrar empleados
    employees = daoEmployee.get_all()
    for employee in employees:
        print(employee)

def ElimiarEmpleado():
    os.system('cls')
    MostrarEmpleado()
    EmpleadoElimiar = input("escoja el id del trabajo que quiere eliminar:")
        
    daoEmployee = daoConnection.DaoEmployee(conex)
    #eliminar
    daoEmployee.delete(EmpleadoElimiar)

def EditarEmpleado():
    os.system('cls')
    MostrarEmpleado()
    oldId = int(input("ID del empleado a editar: "))
    newName = input("Nuevo Nombre: ")
    os.system('cls')
    MostrarCiudad()
    newCityid = input("Nueva ID de ciudad: ")
    os.system('cls')
    MostrarTrabajo()
    newJobid = input("Nueva ID de trabajo: ")
    newSalary = input("Nuevo salario: ")
    newStatus = int(input("Ingrese el nuevo estado: 1) Activo || 2) Inactivo: "))

    if validar_status(newStatus):
        print("Status valido")
        daoEmployee = daoConnection.DaoEmployee(conex)
        empleado = c.Employee(newName, newCityid, newJobid, newSalary, newStatus, oldId)
        #actualizar
        daoEmployee.update(empleado)
    else:
        print("Status inválido. Debe ser 1 o 2.")

def BuscarEmpleado():
    os.system('cls')
    nameBuscar = input("escriba el nombre del empleado que quiere buscar:")

    daoEmployee = daoConnection.DaoEmployee(conex)
    #buscar e imprimir
    employee = daoEmployee.get_by_id(nameBuscar)
    print(employee)

def MenuEmpleado():
    os.system('cls')
    print("----MENU EMPLEADOS----")
    print("1. Ingresar empleado")
    print("2. mostrar empleados")
    print("3. eliminar empleado")
    print("4. editar empleado")
    print("5. buscar empleado")
    print("6. salir")
    print("----------------------")

def mainEmpleado():
    opcion= 0
    while(opcion != 6):
        MenuEmpleado()
        opcion = int(input("dime tu opcion:"))
        if (opcion == 1):
            InsertarEmpleado()
            os.system("pause")
        elif (opcion == 2):
            MostrarEmpleado()
            os.system("pause")
        elif (opcion == 3):
            ElimiarEmpleado()
            os.system("pause")
        elif (opcion == 4):
            EditarEmpleado()
            os.system("pause")    
        elif (opcion == 5):
            BuscarEmpleado()
            os.system("pause")



#MAIN MENU
def MenuPrincipal():
    print("----MENU PRINCIPAL----")
    print("1. Registros ciudades")
    print("2. Registros trabajos")
    print("3. Registros empleados")
    print("4. Salir")
    print("----------------------")

def main():
    opcion= 0
    while(opcion != 4):
        os.system('cls')
        MenuPrincipal()
        opcion = int(input("dime tu opcion:"))
        if (opcion == 1):
            mainCiudad()
            os.system("pause")
        elif (opcion == 2):
            mainTrabajo()
            os.system("pause")
        elif (opcion == 3):
            mainEmpleado()
            os.system("pause")       
        
                        
main()


#IGNORAR ESTO :D
#city1 = c.City("Managua", 1)
#city2 = c.City("León", 1)
#city3 = c.City("Granada", 1)
#city4 = c.City("Masaya", 1)
#city5 = c.City("Estelí", 1)
#city6 = c.City("Jinotepe", 1)

#instanciar dao
#daoCity = daoConnection.DaoCity(conex)
#insertar
#daoCity.insert(city1)
#daoCity.insert(city2)
#daoCity.insert(city3)
#daoCity.insert(city4)
#daoCity.insert(city5)
#daoCity.insert(city6)

#consultar
#cities = daoCity.get_all()
#for city in cities:
    #print(city)



#instanciar modelo
#job1 = c.Job("Carguero", 1)
#job2 = c.Job("Administrador", 1)
#job3 = c.Job("Seguridad", 1)
#job4 = c.Job("Conductor", 1)

#instanciar dao
#daoJob = daoConnection.DaoJob(conex)
#insertar
#daoJob.i1
# nsert(job1)
#daoJob.insert(job2)
#daoJob.insert(job3)
#daoJob.insert(job4)

#consultar
#jobs = daoJob.get_all()
#for job in jobs:
    #print(job)



#instanciar modelo
#employee1 = c.Employee("Mathius", 2, 2, "15000", 1)
#employee2 = c.Employee("Jose", 1, 3, "8000", 1)
#employee3 = c.Employee("Rodrigo", 5, 4, "7000", 1)
#employee4 = c.Employee("Bryan", 6, 1, "11000", 1)

#instanciar dao
#daoEmployee = daoConnection.DaoEmployee(conex)
#insertar
#daoEmployee.insert(employee1)
#daoEmployee.insert(employee2)
#daoEmployee.insert(employee3)
#daoEmployee.insert(employee4)

#consultar
#employees = daoEmployee.get_all()
#for employee in employees:
    #print(employee)