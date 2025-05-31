from PySide6.QtCore import Qt, QDateTime
from PySide6.QtWidgets import QMainWindow, QPushButton, QMessageBox, QTableWidgetItem, QDialog, QDateTimeEdit
from PySide6.QtGui import QIcon

from lib.static import LOGO_FILE, LOGO_XS_FILE
from ui.compiled.ui_testing2 import Ui_MainWindow

from lib.services.server import conectar_base_datos
from ui.compiled.ui_providerInputForm import Ui_providerAdd
from ui.compiled.ui_clientInputForm import Ui_Form
from ui.compiled.ui_productInputForm import Ui_Form as Producto
from ui.compiled.ui_SProvInputForm import Ui_Form as ProveedoresP
from ui.compiled.ui_CombInputForm import Ui_Form as Comb
from ui.compiled.ui_BaseInputForm import Ui_Form as Base
from ui.compiled.ui_PedInputForm import Ui_Form as Pedido
from ui.compiled.ui_PaqInputForm import Ui_Form as Paquete
import mysql.connector

class Product_ADD(QDialog, Producto):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Agregar Producto")
        self.btnOk.clicked.connect(self.acceptButton)
        self.btnCancel.clicked.connect(self.close)
        self.textDate.setDateTime(QDateTime.currentDateTime())
    
    def cancelButton(self):
        self.reject()

    def acceptButton(self):
        ayudaLista = [self.textName.toPlainText(), self.textLevel.toPlainText(), self.textType.toPlainText(), self.textDate.dateTime().toString("yyyy-MM-dd")]
        if not all(not item for item in ayudaLista):
            self.accept()
            self.close()
            return ayudaLista
        QMessageBox.warning(self, "Error", "Ingrese todos los datos")
        return

class Client_ADD(QDialog, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Agregar Cliente")
        self.btnOk.clicked.connect(self.acceptButton)
        self.btnCancel.clicked.connect(self.close)
    
    def cancelButton(self):
        self.reject()

    def acceptButton(self):
        ayudaLista = [self.textName.toPlainText(), self.textFlavor.toPlainText(), self.textHistory.toPlainText()]
        if not all(not item for item in ayudaLista):
            self.accept()
            self.close()
            return ayudaLista
        QMessageBox.warning(self, "Error", "Ingrese todos los datos")
        return

class Provider_ADD(QDialog, Ui_providerAdd):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Agregar proveedor")
        self.btnOk.clicked.connect(self.acceptButton)
        self.btnCancel.clicked.connect(self.close)
    
    def cancelButton(self):
        self.reject()

    def acceptButton(self):
        ayudaLista = [self.textName.toPlainText(), self.textContact.toPlainText(), self.textPhone.toPlainText(), self.textEmail.toPlainText(), self.textAddres.toPlainText()]
        if not all(not item for item in ayudaLista):
            self.accept()
            self.close()
            return ayudaLista
        QMessageBox.warning(self, "Error", "Ingrese todos los datos")
        return


class ProvP_ADD(QDialog, ProveedoresP):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Agregar Proveedor de sabores")
        self.btnOk.clicked.connect(self.acceptButton)
        self.btnCancel.clicked.connect(self.close)
        self.textCom.setDateTime(QDateTime.currentDateTime())
        self.dateLcomp.setDateTime(QDateTime.currentDateTime())
    
    def cancelButton(self):
        self.reject()

    def acceptButton(self):
        ayudaLista = [self.textFla.toPlainText(), self.textProv.toPlainText(), self.textPri.toPlainText(), self.textCom.dateTime().toString("yyyy-MM-dd"), self.textCant.toPlainText(), self.dateLcomp.dateTime().toString("yyyy-MM-dd hh:mm:ss")]
        if not all(not item for item in ayudaLista):
            self.accept()
            self.close()
            return ayudaLista
        QMessageBox.warning(self, "Error", "Ingrese todos los datos")
        return
class Comb_ADD(QDialog, Comb):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Agregar Combinacion")
        self.btnOk.clicked.connect(self.acceptButton)
        self.btnCancel.clicked.connect(self.close)
    
    def cancelButton(self):
        self.reject()

    def acceptButton(self):
        ayudaLista = [self.textBase.toPlainText(), self.textSab.toPlainText(), self.textCant.toPlainText()]
        if not all(not item for item in ayudaLista):
            self.accept()
            self.close()
            return ayudaLista
        QMessageBox.warning(self, "Error", "Ingrese todos los datos")
        return
class Base_ADD(QDialog, Base):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Agregar Chicle base")
        self.btnOk.clicked.connect(self.acceptButton)
        self.btnCancel.clicked.connect(self.close)
    
    def cancelButton(self):
        self.reject()

    def acceptButton(self):
        ayudaLista = [self.textTam.toPlainText(), self.textForm.toPlainText()]
        if not all(not item for item in ayudaLista):
            self.accept()
            self.close()
            return ayudaLista
        QMessageBox.warning(self, "Error", "Ingrese todos los datos")
        return
class Ped_ADD(QDialog, Pedido):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Agregar Pedido")
        self.btnOk.clicked.connect(self.acceptButton)
        self.btnCancel.clicked.connect(self.close)
    
    def cancelButton(self):
        self.reject()

    def acceptButton(self):
        ayudaLista = [self.textCli.toPlainText(), self.textPaq.toPlainText()]
        if not all(not item for item in ayudaLista):
            self.accept()
            self.close()
            return ayudaLista
        QMessageBox.warning(self, "Error", "Ingrese todos los datos")
        return
class Paq_ADD(QDialog, Paquete):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Agregar Paquete")
        self.btnOk.clicked.connect(self.acceptButton)
        self.btnCancel.clicked.connect(self.close)
    
    def cancelButton(self):
        self.reject()

    def acceptButton(self):
        ayudaLista = [self.textBase.toPlainText(), self.textSab.toPlainText()]
        if not all(not item for item in ayudaLista):
            self.accept()
            self.close()
            return ayudaLista
        QMessageBox.warning(self, "Error", "Ingrese todos los datos")
        return

class MainView(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        # * Windows
        self.login_view = None
       
        # * Config UI
        self.setupUi(self)
        self.setWindowTitle("Chicles") 
        self.setWindowIcon(QIcon(str(LOGO_XS_FILE)))

        # * Set initial state
        self.username = None
        self.initial_state()

        # * Connect Events
        self.btnProvider.clicked.connect(lambda: self.change_main_page(self.btnProvider, 0,))
        self.btnClient.clicked.connect(lambda: self.change_main_page(self.btnClient, 1,))
        self.btnProduct.clicked.connect(lambda: self.change_main_page(self.btnProduct, 2,))
        self.btnComb.clicked.connect(lambda: self.change_main_page(self.btnComb, 3,))
        self.btnSProv.clicked.connect(lambda: self.change_main_page(self.btnSProv, 4,))
        self.btnBase.clicked.connect(lambda: self.change_main_page(self.btnBase, 5,))
        self.btnPed.clicked.connect(lambda: self.change_main_page(self.btnPed, 6,))
        self.btnPaq.clicked.connect(lambda: self.change_main_page(self.btnPaq, 7,))

        self.btnClose.clicked.connect(self.close)
        self.btnLogOut.clicked.connect(self.logout)

        self.btnDeleteRow.clicked.connect(self.deleteSelected)
        self.btnUpdateRow.clicked.connect(self.updateData)
        self.btnAdd.clicked.connect(self.addNew)

    # getting of client
    def base_datos(self, table):
        conexion = conectar_base_datos()
        if conexion:
            try:
                mysqlcursor = conexion.cursor()
                mysqlcursor.execute(f"SELECT * FROM {table}")
                self.result = mysqlcursor.fetchall()
                conexion.close()
                return self.result
            except mysql.connector.Error as err:
                QMessageBox.warning(self, "Error", f"Error: {err}")
                return
    
    # query throw data
    def llenar_tablas_datos(self, tabla, QTableWidget):
        allClients = self.base_datos(tabla)
        if allClients:
            lenght = len(allClients)
            QTableWidget.setRowCount(lenght)
            fila = 0
            for item in allClients:
                for index in range(len(item)):
                    QTableWidget.setItem(fila, index, QTableWidgetItem(str(item[index])))
                fila += 1
        else:
            print(f"Error")
 
    # actions
    def deleteSelected(self):
        self.support = []
        if self.tableClient.selectedItems() or self.tableProvider.selectedItems() or self.tableProduct.selectedItems() or self.tableComb.selectedItems() or self.tableSProv.selectedItems() or self.tableBase.selectedItems() or self.tablePed.selectedItems() or self.tablePaq.selectedItems():
            rango = 0
            conexion = conectar_base_datos()
            if conexion:
                try:
                    mysqlcursor = conexion.cursor() 
                    current_view = self.stacked1Contenido.currentIndex()

                    # tabla de proveedores
                    if current_view == 0:
                        self.selected = self.tableProvider.selectedItems()
                        for item in self.selected:
                            self.support.insert(rango, item.text())
                            rango += 1
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Advertencia!")
                        self.boxNew.setText(f"Estas apunto de borrar los datos de: {str(self.support[1])}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "DELETE FROM proveedor WHERE ID_Proveedor = %s;"
                            mysqlcursor.execute(sql, (self.support[0],))
                            conexion.commit()
                            QMessageBox.warning(self, "Borrado!", "Dato borrado exitosamente")
                            self.llenar_tablas_datos("proveedor", self.tableProvider)

                    # tabla de clientes
                    if current_view == 1:
                        self.selected = self.tableClient.selectedItems()
                        for item in self.selected:
                            self.support.insert(rango, item.text())
                            rango += 1
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Advertencia!")
                        self.boxNew.setText(f"Estas apunto de borrar los datos de: {str(self.support[1])}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "DELETE FROM cliente WHERE ID_CLiente = %s;"
                            mysqlcursor.execute(sql, (self.support[0],))
                            conexion.commit()
                            QMessageBox.warning(self, "Borrado!", "Dato borrado exitosamente")
                            self.llenar_tablas_datos("cliente", self.tableClient)

                    # tabla de productos
                    if current_view == 2:
                        self.selected = self.tableProduct.selectedItems()
                        for item in self.selected:
                            self.support.insert(rango, item.text())
                            rango += 1
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Advertencia!")
                        self.boxNew.setText(f"Estas apunto de borrar los datos de: {str(self.support[1])}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "DELETE FROM polvosabor WHERE ID_Sabor = %s;"
                            mysqlcursor.execute(sql, (self.support[0],))
                            conexion.commit()
                            QMessageBox.warning(self, "Borrado!", "Dato borrado exitosamente")
                            self.llenar_tablas_datos("polvosabor", self.tableProduct)
                    # tabla de Combinaciones
                    if current_view == 3:
                        self.selected = self.tableComb.selectedItems()
                        for item in self.selected:
                            self.support.insert(rango, item.text())
                            rango += 1
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Advertencia!")
                        self.boxNew.setText(f"Estas apunto de borrar los datos de: {str(self.support[1])}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "DELETE FROM combinacionsabor WHERE ID_Combinacion = %s;"
                            mysqlcursor.execute(sql, (self.support[0],))
                            conexion.commit()
                            QMessageBox.warning(self, "Borrado!", "Dato borrado exitosamente")
                            self.llenar_tablas_datos("combinacionsabor", self.tableComb)
                    # tabla de proveedores por sabor
                    if current_view == 4:
                        self.selected = self.tableSProv.selectedItems()
                        for item in self.selected:
                            self.support.insert(rango, item.text())
                            rango += 1
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Advertencia!")
                        self.boxNew.setText(f"Estas apunto de borrar los datos de: {str(self.support[1])}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "DELETE FROM polvosabor_proveedor WHERE ID_Sabor = %s;"
                            mysqlcursor.execute(sql, (self.support[0],))
                            conexion.commit()
                            QMessageBox.warning(self, "Borrado!", "Dato borrado exitosamente")
                            self.llenar_tablas_datos("polvosabor_proveedor", self.tableSProv)
                    # tabla de chicles base
                    if current_view == 5:
                        self.selected = self.tableBase.selectedItems()
                        for item in self.selected:
                            self.support.insert(rango, item.text())
                            rango += 1
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Advertencia!")
                        self.boxNew.setText(f"Estas apunto de borrar los datos de: {str(self.support[1])}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "DELETE FROM chiclebase WHERE ID_BaseChicle = %s;"
                            mysqlcursor.execute(sql, (self.support[0],))
                            conexion.commit()
                            QMessageBox.warning(self, "Borrado!", "Dato borrado exitosamente")
                            self.llenar_tablas_datos("chiclebase", self.tableBase)
                    # tabla de pedidos
                    if current_view == 6:
                        self.selected = self.tablePed.selectedItems()
                        for item in self.selected:
                            self.support.insert(rango, item.text())
                            rango += 1
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Advertencia!")
                        self.boxNew.setText(f"Estas apunto de borrar los datos de: {str(self.support[1])}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "DELETE FROM pedidos WHERE pedidosid = %s;"
                            mysqlcursor.execute(sql, (self.support[0],))
                            conexion.commit()
                            QMessageBox.warning(self, "Borrado!", "Dato borrado exitosamente")
                            self.llenar_tablas_datos("pedidos", self.tablePed)
                    # tabla de paquetes
                    if current_view == 7:
                        self.selected = self.tablePaq.selectedItems()
                        for item in self.selected:
                            self.support.insert(rango, item.text())
                            rango += 1
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Advertencia!")
                        self.boxNew.setText(f"Estas apunto de borrar los datos de: {str(self.support[1])}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "DELETE FROM paqueteproducto WHERE ID_Paquete = %s;"
                            mysqlcursor.execute(sql, (self.support[0],))
                            conexion.commit()
                            QMessageBox.warning(self, "Borrado!", "Dato borrado exitosamente")
                            self.llenar_tablas_datos("paqueteproducto", self.tablePaq)
                            
                            

                except mysql.connector.Error as err:
                    QMessageBox.warning(self, "Error", f"Error: {err}")
                finally:
                    conexion.close()
        else:
            QMessageBox.warning(self, "Error", "No seleccionaste ningun dato a borrar")

    def updateData(self):
        # revisar que se haya seleccionado un dato
        if self.tableProvider.selectedItems() or self.tableClient.selectedItems() or self.tableProduct.selectedItems() or self.tableComb.selectedItems() or self.tableSProv.selectedItems() or self.tableBase.selectedItems() or self.tablePed.selectedItems() or self.tablePaq.selectedItems():
            index = self.stacked1Contenido.currentIndex()
            support = []
            rango = 0
            # editar tabla de proveedor
            if index == 0:
                self.selected = self.tableProvider.selectedItems()
                for item in self.selected:
                    support.insert(rango, item.text())
                    rango += 1
                # compararlos con los datos de la base de datos
                conexion = conectar_base_datos()
                try:
                    mysqlconexion = conexion.cursor()
                    # hacer la consulta 
                    sql = "SELECT * FROM proveedor WHERE ID_Proveedor = %s"
                    mysqlconexion.execute(sql, (support[0],))
                    respuesta_busqueda = mysqlconexion.fetchall()
                    # tenemos que volver el dato a entero
                    support[0] = int(support[0])
                    # comparar si se edito algun dato
                    if set(respuesta_busqueda[0]) == set(support):
                        QMessageBox.warning(self, "Error", "Ningun dato fue editado.")
                        return
                    else:
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Advertencia!")
                        self.boxNew.setText(f"Estas apunto de editar los datos seleccionados a: {str(support)}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "UPDATE proveedor SET Nombre = %s, Contacto = %s, Telefono = %s, Email = %s, Direccion = %s WHERE ID_Proveedor = %s;"
                            mysqlconexion.execute(sql, (support[1], support[2], support[3], support[4], support[5], support[0]))
                            conexion.commit()
                            QMessageBox.warning(self, "Actualizacion", "Datos editados exitosamente")
                            self.llenar_tablas_datos("proveedor", self.tableProvider)
                except mysql.connector.Error as err:
                    QMessageBox.warning(self, "Error", f"Error: {err}")
                finally:
                    conexion.close()

            # para la tabla clientes
            if index == 1:
                self.selected = self.tableClient.selectedItems()
                for item in self.selected:
                    support.insert(rango, item.text())
                    rango += 1
                # compararlos con los datos de la base de datos
                conexion = conectar_base_datos()
                try:
                    mysqlconexion = conexion.cursor()
                    # hacer la consulta 
                    sql = "SELECT * FROM cliente WHERE ID_Cliente = %s"
                    mysqlconexion.execute(sql, (support[0],))
                    respuesta_busqueda = mysqlconexion.fetchall()
                    # tenemos que volver el dato a entero
                    support[0] = int(support[0])
                    # comparar si se edito algun dato
                    if set(respuesta_busqueda[0]) == set(support):
                        QMessageBox.warning(self, "Error", "Ningun dato fue editado.")
                        return
                    else:
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Advertencia!")
                        self.boxNew.setText(f"Estas apunto de editar los datos seleccionados a: {str(support)}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "UPDATE cliente SET Nombre = %s, PreferenciasSabor = %s, HistorialCombinaciones = %s WHERE ID_Cliente = %s;"
                            mysqlconexion.execute(sql, (support[1], support[2], support[3], support[0]))
                            conexion.commit()
                            QMessageBox.warning(self, "Actualizacion", "Datos editados exitosamente")
                            self.llenar_tablas_datos("cliente", self.tableClient)
                except mysql.connector.Error as err:
                    QMessageBox.warning(self, "Error", f"Error: {err}")
                finally:
                    conexion.close()
            
            # para la tabla polvosabor
            if index == 2:
                self.selected = self.tableProduct.selectedItems()
                for item in self.selected:
                    support.insert(rango, item.text())
                    rango += 1
                # compararlos con los datos de la base de datos
                conexion = conectar_base_datos()
                try:
                    mysqlconexion = conexion.cursor()
                    # hacer la consulta 
                    sql = "SELECT * FROM polvosabor WHERE ID_Sabor = %s"
                    mysqlconexion.execute(sql, (support[0],))
                    respuesta_busqueda = mysqlconexion.fetchall()
                    # tenemos que volver el dato a entero
                    support[0] = int(support[0])
                    # comparar si se edito algun dato
                    if set(respuesta_busqueda[0]) == set(support):
                        QMessageBox.warning(self, "Error", "Ningun dato fue editado.")
                        return
                    else:
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Advertencia!")
                        self.boxNew.setText(f"Estas apunto de editar los datos seleccionados a: {str(support)}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "UPDATE polvosabor SET Nombre = %s, Intensidad = %s, Tipo = %s, FechaExpiración = %s WHERE ID_Sabor = %s;"
                            mysqlconexion.execute(sql, (support[1], support[2], support[3], support[4], support[0]))
                            conexion.commit()
                            QMessageBox.warning(self, "Actualizacion", "Datos editados exitosamente")
                            self.llenar_tablas_datos("polvosabor", self.tableProduct)
                except mysql.connector.Error as err:
                    QMessageBox.warning(self, "Error", f"Error: {err}")
                finally:
                    conexion.close()

            # para la tabla Combinacion
            if index == 3:
                self.selected = self.tableComb.selectedItems()
                for item in self.selected:
                    support.insert(rango, item.text())
                    rango += 1
                # compararlos con los datos de la base de datos
                conexion = conectar_base_datos()
                try:
                    mysqlconexion = conexion.cursor()
                    # hacer la consulta 
                    sql = "SELECT * FROM combinacionsabor WHERE ID_Combinacion = %s"
                    mysqlconexion.execute(sql, (support[0],))
                    respuesta_busqueda = mysqlconexion.fetchall()
                    # tenemos que volver el dato a entero
                    support[0] = int(support[0])
                    # comparar si se edito algun dato
                    if set(respuesta_busqueda[0]) == set(support):
                        QMessageBox.warning(self, "Error", "Ningun dato fue editado.")
                        return
                    else:
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Advertencia!")
                        self.boxNew.setText(f"Estas apunto de editar los datos seleccionados a: {str(support)}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "UPDATE combinacionsabor SET ID_BaseChicle = %s, ID_Sabor = %s, CantidadPolvos = %s WHERE ID_Combinacion = %s;"
                            mysqlconexion.execute(sql, (support[1], support[2], support[3], support[0]))
                            conexion.commit()
                            QMessageBox.warning(self, "Actualizacion", "Datos editados exitosamente")
                            self.llenar_tablas_datos("combinacionsabor", self.tableComb)
                except mysql.connector.Error as err:
                    QMessageBox.warning(self, "Error", f"Error: {err}")
                finally:
                    conexion.close()

            # para la tabla Proveedor sabores
            if index == 4:
                self.selected = self.tableSProv.selectedItems()
                for item in self.selected:
                    support.insert(rango, item.text())
                    rango += 1
                # compararlos con los datos de la base de datos
                conexion = conectar_base_datos()
                try:
                    mysqlconexion = conexion.cursor()
                    # hacer la consulta 
                    sql = "SELECT * FROM polvosabor_proveedor WHERE ID_Sabor = %s"
                    mysqlconexion.execute(sql, (support[0],))
                    respuesta_busqueda = mysqlconexion.fetchall()
                    # tenemos que volver el dato a entero
                    support[0] = int(support[0])
                    # comparar si se edito algun dato
                    if set(respuesta_busqueda[0]) == set(support):
                        QMessageBox.warning(self, "Error", "Ningun dato fue editado.")
                        return
                    else:
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Advertencia!")
                        self.boxNew.setText(f"Estas apunto de editar los datos seleccionados a: {str(support)}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "UPDATE polvosabor_proveedor SET ID_Sabor = %s, ID_Proveedor = %s, Precio = %s, FechaUltimaCompra = %s, cantidad_comprada = %s, ultima_fecha_de_compra = %s WHERE ID_Sabor = %s;"
                            mysqlconexion.execute(sql, (support[1], support[2], support[3], support[4], support[5], support[6], support[0]))
                            conexion.commit()
                            QMessageBox.warning(self, "Actualizacion", "Datos editados exitosamente")
                            self.llenar_tablas_datos("polvosabor_proveedor", self.tableSProv)
                except mysql.connector.Error as err:
                    QMessageBox.warning(self, "Error", f"Error: {err}")
                finally:
                    conexion.close()

            # para la tabla Bases
            if index == 5:
                self.selected = self.tableBase.selectedItems()
                for item in self.selected:
                    support.insert(rango, item.text())
                    rango += 1
                # compararlos con los datos de la base de datos
                conexion = conectar_base_datos()
                try:
                    mysqlconexion = conexion.cursor()
                    # hacer la consulta 
                    sql = "SELECT * FROM chiclebase WHERE ID_BaseChicle = %s"
                    mysqlconexion.execute(sql, (support[0],))
                    respuesta_busqueda = mysqlconexion.fetchall()
                    # tenemos que volver el dato a entero
                    support[0] = int(support[0])
                    # comparar si se edito algun dato
                    if set(respuesta_busqueda[0]) == set(support):
                        QMessageBox.warning(self, "Error", "Ningun dato fue editado.")
                        return
                    else:
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Advertencia!")
                        self.boxNew.setText(f"Estas apunto de editar los datos seleccionados a: {str(support)}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "UPDATE chiclebase SET Tamaño = %s, Fórmula = %s WHERE ID_BaseChicle = %s;"
                            mysqlconexion.execute(sql, (support[1], support[2], support[0]))
                            conexion.commit()
                            QMessageBox.warning(self, "Actualizacion", "Datos editados exitosamente")
                            self.llenar_tablas_datos("chiclebase", self.tableBase)
                except mysql.connector.Error as err:
                    QMessageBox.warning(self, "Error", f"Error: {err}")
                finally:
                    conexion.close()

            # para la tabla Pedidos
            if index == 6:
                self.selected = self.tablePed.selectedItems()
                for item in self.selected:
                    support.insert(rango, item.text())
                    rango += 1
                # compararlos con los datos de la base de datos
                conexion = conectar_base_datos()
                try:
                    mysqlconexion = conexion.cursor()
                    # hacer la consulta 
                    sql = "SELECT * FROM pedidos WHERE pedidosid = %s"
                    mysqlconexion.execute(sql, (support[0],))
                    respuesta_busqueda = mysqlconexion.fetchall()
                    # tenemos que volver el dato a entero
                    support[0] = int(support[0])
                    # comparar si se edito algun dato
                    if set(respuesta_busqueda[0]) == set(support):
                        QMessageBox.warning(self, "Error", "Ningun dato fue editado.")
                        return
                    else:
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Advertencia!")
                        self.boxNew.setText(f"Estas apunto de editar los datos seleccionados a: {str(support)}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "UPDATE pedidos SET ID_Cliente = %s, ID_Paquete = %s WHERE pedidosid = %s;"
                            mysqlconexion.execute(sql, (support[1], support[2], support[0]))
                            conexion.commit()
                            QMessageBox.warning(self, "Actualizacion", "Datos editados exitosamente")
                            self.llenar_tablas_datos("pedidos", self.tablePed)
                except mysql.connector.Error as err:
                    QMessageBox.warning(self, "Error", f"Error: {err}")
                finally:
                    conexion.close()

            # para la tabla Paquetes
            if index == 7:
                self.selected = self.tablePaq.selectedItems()
                for item in self.selected:
                    support.insert(rango, item.text())
                    rango += 1
                # compararlos con los datos de la base de datos
                conexion = conectar_base_datos()
                try:
                    mysqlconexion = conexion.cursor()
                    # hacer la consulta 
                    sql = "SELECT * FROM paqueteproducto WHERE ID_Paquete = %s"
                    mysqlconexion.execute(sql, (support[0],))
                    respuesta_busqueda = mysqlconexion.fetchall()
                    # tenemos que volver el dato a entero
                    support[0] = int(support[0])
                    # comparar si se edito algun dato
                    if set(respuesta_busqueda[0]) == set(support):
                        QMessageBox.warning(self, "Error", "Ningun dato fue editado.")
                        return
                    else:
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Advertencia!")
                        self.boxNew.setText(f"Estas apunto de editar los datos seleccionados a: {str(support)}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "UPDATE paqueteproducto SET ID_BaseChicle = %s, ID_Sabor = %s WHERE ID_Paquete = %s;"
                            mysqlconexion.execute(sql, (support[1], support[2], support[0]))
                            conexion.commit()
                            QMessageBox.warning(self, "Actualizacion", "Datos editados exitosamente")
                            self.llenar_tablas_datos("paqueteproducto", self.tablePaq)
                except mysql.connector.Error as err:
                    QMessageBox.warning(self, "Error", f"Error: {err}")
                finally:
                    conexion.close()
        else:
            QMessageBox.warning(self, "Error", "No hay datos a modificar")

    def addNew(self):
        conexion = conectar_base_datos()
        try:
            vista_actual = self.stacked1Contenido.currentIndex()
            mysqlconexion = conexion.cursor()
            # para la tabla de proveedores
            if vista_actual == 0:
                form = Provider_ADD()
                result = form.exec()
                if result:
                    response = form.acceptButton()
                    # se recibieron datos
                    sql = "INSERT INTO proveedor (Nombre,Contacto,Telefono,Email,Direccion) VALUES(%s, %s, %s, %s, %s)"
                    values = (response[0], response[1], response[2], response[3], response[4])
                    mysqlconexion.execute(sql, values)
                    conexion.commit()
                    QMessageBox.warning(self, "Exito", "Datos agregados con exito")
                    self.llenar_tablas_datos("proveedor", self.tableProvider)
            # para la tabla de clientes
            if vista_actual == 1:
                form = Client_ADD()
                result = form.exec()
                if result:
                    response = form.acceptButton()
                    # se recibieron datos
                    sql = "INSERT INTO cliente (Nombre,PreferenciasSabor,HistorialCombinaciones) VALUES(%s, %s, %s)"
                    values = (response[0], response[1], response[2])
                    mysqlconexion.execute(sql, values)
                    conexion.commit()
                    QMessageBox.warning(self, "Exito", "Datos agregados con exito")
                    self.llenar_tablas_datos("cliente", self.tableClient)
            # para la tabla de productos
            if vista_actual == 2:
                form = Product_ADD()
                result = form.exec()
                if result:
                    response = form.acceptButton()
                    # se recibieron datos
                    print(response)
                    sql = "INSERT INTO polvosabor (Nombre,Intensidad,Tipo,FechaExpiración) VALUES(%s, %s, %s, %s)"
                    values = (response[0], response[1], response[2], response[3])
                    mysqlconexion.execute(sql, values)
                    conexion.commit()
                    QMessageBox.warning(self, "Exito", "Datos agregados con exito")
                    self.llenar_tablas_datos("polvosabor", self.tableProduct)
            # para la tabla de combinaciones
            if vista_actual == 3:
                form = Comb_ADD()
                result = form.exec()
                if result:
                    response = form.acceptButton()
                    # se recibieron datos
                    sql = "INSERT INTO combinacionsabor (ID_BaseChicle,ID_Sabor,CantidadPolvos) VALUES(%s, %s, %s)"
                    values = (response[0], response[1], response[2])
                    mysqlconexion.execute(sql, values)
                    conexion.commit()
                    QMessageBox.warning(self, "Exito", "Datos agregados con exito")
                    self.llenar_tablas_datos("combinacionsabor", self.tableComb)
            # para la tabla de proveedores polvos
            if vista_actual == 4:
                form = ProvP_ADD()
                result = form.exec()
                if result:
                    response = form.acceptButton()
                    # se recibieron datos
                    print(response)
                    sql = "INSERT INTO polvosabor_proveedor (ID_Sabor,ID_Proveedor,Precio,FechaUltimaCompra,cantidad_comprada,ultima_fecha_de_compra) VALUES(%s, %s, %s, %s, %s, %s)"
                    values = (response[0], response[1], response[2], response[3], response[4], response[5])
                    mysqlconexion.execute(sql, values)
                    conexion.commit()
                    QMessageBox.warning(self, "Exito", "Datos agregados con exito")
                    self.llenar_tablas_datos("polvosabor_proveedor", self.tableSProv)
            # para la tabla de bases
            if vista_actual == 5:
                form = Base_ADD()
                result = form.exec()
                if result:
                    response = form.acceptButton()
                    # se recibieron datos
                    sql = "INSERT INTO chiclebase (Tamaño,Fórmula) VALUES(%s, %s)"
                    values = (response[0], response[1])
                    mysqlconexion.execute(sql, values)
                    conexion.commit()
                    QMessageBox.warning(self, "Exito", "Datos agregados con exito")
                    self.llenar_tablas_datos("chiclebase", self.tableBase)
            # para la tabla de pedidos
            if vista_actual == 6:
                form = Ped_ADD()
                result = form.exec()
                if result:
                    response = form.acceptButton()
                    # se recibieron datos
                    sql = "INSERT INTO pedidos (ID_Cliente,ID_Paquete) VALUES(%s, %s)"
                    values = (response[0], response[1])
                    mysqlconexion.execute(sql, values)
                    conexion.commit()
                    QMessageBox.warning(self, "Exito", "Datos agregados con exito")
                    self.llenar_tablas_datos("pedidos", self.tablePed)
            # para la tabla de paquete
            if vista_actual == 7:
                form = Paq_ADD()
                result = form.exec()
                if result:
                    response = form.acceptButton()
                    # se recibieron datos
                    sql = "INSERT INTO paqueteproducto (ID_BaseChicle,ID_Sabor) VALUES(%s, %s)"
                    values = (response[0], response[1])
                    mysqlconexion.execute(sql, values)
                    conexion.commit()
                    QMessageBox.warning(self, "Exito", "Datos agregados con exito")
                    self.llenar_tablas_datos("paqueteproducto", self.tablePaq)
        except mysql.connector.Error as err:
            QMessageBox.warning(self, "Error",f"Error: {err}")
        finally:
            conexion.close()

    # valor inicial de la vista
    def initial_state(self):
        """ Set initial state for the window """
        self.lbCompany.setText("Chicles")
        self.lbUser.setText(self.username if self.username is not None else "USER")
        self.stacked1Contenido.setCurrentIndex(0)
        for btn_nav in self.findChildren(QPushButton): btn_nav.setChecked(False)

        self.llenar_tablas_datos("proveedor", self.tableProvider)
        for table in [
        self.tableProvider, self.tableClient, self.tableProduct,
        self.tableComb, self.tableSProv, self.tableBase,
        self.tablePed, self.tablePaq
        ]:
            table.setSortingEnabled(True)


    # cuando escucha que vista fue cambiada
    def change_main_page(self, pressed_btn_nav, stack1_index):
        # * Alternate state for each btnNav button
        for btn_nav in self.findChildren(QPushButton): btn_nav.setChecked(False)
        pressed_btn_nav.setChecked(True)
        # * Set active the selected page
        self.stacked1Contenido.setCurrentIndex(stack1_index)
        # load data from the first table
        if stack1_index == 0:
            self.llenar_tablas_datos("proveedor", self.tableProvider)
        if stack1_index == 1:
            self.llenar_tablas_datos("cliente", self.tableClient)
        if stack1_index == 2:
            self.llenar_tablas_datos("polvosabor", self.tableProduct)
        if stack1_index == 3:
            self.llenar_tablas_datos("combinacionsabor", self.tableComb)
        if stack1_index == 4:
            self.llenar_tablas_datos("polvosabor_proveedor", self.tableSProv)
        if stack1_index == 5:
            self.llenar_tablas_datos("chiclebase", self.tableBase)
        if stack1_index == 6:
            self.llenar_tablas_datos("pedidos", self.tablePed)
        if stack1_index == 7:
            self.llenar_tablas_datos("paqueteproducto", self.tablePaq)

            
    def logout(self):
        self.login_view.initial_state()
        self.login_view.show()
        self.close()
