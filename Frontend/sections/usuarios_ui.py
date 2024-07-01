from PyQt6 import QtCore, QtGui, QtWidgets
from Frontend.components.widget import Widget
from Frontend.components.boton import boton
from Frontend.components.tabla import tabla
from Frontend.components.input_text import inputText
from Frontend.components.label import label
from Frontend.components.frame import frame

from Backend.services.service_usuario import UsuarioService
from Backend.services.service_direccion import DireccionService
from Backend.services.service_rol import RolService
from unidecode import unidecode
from PyQt6.QtWidgets import QTableWidgetItem, QPushButton

class Ui_FormUsuarios(object):
    def __init__(self, conn):
            self.conn = conn
            self.entidad_service = UsuarioService(conn)
            self.direccion_service = DireccionService(conn)
            self.rol_service = RolService(conn)
    
#metodos de entidad principal
            
    def definir_modelo(self, entidad, direccion, rol):
        modelo = [
            (str(entidad['idUsuario'])),
            (entidad['nombre']),
            (entidad['apellido']),
            (entidad['correo']),
            (entidad['telefono']),
            (entidad['fechaNacimiento']),
            (str(direccion.idDireccion)),
            (str(rol.idRol))
        ]
        
        return modelo
    def definir_modelo_carga(self, entidad, rol, direccion, pais , ciudad):
        
        modelo = [(str(entidad['idUsuario'])),
            (entidad['nombre']),
            (entidad['apellido']),
            (entidad['correo']),
            (entidad['telefono']),
            (entidad['fechaNacimiento']),
            (pais.nombre),
            (ciudad.nombre),
            (direccion.calle),
            (str(direccion.numero)),
            (str(rol))
        ]
        
        return modelo
    
    def entidad_buscar_todos(self):
        resultado = self.entidad_service.buscar_usuarios()
        return resultado
    
    def entidad_buscar_generico(self, criterio_busqueda):
        resultado = self.entidad_service.buscar_usuarios_generico(criterio_busqueda)
        return resultado
    
    def entidad_buscar_por_id(self, entidad_id):
        resultado = self.entidad_service.buscar_usuario(entidad_id)
        return resultado
    
    def entidad_crear(self, valores, direccion_id, rol_id):
        resultado = self.entidad_service.crear_usuario(valores["nombre"], valores["apellido"], valores["correo"], valores["telefono"], valores["fechaNacimiento"], direccion_id, rol_id)        
        return resultado
    
    def entidad_actualizar(self, idEntidad, valores, direccion_id, rol_id):
        resultado = self.entidad_service.actualizar_usuario(idEntidad, valores["nombre"], valores["apellido"], valores["correo"], valores["telefono"], valores["fechaNacimiento"], direccion_id, rol_id)
        return resultado
    
    def entidad_eliminar(self, entidad_id):
        resultado = self.entidad_service.eliminar_usuario(entidad_id)
        return resultado      
            
        
    def setupUi(self, FormUsuarios, palette):
        self.formulario = FormUsuarios
        self.nombre_app = "Gestor de Biblioteca"
        self.nombre_tab = "USUARIOS"
        self.sing = "Usuario"
        self.plural = self.sing+"s"
        self.columnas = ["ID", "Nombre", "Apellido", "Correo", "Teléfono", "Fecha Nacimiento", "País", "Ciudad", "Calle", "Número", "Rol"]
        self.columnas.extend(["Actualizar", "Eliminar"])
        
        self.campos_a_mostrar = [ "Nombre", "Apellido", "Correo", "Teléfono", "Fecha Nacimiento", "País", "Ciudad", "Calle", "Número", "Rol"]
        
        self.formulario.setObjectName("Form")
        self.formulario.resize(901, 791)

        self.palette = palette
# Layout principal
        self.layout = QtWidgets.QVBoxLayout(self.formulario)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        # Frame principal
        self.espacio_principal = frame().frame(self.formulario, 0, 0, 0, 0, "background-color: " + self.palette.backgroundColor1 + ";",
                                              "espacio_principal")
        self.layout.addWidget(self.espacio_principal)

        espacio_layout = QtWidgets.QVBoxLayout(self.espacio_principal)

        # Label Layout (contiene el label_3 y los controles de búsqueda)
        label_layout = QtWidgets.QVBoxLayout()
        espacio_layout.addLayout(label_layout)

        self.label_3 = label().label(self.espacio_principal, 0, 0, 0, 0, "label_3")
        self.label_3.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\"; color:" + self.palette.darkTextColor + ";")
        label_layout.addWidget(self.label_3, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)

        # Top Layout (barra de búsqueda y botones)
        top_layout = QtWidgets.QHBoxLayout()
        label_layout.addLayout(top_layout)

        self.input_buscar_usuario = inputText().inputText(self.espacio_principal, 0, 0, 0, 0, "InputBuscarUsuario")
        self.input_buscar_usuario.setStyleSheet(
            "padding: 10px; font-weight: bold;" + "color: " + self.palette.darkTextColor + "; ")
        top_layout.addWidget(self.input_buscar_usuario)

        self.boton_buscar_empresa = boton().boton(self.espacio_principal,
                                                  "background-color: " + self.palette.primaryColor + "; padding: 10px; font-weight: bold;",
                                                  "Buscar  "+self.sing, 0, 0, 0, 0, "botonBuscarEmpresa")
        top_layout.addWidget(self.boton_buscar_empresa)

        #buscar haciendo enter
        self.input_buscar_usuario.returnPressed.connect(self.buscarEntidad)
        
        
        self.boton_crear_empresa_2 = boton().boton(self.espacio_principal,
                                                   "background-color: #03dac5;padding: 10px; color: #232f34; font-weight: bold;",
                                                   "Nuevo  "+self.sing, 0, 0, 0, 0, "botonCrearEmpresa_2")
        top_layout.addWidget(self.boton_crear_empresa_2)

        # Stacked Widget - pestañas
        self.stacked_widget = Widget().createStackedWidget(self.espacio_principal, 0, 0, 0, 0, "createStackedWidget_2")
        espacio_layout.addWidget(self.stacked_widget)

# Widget Principal - Tabla
        widget_principal_tabla = Widget().createWidget("widget_principal_tabla")
        self.stacked_widget.addWidget(widget_principal_tabla)

# Widget para crear
        self.widget_crear_nuevo = Widget().createWidget("widget_crear_nuevo")
        self.stacked_widget.addWidget(self.widget_crear_nuevo)
        
#  Widget para actualizar
        self.widget_actualizar = Widget().createWidget("widget_actualizar")
        self.stacked_widget.addWidget(self.widget_actualizar)
        
    
##  Principal - Tabla
    # Area de la Tabla
        area_tabla = frame().frame(widget_principal_tabla, 0, 0, 0, 0, "background-color: "+self.palette.lighBackgroundColor2+";", "area_tabla")
        
        buscar_usuarios_layout = QtWidgets.QVBoxLayout(widget_principal_tabla)
        
        buscar_usuarios_layout.addWidget(area_tabla)

    # Layout de la Tabla
        tabla_layout = QtWidgets.QVBoxLayout(area_tabla)
    #crear la tabla 
        self.tabla_usuarios = tabla().tabla(area_tabla, len(self.columnas), 0, 0, 0, 811, 591, "tabla_usuarios", self.columnas)
        self.tabla_usuarios.verticalHeader().setVisible(False)
        tabla_layout.addWidget(self.tabla_usuarios)
    
    
##  Crear Nuevo
        self.area_formulario_crear = frame().frame(self.widget_crear_nuevo, 0, 0, 0, 0, "background-color: " + self.palette.lighBackgroundColor2 + ";", "area_formulario_crear")
        self.widget_crear_nuevo.setLayout(QtWidgets.QVBoxLayout(self.widget_crear_nuevo))

        self.formulario_layout = QtWidgets.QFormLayout(self.area_formulario_crear)

        # Etiquetas y campos de entrada
        
        #recorrer campos_a_mostrar y crear los campos
        self.campos_texto = {}
        for campo in self.campos_a_mostrar:
            
            #Crear campo
                self.label_n = inputText().labelForm(campo, self.palette.darkTextColor)
                self.input_n = inputText().inputForm(self.area_formulario_crear, 180, 30, 60, 40, campo, self.palette.darkTextColor, self.palette.backgroundColor1, self.sing)
                    #Insertar campo
                self.formulario_layout.addRow(self.label_n, self.input_n)
                self.campos_texto[campo.lower()] = self.input_n
            
        

        # Botón Crear
        self.boton_crear_empresa_form = boton().boton(self.area_formulario_crear, "background-color: rgb(85, 255, 127); padding: 10px; color:"+self.palette.darkTextColor+"; font-weight: bold;", "Crear "+self.sing, 120, 400, 101, 41, "boton_crear_empresa_form")
        self.boton_crear_empresa_form.setFixedSize(150, 50)
        self.formulario_layout.addRow("", self.boton_crear_empresa_form)

        self.formulario_layout.setContentsMargins(250, 100, 250, 100)  

        # Asegúrate de que el layout del formulario se aplique correctamente al widget principal
        self.area_formulario_crear.setLayout(self.formulario_layout)

        # Agregar el área del formulario al layout principal del widget_crear_nuevo
        self.widget_crear_nuevo.layout().addWidget(self.area_formulario_crear)
        
        #boton de formulario de creacion
        self.boton_crear_empresa_form.clicked.connect(lambda: self.crearEntidad(self.campos_texto))


##  Actualizar

        ##  Actualizar
        self.area_formulario_actualizar = frame().frame(self.widget_actualizar, 0, 0, 0, 0, "background-color: " + self.palette.lighBackgroundColor2 + ";", "area_formulario_actualizar")
        self.widget_actualizar.setLayout(QtWidgets.QVBoxLayout(self.widget_actualizar))

        self.formulario_layout_act = QtWidgets.QFormLayout(self.area_formulario_actualizar)

        # Asegúrate de que el layout del formulario se aplique correctamente al widget principal
        self.area_formulario_actualizar.setLayout(self.formulario_layout_act)

        # Agregar el área del formulario al layout principal del widget_actualizar
        self.widget_actualizar.layout().addWidget(self.area_formulario_actualizar)


    # Conectar botones principales a funciones
        self.boton_buscar_empresa.clicked.connect(self.boton_buscar_entidad_clicked)
        self.boton_crear_empresa_2.clicked.connect(lambda: self.stacked_button_actions(1))
        
        


        
    # Llamar a retranslateUi
        self.retranslateUi(self.formulario, self.nombre_app, self.nombre_tab)
        QtCore.QMetaObject.connectSlotsByName(self.formulario)
    
    # Cargar empresas
        self.cargarEntidad()
        
    
    def retranslateUi(self, formulario, nombre_app, nombre_tab):
        _translate = QtCore.QCoreApplication.translate
        self.formulario = formulario
        _translate = QtCore.QCoreApplication.translate
        self.formulario.setWindowTitle(_translate("Form", nombre_app))
        self.label_3.setText(_translate("Form", nombre_tab))

#Funciones de vista
    def nuevaEntidad(self):
            self.stacked_widget.setCurrentIndex(1)  # Cambiar al formulario de nueva empresa

    def limpiar_formulario_nueva_entidad(self):
        # Aquí debes limpiar todos los campos del formulario de creación de empresa
        for campo, widget in self.campos_texto.items():
            widget.clear() 
            
    def boton_buscar_entidad_clicked(self):
        current_index = self.stacked_widget.currentIndex()

        if current_index == 0:
            self.buscarEntidad()  # Ejecutar la función buscarEmpresa si está en el índice 0
        else:
            self.stacked_widget.setCurrentIndex(0)  # Cambiar al índice 0 si está en cualquier otro índice

    
    
    def stacked_button_actions(self, index):
        if index == 0:
            # Acciones para stackedWidget(0)
            self.stacked_widget.setCurrentIndex(0)
        elif index == 1:
            # Acciones para stackedWidget(1)
            self.stacked_widget.setCurrentIndex(1)
            self.limpiar_formulario_nueva_entidad()
    
    def show_message(self, message, message_type):
        msg_box = QtWidgets.QMessageBox()
        if message_type == "success":
            msg_box.setIcon(QtWidgets.QMessageBox.Icon.Information)
        elif message_type == "error":
            msg_box.setIcon(QtWidgets.QMessageBox.Icon.Critical)
        msg_box.setText(message)
        msg_box.setWindowTitle("Mensaje")
        msg_box.exec()

    def actualizarTablaEntidades(self, entidades):
        # Limpiar la tabla antes de actualizar
        self.tabla_usuarios.clearContents()
        self.tabla_usuarios.setRowCount(len(entidades))
        
        # Iterar sobre las empresas y actualizar la tabla
        for row_idx, entidad in enumerate(entidades):
            direccion = self.direccion_service.buscar_direccion(entidad['Direccion_idDireccion'])
            ciudad = self.direccion_service.buscar_ciudad(direccion.Ciudad_idCiudad)
            pais = self.direccion_service.buscar_pais(ciudad.Pais_idPais)
            rol = self.rol_service.buscar_rol(entidad['Rol_idRol'])
            rol_id = rol.rol
            
            # Lista con los datos de la empresa y su dirección
            datos_entidad = self.definir_modelo_carga(entidad, rol_id, direccion, pais, ciudad, )
            
            
            # Iterar sobre los datos y asignarlos a las celdas correspondientes en la tabla
            for col_idx, dato in enumerate(datos_entidad):
                item = QTableWidgetItem(str(dato))
                self.tabla_usuarios.setItem(row_idx, col_idx, item)
            
            # Botón Actualizar
            btn_actualizar = QPushButton('Actualizar')
            btn_actualizar.setStyleSheet("background-color: #03dac5; padding: 5px; color: #232f34; font-weight: bold;")
            btn_actualizar.clicked.connect(lambda checked, idx=row_idx: self.ir_actualizar_entidad(idx))
            self.tabla_usuarios.setCellWidget(row_idx, len(datos_entidad), btn_actualizar)
            
            # Botón Eliminar
            btn_eliminar = QPushButton('Eliminar')
            btn_eliminar.setStyleSheet("background-color: #ff0000; padding: 5px; color: #232f34; font-weight: bold;")
            btn_eliminar.clicked.connect(lambda checked, idx=row_idx: self.eliminar_entidad(idx))
            self.tabla_usuarios.setCellWidget(row_idx, len(datos_entidad) + 1, btn_eliminar)
            
            # Ajustar la altura de la fila
            self.tabla_usuarios.setRowHeight(row_idx, 40)
        
        
        


#Funciones de servicio

    def buscarEntidad(self):
        # Implementa aquí la lógica para buscar empresas
        criterio_busqueda = self.input_buscar_usuario.text()
        
        entidad = self.entidad_buscar_generico(criterio_busqueda)
        self.actualizarTablaEntidades(entidad)
        
    
        
    def cargarEntidad(self):
        entidades = self.entidad_buscar_todos()
        self.tabla_usuarios.setRowCount(len(entidades))
        self.tabla_usuarios.setColumnCount(len(self.columnas))  # Asegúrate de que la tabla tenga el número correcto de columnas
        
        for row_idx, entidad in enumerate(entidades):
            direccion = self.direccion_service.buscar_direccion(entidad['Direccion_idDireccion'])
            ciudad = self.direccion_service.buscar_ciudad(direccion.Ciudad_idCiudad)
            pais = self.direccion_service.buscar_pais(ciudad.Pais_idPais)
            rol = self.rol_service.buscar_rol(entidad['Rol_idRol'])
            rol= rol.rol
            print("aca")
            print(rol)
            
            
            modelo = self.definir_modelo_carga(entidad, rol, direccion, pais , ciudad)
            
            #print(modelo)
            for col_idx, data in enumerate(modelo):
                self.tabla_usuarios.setItem(row_idx, col_idx, QTableWidgetItem(data))
            
            # Crear los botones y agregarlos a la celda correspondiente
            actualizar_btn = QPushButton('Actualizar')
            actualizar_btn.setStyleSheet("background-color: #03dac5; padding: 10px; color: #232f34; font-weight: bold;")
            actualizar_btn.clicked.connect(lambda checked, idx=row_idx: self.ir_actualizar_entidad(idx))
            self.tabla_usuarios.setCellWidget(row_idx, len(modelo), actualizar_btn)
            
            eliminar_btn = QPushButton('Eliminar')
            eliminar_btn.setStyleSheet("background-color: #ff0000; padding: 10px; color: #232f34; font-weight: bold;")
            eliminar_btn.clicked.connect(lambda checked, idx=row_idx: self.eliminar_entidad(idx))
            self.tabla_usuarios.setCellWidget(row_idx, len(modelo) + 1, eliminar_btn)
        
        # Ajustar el tamaño de las columnas
        
        
        self.tabla_usuarios.setStyleSheet(f"""
                                            QTableWidget {{
                                                color: {self.palette.darkTextColor};  /* Eliminar borde */
                                                border: none;  /* Eliminar borde de la tabla */
                                            }}
                                            QTableWidget::item {{
                                                border-right: 2px solid #fff;  
                                                border-bottom: 1px solid #fff;  /* Añadir borde inferior */
                                                text-align: center;  /* Alinear texto al centro */
                                            }}
                                            QHeaderView::section {{
                                                color:{self.palette.darkTextColor};  /* Color del texto */
                                                border-bottom: 3px solid #fff;  /* Añadir borde inferior */
                                                background-color: transparent;  /* Color de fondo */
                                                padding-bottom: 4px;  /* Espaciado inferior */
                                                font-size: 12pt;  /* Tamaño de la fuente */
                                            }}
                                        """)

        # Ajustar la altura de las filas
        for row_idx in range(len(entidades)):
            self.tabla_usuarios.setRowHeight(row_idx, 40)
        


    def eliminar_entidad(self, row_idx):
        entidad_id = self.tabla_usuarios.item(row_idx, 0).text()
        self.entidad_eliminar(entidad_id)
        self.cargarEntidad()
        print(f'Eliminar {entidad_id}')
    
    
        
    def ir_actualizar_entidad(self, row_idx):
        self.idEntidad = self.tabla_usuarios.item(row_idx, 0).text()
        self.stacked_widget.setCurrentIndex(2)
        
        # Obtener los datos de la empresa
        entidad_data = self.entidad_buscar_por_id(self.idEntidad)
        direccion = self.direccion_service.buscar_direccion(entidad_data.Direccion_idDireccion)
        ciudad = self.direccion_service.buscar_ciudad(direccion.Ciudad_idCiudad)
        pais = self.direccion_service.buscar_pais(ciudad.Pais_idPais)
        rol = self.rol_service.buscar_rol(entidad_data.Rol_idRol)
        rol_id = rol.idRol

        
        # Recorrer campos_a_mostrar y crear los campos
        self.campos_texto = {}
        for campo in self.campos_a_mostrar:
            
            if unidecode(campo.lower()) == "empresa":
                continue

            if unidecode(campo.lower()) == "logo":
                value = entidad_data.logoEmpresa
            elif unidecode(campo.lower()) == "capacidad":
                value = entidad_data.capacidadTotalM3
            elif unidecode(campo.lower()) == "uso":
                value = entidad_data.usoM3
            elif unidecode(campo.lower()) == "pais":
                value = pais.nombre
            elif unidecode(campo.lower()) == "ciudad":
                value = ciudad.nombre
            elif unidecode(campo.lower()) == "calle":
                value = direccion.calle
            elif unidecode(campo.lower()) == "numero":
                value = direccion.numero
            elif unidecode(campo.lower()) == "rol":
                value = entidad_data.Rol_idRol
            else:
                # Usar getattr para obtener el valor del atributo del objeto entidad_data
                value = getattr(entidad_data, unidecode(campo.lower()), "")

            
            self.label_n = inputText().labelForm(campo, self.palette.darkTextColor)

            # Convertir value a string si no lo es
            value_str = str(value) 

            # Crear campo
            
            if campo.lower() == "fecha nacimiento":
                self.input_n = QtWidgets.QDateEdit(self.area_formulario_actualizar)
                self.input_n.setDisplayFormat("yyyy-MM-dd")  # Configura el formato de la fecha
                self.input_n.setCalendarPopup(True)  # Habilita el calendario desplegable
                self.input_n.setDate(QtCore.QDate.fromString(value_str, "yyyy-MM-dd"))  # Establece la fecha inicial
                self.input_n.setStyleSheet("padding: 10px; font-weight: bold;" + "color: " + self.palette.darkTextColor + "; background-color: " + self.palette.backgroundColor1 + ";")
            else:
                self.input_n = inputText().inputForm(self.area_formulario_actualizar, 180, 30, 60, 20, campo, self.palette.darkTextColor, self.palette.backgroundColor1, self.sing, value_str, True)

            # Insertar campo
            self.formulario_layout_act.addRow(self.label_n, self.input_n)
            self.campos_texto[campo.lower()] = self.input_n

        # Botón Actualizar
        self.boton_act_entidad_form = boton().boton(self.area_formulario_actualizar, "background-color: rgb(85, 255, 127); padding: 10px; color:" + self.palette.darkTextColor + "; font-weight: bold;", "Actualizar "+self.sing, 120, 400, 101, 41, "boton_actualizar_empresa_form")
        self.boton_act_entidad_form.setFixedSize(150, 50)
        self.formulario_layout_act.addRow("", self.boton_act_entidad_form)

        self.formulario_layout_act.setContentsMargins(250, 100, 250, 100)

        # Conectar el botón de actualización a la función correspondiente
        self.boton_act_entidad_form.clicked.connect(lambda: self.actualizar_entidad(self.campos_texto))

        
        
    def confirmar_actualizacion(self, campos_texto):
        valores = {}

        # Iterar campos_texto para obtener los valores
        for campo, widget in campos_texto.items():
            valor = unidecode(widget.text()).lower()  # Obtener el texto del widget
            valores[campo] = valor
            
            

        try:
            direccion_id = self.direccion_service.devolver_direccion(valores["ciudad"], valores["pais"], valores["calle"], valores["numero"])
            rol_id = self.rol_service.buscar_rol(valores["rol"])
            
            self.entidad_actualizar(self.idEntidad, valores, direccion_id, rol_id)
            
            self.show_message("actualizada con éxito.", "success")
            self.stacked_widget.setCurrentIndex(0)
            self.cargarEntidad()
        except Exception as e:
            self.show_message(f"Error al actualizar : {str(e)}", "error")


    def devolver_direccion(self, ciudad, pais, calle, numero):
        print(f"Procesando dirección: Ciudad={ciudad}, País={pais}, Calle={calle}, Número={numero}")  # Añadir este mensaje de depuración
        id_pais = self.direccion_service.pais_existe(nombre_pais=pais)
        id_ciudad = self.direccion_service.ciudad_existe(nombre_ciudad=ciudad, idPais=id_pais)

        nueva_direccion = self.direccion_service.crear_direccion(
            calle=calle, numero=numero, descripcion="LEJOS",
            Ciudad_idCiudad=id_ciudad, Ciudad_Pais_idPais=id_pais
        )
        direccion_id = nueva_direccion.idDireccion

        return direccion_id

    def actualizar_entidad(self, campos_texto):
        valores = {}

        # Iterar campos_texto para obtener los valores
        for campo, widget in campos_texto.items():
            campo = unidecode(campo).lower()
            valor = widget.text()  # Obtener el texto del widget
            
            if campo=="pais":
                valores[campo] = widget.text().capitalize()
                id=self.direccion_service.pais_existe(valores[campo])
                valores[campo] = id
            elif campo=="ciudad":
                valores[campo] = widget.text().capitalize()
                id=self.direccion_service.ciudad_existe(valores[campo], valores["pais"])
                valores[campo] = id   
            elif campo == "fecha nacimiento":
                campo = "fechaNacimiento"
                valores[campo] = valor
            else:
                valores[campo] = valor
                # Obtener el texto del widget
                
        
        print("Valores a actualizar:", valores)  # Añadir este mensaje de depuración

        try:
            # Obtener el ID de la dirección usando el servicio correspondiente
            direccion_id = self.devolver_direccion(valores["ciudad"], valores["pais"], valores["calle"], valores["numero"])
            rol_id = self.rol_service.buscar_rol(valores["rol"])
            rol_id = rol_id.idRol

            print(f"Direccion ID: {direccion_id}, Rol ID: {rol_id}")  # Añadir este mensaje de depuración

            # Actualizar la empresa utilizando el servicio adecuado
            self.entidad_actualizar(self.idEntidad, valores, direccion_id, rol_id)

            # Mostrar un mensaje de éxito
            self.show_message("Actualizada con éxito.", "success")

            # Regresar al índice 0 del stacked widget y recargar las empresas
            self.stacked_widget.setCurrentIndex(0)
            self.cargarEntidad()
        except Exception as e:
            # Capturar y mostrar cualquier error ocurrido durante la actualización
            self.show_message(f"Error al actualizar : {str(e)}", "error")

    def crearEntidad(self, campos_texto):
        valores = {}
        
        #iterar campos_texto para obtener los valores
        for campo, widget in campos_texto.items():
            
            campo = unidecode(campo).lower()
            valor = widget.text()  # Obtener el texto del widget
            print(valor)
            if campo == "fecha nacimiento":
                campo = "fechaNacimiento"
            print(campo)
            valores[campo] = valor
            
        
        direccion_id = self.devolver_direccion(valores["ciudad"], valores["pais"], valores["calle"], valores["numero"])
        
        
        rol_id = self.rol_service.buscar_rol(valores["rol"])
        rol_id = rol_id.idRol
        
        self.entidad_crear(valores, direccion_id, rol_id)

        self.stacked_widget.setCurrentIndex(0)
        self.entidad_buscar_todos()
        self.cargarEntidad()
        
    
