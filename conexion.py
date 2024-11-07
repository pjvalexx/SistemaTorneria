import sqlite3

class Conexion:
    def __init__(self):
        try:
            self.con = sqlite3.connect("sistema.db")
            self.crear_tablas()
        except Exception as ex:
            print("Error al conectar con la base de datos:", ex)

    def crear_tablas(self):
        # SQL para crear la tabla de usuarios
        sql_create_usuarios = """
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                usuario TEXT UNIQUE,
                clave TEXT
            )
        """
        
        # SQL para crear la tabla de órdenes de trabajo
        sql_create_orden_trabajo = """
            CREATE TABLE IF NOT EXISTS orden_trabajo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                telefono TEXT,
                direccion TEXT,
                tipo_servicio TEXT,
                descripcion_servicio TEXT,
                observaciones TEXT,
                fecha_entrega_estimada DATE,
                materiales TEXT,
                monto REAL,
                fecha_creacion DATE DEFAULT CURRENT_DATE
            )
        """
        
        # Ejecutar la creación de tablas
        try:
            cur = self.con.cursor()
            cur.execute(sql_create_usuarios)
            cur.execute(sql_create_orden_trabajo)
            self.con.commit()
            cur.close()
            # Llamar a la función para crear el usuario administrador
            self.crear_admin()
        except Exception as ex:
            print("Error al crear las tablas:", ex)

    def crear_admin(self):
        try:
            # Insertar el usuario administrador si no existe
            sql_insert = "INSERT OR IGNORE INTO usuarios (nombre, usuario, clave) VALUES (?, ?, ?)"
            cur = self.con.cursor()
            cur.execute(sql_insert, ("Administrador", "admin", "admin"))
            self.con.commit()
            cur.close()
        except Exception as ex:
            print("Error al crear el usuario admin:", ex)

    def conectar(self):
        return self.con

    def cerrar_conexion(self):
        if self.con:
            self.con.close()

    def insertar_orden(self, nombre, telefono, direccion, tipo_servicio, descripcion_servicio,
                    observaciones, fecha_entrega_estimada, materiales, monto):
        try:
            sql_insert = '''
                INSERT INTO orden_trabajo 
                (nombre, telefono, direccion, tipo_servicio, descripcion_servicio, observaciones, 
                fecha_entrega_estimada, materiales, monto)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            '''
            cur = self.con.cursor()
            cur.execute(sql_insert, (nombre, telefono, direccion, tipo_servicio, descripcion_servicio,
                                    observaciones, fecha_entrega_estimada, materiales, monto))
            self.con.commit()
            cur.close()
        except Exception as ex:
            print("Error al insertar la orden:", ex)
            raise
