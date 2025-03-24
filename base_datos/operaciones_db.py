from base_datos.modelo_empleados import Empleado, session

def insertar_empleado(nombre, salario, departamento):

    nuevo_empleado = Empleado(nombre=nombre, salario=salario, departamento=departamento)
    session.add(nuevo_empleado)
    session.commit()
    print(f"Empleado '{nombre}' agregado correctamente.")

def consultar_por_departamento(departamento):

    empleados = session.query(Empleado).filter_by(departamento=departamento).all()
    print(f"Empleados en el departamento '{departamento}':")
    for emp in empleados:
        print(f"- {emp.nombre}, Salario: {emp.salario}")
    return empleados

def calcular_salario_promedio(departamento):

    empleados = session.query(Empleado).filter_by(departamento=departamento).all()
    if empleados:
        promedio = sum(emp.salario for emp in empleados) / len(empleados)
        print(f"Salario promedio en el departamento '{departamento}': {promedio}")
        return promedio
    print(f"No hay empleados en el departamento '{departamento}'.")
    return 0
