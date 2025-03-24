import unittest
from base_datos.modelo_empleados import Empleado, Base, engine, session
from base_datos.operaciones_db import insertar_empleado, consultar_por_departamento, calcular_salario_promedio


class TestOperacionesDB(unittest.TestCase):
    def setUp(self):

        self.engine = engine
        Base.metadata.drop_all(bind=self.engine)
        Base.metadata.create_all(bind=self.engine)
        self.session = session

    def tearDown(self):

        self.session.query(Empleado).delete()
        self.session.commit()

    def test_insertar_empleado(self):

        insertar_empleado(nombre="Carlos López", salario=2800.0, departamento="Marketing")
        empleado = self.session.query(Empleado).filter_by(nombre="Carlos López").first()

        self.assertIsNotNone(empleado)
        self.assertEqual(empleado.salario, 2800.0)
        self.assertEqual(empleado.departamento, "Marketing")

    def test_consultar_por_departamento(self):


        insertar_empleado(nombre="Laura Méndez", salario=3200.0, departamento="Recursos Humanos")
        insertar_empleado(nombre="Luis Pérez", salario=2900.0, departamento="Recursos Humanos")

        empleados = consultar_por_departamento("Recursos Humanos")

        self.assertEqual(len(empleados), 2)
        self.assertEqual(empleados[0].nombre, "Laura Méndez")
        self.assertEqual(empleados[1].nombre, "Luis Pérez")

    def test_calcular_salario_promedio(self):

        insertar_empleado(nombre="Pedro Gómez", salario=2700.0, departamento="Finanzas")
        insertar_empleado(nombre="Lucía García", salario=3300.0, departamento="Finanzas")

        promedio = calcular_salario_promedio("Finanzas")

        self.assertAlmostEqual(promedio, 3000.0)


if __name__ == "__main__":
    unittest.main()
