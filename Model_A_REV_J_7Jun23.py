# Form implementation generated from reading ui file 'Model_A.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import sqlite3
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1078, 763)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_m = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_m.setGeometry(QtCore.QRect(10, 10, 431, 298))
        self.groupBox_m.setObjectName("groupBox_m")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_m)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_m_add = QtWidgets.QPushButton(parent=self.groupBox_m)
        self.pushButton_m_add.setObjectName("pushButton_m_add")

        # Connect signal
        self.pushButton_m_add.clicked.connect(self.add_row)
        self.horizontalLayout.addWidget(self.pushButton_m_add)

        self.pushButton_m_ddt = QtWidgets.QPushButton(parent=self.groupBox_m)
        self.pushButton_m_ddt.setObjectName("pushButton_m_ddt")
        self.pushButton_m_ddt.setStyleSheet("color: red")

        # Connect signal
        self.pushButton_m_ddt.clicked.connect(self.ddt_row)
        self.horizontalLayout.addWidget(self.pushButton_m_ddt)

        self.pushButton_m_del = QtWidgets.QPushButton(parent=self.groupBox_m)
        self.pushButton_m_del.setObjectName("pushButton_m_del")

        # Connect signal
        self.pushButton_m_del.clicked.connect(self.delete_row)

        self.horizontalLayout.addWidget(self.pushButton_m_del)
        self.pushButton_m_sqr = QtWidgets.QPushButton(parent=self.groupBox_m)
        self.pushButton_m_sqr.setObjectName("pushButton_m_sqr")

        # Connect signal
        self.pushButton_m_sqr.clicked.connect(self.square)

        self.horizontalLayout.addWidget(self.pushButton_m_sqr)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget_m = QtWidgets.QTableWidget(parent=self.groupBox_m)
        self.tableWidget_m.setObjectName("tableWidget_m")

        # Alternate the colors of the rows for better User Experience (UX)
        self.tableWidget_m.setAlternatingRowColors(True)

        self.tableWidget_m.setColumnCount(6)
        self.tableWidget_m.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_m.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_m.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_m.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_m.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_m.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_m.setHorizontalHeaderItem(5, item)
        self.verticalLayout.addWidget(self.tableWidget_m)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_m_clear = QtWidgets.QPushButton(parent=self.groupBox_m)
        self.pushButton_m_clear.setObjectName("pushButton_m_clear")

        # Connect signal
        self.pushButton_m_clear.clicked.connect(self.clear_table)

        self.horizontalLayout_3.addWidget(self.pushButton_m_clear)
        self.pushButton_m_insert = QtWidgets.QPushButton(parent=self.groupBox_m)
        self.pushButton_m_insert.setObjectName("pushButton_m_insert")

        # Connect signals
        self.pushButton_m_insert.clicked.connect(self.save_table_data)
        self.pushButton_m_insert.clicked.connect(self.load_table_data)

        self.horizontalLayout_3.addWidget(self.pushButton_m_insert)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(450, 10, 621, 711))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_print = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_print.setObjectName("pushButton_print")
        self.horizontalLayout_2.addWidget(self.pushButton_print)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tableWidget_takeOff = QtWidgets.QTableWidget(parent=self.groupBox)
        self.tableWidget_takeOff.setObjectName("tableWidget_takeOff")
        self.tableWidget_takeOff.setColumnCount(6)
        self.tableWidget_takeOff.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_takeOff.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_takeOff.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_takeOff.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_takeOff.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_takeOff.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_takeOff.setHorizontalHeaderItem(5, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget_takeOff.setHorizontalHeaderItem(6, item)
        self.verticalLayout_2.addWidget(self.tableWidget_takeOff)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1078, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def add_row(self):
        current_row = self.tableWidget_m.currentRow()  # Get the current row index

        unit_m = "m"  # Set the unit
        unit_m_cell = QtWidgets.QTableWidgetItem(unit_m)

        new_row = self.tableWidget_m.rowCount()  # Insert one new row at the end of the table
        self.tableWidget_m.insertRow(new_row)

        flags = unit_m_cell.flags()  # Freeze cell
        flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable  # set the cell as read-only
        flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable  # disable cell selection
        unit_m_cell.setFlags(flags)

        self.tableWidget_m.setItem(0, 4, unit_m_cell)  # set the unit

        # Copy the formatting and logic from the previous row to the new row
        for column in range(self.tableWidget_m.columnCount()):
            item = self.tableWidget_m.item(current_row, column)
            if item is not None:
                new_item = QtWidgets.QTableWidgetItem(item.text())
                flags = item.flags()
                new_item.setFlags(flags)
                self.tableWidget_m.setItem(new_row, column, new_item)

    def add_row(self):
        current_row = self.tableWidget_m.currentRow()  # Get the current row index

        unit_m = "m"  # Set the unit
        unit_m_cell = QtWidgets.QTableWidgetItem(unit_m)

        new_row = self.tableWidget_m.rowCount()  # Insert one new row at the end of the table
        self.tableWidget_m.insertRow(new_row)

        flags = unit_m_cell.flags()  # Freeze cell
        flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable  # set the cell as read-only
        flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable  # disable cell selection
        unit_m_cell.setFlags(flags)

        self.tableWidget_m.setItem(0, 4, unit_m_cell)  # set the unit

        # Copy the formatting and logic from the previous row to the new row
        for column in range(self.tableWidget_m.columnCount()):
            item = self.tableWidget_m.item(current_row, column)
            if item is not None:
                new_item = QtWidgets.QTableWidgetItem(item.text())
                flags = item.flags()
                new_item.setFlags(flags)
                self.tableWidget_m.setItem(new_row, column, new_item)

    def ddt_row(self):
        current_row = self.tableWidget_m.rowCount() - 1  # Get the current row index

        unit_m = "m"  # Set the unit
        unit_m_cell = QtWidgets.QTableWidgetItem(unit_m)
        unit_m_cell.setForeground(QtGui.QColor("red"))  # Set the text color to red

        new_row = self.tableWidget_m.rowCount()  # Insert one new row at the end of the table
        self.tableWidget_m.insertRow(new_row)

        flags = unit_m_cell.flags()  # Freeze cell
        flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable  # set the cell as read-only
        flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable  # disable cell selection
        unit_m_cell.setFlags(flags)

        self.tableWidget_m.setItem(new_row, 4, unit_m_cell)  # set the unit

        # Copy the formatting and logic from the previous row to the new row
        for column in range(self.tableWidget_m.columnCount()):
            item = self.tableWidget_m.item(current_row, column)
            if item is not None:
                new_item = QtWidgets.QTableWidgetItem(item.text())
                new_item.setForeground(QtGui.QColor("red"))  # Set the text color to red
                flags = item.flags()
                new_item.setFlags(flags)

                # Check if the current column is the square cell (column index 3)
                if column == 3:
                    # Convert the value to a negative number
                    value = float(new_item.text())
                    formatted_value = "{:,.2f}".format(-value)  # Format the value with pattern "{:,.2f}"
                    new_item.setText(formatted_value)

                self.tableWidget_m.setItem(new_row, column, new_item)

    def delete_row(self):
        current_row = self.tableWidget_m.currentRow()
        self.tableWidget_m.removeRow(current_row)

    def square(self):
        try:
            for row in range(self.tableWidget_m.rowCount()):
                times_item = self.tableWidget_m.item(row, 1)
                times_value = times_item.text()

                # Check if times value is empty
                if times_value.strip() == "":
                    times_item.setText("1.00 /")  # Set default value of "1.00 /"
                else:
                    times = float(times_value.rstrip(" /"))
                    times_item.setText("{:,.2f} /".format(times))

                dims_item = self.tableWidget_m.item(row, 2)
                dims = float(dims_item.text())
                dims_item.setText("{:,.2f}".format(dims))

                # Calculate square
                square = round(times * dims, 2)
                item = QtWidgets.QTableWidgetItem("{:,.2f}".format(square))

                # Freeze the cell
                flags = item.flags()
                flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable
                flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable
                item.setFlags(flags)

                # Set the square for row and col
                self.tableWidget_m.setItem(row, 3, item)

            # Add a new row at the end
            last_row = self.tableWidget_m.rowCount()
            self.tableWidget_m.insertRow(last_row)

            # Set unit column as 'm' for the last row
            unit_item = QtWidgets.QTableWidgetItem("m")
            flags = unit_item.flags()
            flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable
            flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable
            unit_item.setFlags(flags)
            self.tableWidget_m.setItem(last_row, 4, unit_item)

            # Set description column as 'sum' for the last row
            desc_item = QtWidgets.QTableWidgetItem("sum")
            flags = desc_item.flags()
            flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable
            flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable
            desc_item.setFlags(flags)
            self.tableWidget_m.setItem(last_row, 5, desc_item)

            # Sum the numbers in the square column
            total_square = 0.0
            for row in range(self.tableWidget_m.rowCount() - 1):
                square_item = self.tableWidget_m.item(row, 3)
                square_value = square_item.text().replace(",", "")
                total_square += float(square_value)

            # Set the total square in the last row's square column
            total_item = QtWidgets.QTableWidgetItem("{:,.2f}".format(total_square))
            flags = total_item.flags()
            flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable
            flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable
            total_item.setFlags(flags)
            self.tableWidget_m.setItem(last_row, 3, total_item)

        except ValueError:
            return
        except AttributeError:
            return
        except UnboundLocalError:
            return

    def clear_table(self):
        self.tableWidget_m.clearContents()
        self.tableWidget_m.setRowCount(0)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_m.setTitle(_translate("MainWindow", "m"))
        self.pushButton_m_add.setText(_translate("MainWindow", "Add"))
        self.pushButton_m_ddt.setText(_translate("MainWindow", "Ddt"))
        self.pushButton_m_del.setText(_translate("MainWindow", "Del"))
        self.pushButton_m_sqr.setText(_translate("MainWindow", "Sqr"))
        item = self.tableWidget_m.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "code"))
        self.tableWidget_m.setColumnWidth(0, 60)
        item = self.tableWidget_m.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "times"))
        self.tableWidget_m.setColumnWidth(1, 60)
        item = self.tableWidget_m.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "dims"))
        self.tableWidget_m.setColumnWidth(2, 60)
        item = self.tableWidget_m.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "square"))
        self.tableWidget_m.setColumnWidth(3, 60)
        item = self.tableWidget_m.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "unit"))
        self.tableWidget_m.setColumnWidth(4, 30)
        item = self.tableWidget_m.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "description"))
        self.tableWidget_m.setColumnWidth(5, 160)
        self.pushButton_m_clear.setText(_translate("MainWindow", "Clear"))
        self.pushButton_m_insert.setText(_translate("MainWindow", "Insert"))
        self.groupBox.setTitle(_translate("MainWindow", "Take Off"))
        self.pushButton.setText(_translate("MainWindow", "Abstract"))
        self.pushButton_print.setText(_translate("MainWindow", "Print"))

        item = self.tableWidget_takeOff.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "code"))
        self.tableWidget_takeOff.setColumnWidth(0, 60)
        item = self.tableWidget_takeOff.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "times"))
        self.tableWidget_takeOff.setColumnWidth(1, 60)
        item = self.tableWidget_takeOff.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "dims"))
        self.tableWidget_takeOff.setColumnWidth(2, 60)
        item = self.tableWidget_takeOff.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "square"))
        self.tableWidget_takeOff.setColumnWidth(3, 60)
        # item = self.tableWidget_takeOff.horizontalHeaderItem(4)
        # item.setText(_translate("MainWindow", "sum"))
        # self.tableWidget_takeOff.setColumnWidth(4, 60)
        item = self.tableWidget_takeOff.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "unit"))
        self.tableWidget_takeOff.setColumnWidth(4, 30)
        item = self.tableWidget_takeOff.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "description"))
        self.tableWidget_takeOff.setColumnWidth(5, 300)

    def save_table_data(self):
        # Connect to the SQLite database
        conn = sqlite3.connect('m_data.db')
        cursor = conn.cursor()

        # Create the table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS m_table_data (
                id     INTEGER PRIMARY KEY AUTOINCREMENT,
                code   TEXT,
                times  TEXT,
                dims   TEXT,
                square INTEGER,
                unit   TEXT,
                desc TEXT
            )
        ''')

        # Clear existing data from the table
        cursor.execute('DELETE FROM m_table_data')

        # Get the number of rows and columns in the table widget
        num_rows = self.tableWidget_m.rowCount()
        num_columns = self.tableWidget_m.columnCount()

        # Iterate over each row in the table widget and insert the data into the database
        for row in range(num_rows):
            data = []
            for col in range(num_columns):
                item = self.tableWidget_m.item(row, col)
                if item is not None:
                    data.append(item.text())
                else:
                    data.append('')

            # Insert the row data into the database
            cursor.execute('''
                INSERT INTO m_table_data (id, code, times, dims, square, unit, desc)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (row + 1,) + tuple(data))

        # Commit the changes and close the database connection
        conn.commit()
        conn.close()

    def load_table_data(self):
        # Connect to the SQLite database
        conn = sqlite3.connect('m_data.db')
        cursor = conn.cursor()

        # Retrieve the data from the m_table_data table
        cursor.execute('SELECT * FROM m_table_data')
        data = cursor.fetchall()

        # Close the database connection
        conn.close()

        # Check if the data list is empty
        if not data:
            return

        # Set the number of rows and columns in the QTableWidget
        self.tableWidget_takeOff.setRowCount(len(data))
        self.tableWidget_takeOff.setColumnCount(len(data[0]) - 1)  # Exclude ID

        # Populate the QTableWidget with the retrieved data
        for row_num, row_data in enumerate(data):
            for col_num, col_data in enumerate(row_data):
                if col_num == 0:  # Exclude ID column
                    continue

                item = QtWidgets.QTableWidgetItem()

                if col_num == 4:  # Assuming "square" column is at index 4
                    try:
                        formatted_value = '{:,.2f}'.format(float(col_data))
                    except ValueError:
                        formatted_value = str(col_data)
                    item.setText(formatted_value)
                else:
                    item.setText(str(col_data))

                self.tableWidget_takeOff.setItem(row_num, col_num - 1, item)  # Adjust column index


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
