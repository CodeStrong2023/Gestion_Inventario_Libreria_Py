

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
        key_name = [key for key in vars(cls()).keys() if key.startswith('id')][0]
        sql_select = f"SELECT * FROM {table_name} WHERE {key_name} = ?"
        cursor = conn.execute(sql_select, (id,))
        row = cursor.fetchone()
        if row:
            return cls(**dict(zip([column[0] for column in cursor.description], row)))
        return None
    
    @staticmethod
    def leerTodos(cls, conn):
        table_name = cls.__name__
        sql_select_all = f"SELECT * FROM {table_name}"
        cursor = conn.execute(sql_select_all)
        rows = cursor.fetchall()
        instances = []
        for row in rows:
            instance = cls(**dict(zip([column[0] for column in cursor.description], row)))
            instances.append(instance)

        # Formato deseado: {(idRol=26, rol='Prueba'), (idRol=26, rol='Prueba')}
        result = "{" + ", ".join(str(tuple(instance.__dict__.items())) for instance in instances) + "}"
        return result

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