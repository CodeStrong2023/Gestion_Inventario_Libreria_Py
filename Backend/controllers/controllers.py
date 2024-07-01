

import sqlite3


class Crud:
    @staticmethod
    def crear(instance, conn):
        cls = instance.__class__
        table_name = cls.__name__
        attributes = vars(instance)
        
        
        keys = ", ".join(attributes.keys())
        question_marks = ", ".join("?" for _ in attributes)
        values = tuple(attributes.values())
        sql_insert = f"INSERT INTO {table_name} ({keys}) VALUES ({question_marks})"
        
        
        cursor = conn.execute(sql_insert, values)
        conn.commit()

        if any(key.startswith('id') for key in attributes):
            for key in attributes:
                if key.startswith('id') and attributes[key] is None:
                    setattr(instance, key, cursor.lastrowid)
                    break

    @staticmethod
    def leer(cls, conn, id):
        table_name = cls.__name__
        key_name = "id"+table_name
        
        sql_select = f"SELECT * FROM {table_name} WHERE {key_name} = ?"
        
        try:
            cursor = conn.execute(sql_select, (id,))
            row = cursor.fetchone()
            if row:
                attributes = dict(zip([column[0] for column in cursor.description], row))
                return cls(**attributes)  
        except sqlite3.Error as e:
            print(f"Error al leer los datos: {e}")
        
        return None

    


    
    @staticmethod
    def leerTodos(cls, conn):
        table_name = cls.__name__
        sql_select_all = f"SELECT * FROM {table_name}"
        cursor = conn.execute(sql_select_all)
        rows = cursor.fetchall()

        # Obtener nombres de las columnas
        columnas = [column[0] for column in cursor.description]

        # Crear una lista de diccionarios
        resultados = []
        for row in rows:
            resultado = dict(zip(columnas, row))
            resultados.append(resultado)

        return resultados


    @staticmethod
    def actualizar(instance, conn):
        cls = instance.__class__
        table_name = cls.__name__
        attributes = vars(instance)
        key_name = [key for key in attributes.keys() if key.startswith('id')][0]
        keys = ", ".join(f"{key} = ?" for key in attributes if key != key_name)
        values = tuple(attributes[key] for key in attributes if key != key_name)
        sql_update = f"UPDATE {table_name} SET {keys} WHERE {key_name} = ?"
        conn.execute(sql_update, values + (getattr(instance, key_name),))
        conn.commit()

    @staticmethod
    def eliminar(cls, conn, id):
        table_name = cls.__name__
        key_name = [key for key in vars(cls()).keys() if key.startswith('id')][0]
        sql_delete = f"DELETE FROM {table_name} WHERE {key_name} = ?"
        conn.execute(sql_delete, (id,))
        conn.commit()        
    
    @staticmethod
    def buscar_generico(cls, conn, criterio_busqueda):
        table_name = cls.__name__
        sql_select_all = f"SELECT * FROM {table_name} WHERE "
        
        # Obtener nombres de las columnas de la tabla
        cursor = conn.execute(f"PRAGMA table_info({table_name})")
        columnas = [column[1] for column in cursor.fetchall()]
        
        # Crear la parte WHERE de la consulta dinámicamente
        conditions = []
        for columna in columnas:
            conditions.append(f"{columna} LIKE ?")
        
        sql_select_all += " OR ".join(conditions)
        
        # Parámetros para el cursor.execute
        params = tuple(f"%{criterio_busqueda}%" for _ in conditions)
        
        cursor = conn.execute(sql_select_all, params)
        rows = cursor.fetchall()

        # Obtener nombres de las columnas
        columnas = [column[0] for column in cursor.description]

        # Crear una lista de diccionarios
        resultados = []
        for row in rows:
            resultado = dict(zip(columnas, row))
            resultados.append(resultado)

        return resultados