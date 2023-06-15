import sqlite3

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem

# Create the SQLite database connection
conn = sqlite3.connect("data.db")
cursor = conn.cursor()

# Create the table to store the table data
cursor.execute("CREATE TABLE IF NOT EXISTS table_data (id INTEGER PRIMARY KEY, data TEXT)")


def save_table_data(table_widget):
    cursor.execute("DELETE FROM table_data")  # Clear existing data
    for row in range(table_widget.rowCount()):
        for column in range(table_widget.columnCount()):
            item = table_widget.item(row, column)
            if item is not None:
                data = item.text()
                cursor.execute("INSERT INTO table_data (data) VALUES (?)", (data,))
    conn.commit()


def load_table_data(table_widget):
    table_widget.clearContents()
    cursor.execute("SELECT data FROM table_data")
    rows = cursor.fetchall()
    table_widget.setRowCount(len(rows))
    for row, data in enumerate(rows):
        item = QTableWidgetItem(data[0])
        item.setFlags(item.flags() | Qt.ItemFlag.ItemIsEditable)  # Set the item as editable
        table_widget.setItem(row, 0, item)


if __name__ == "__main__":
    app = QApplication([])

    # Main window
    main_window = QMainWindow()
    main_widget = QTableWidget()
    main_window.setCentralWidget(main_widget)

    # Source QTableWidget
    source_table = QTableWidget(3, 3)
    for row in range(source_table.rowCount()):
        for column in range(source_table.columnCount()):
            item = QTableWidgetItem(f"Data {row}-{column}")
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsEditable)  # Set the item as editable
            source_table.setItem(row, column, item)

    # Target QTableWidget
    target_table = QTableWidget()

    # Save data from source_table
    save_table_data(source_table)

    # Load data into target_table
    load_table_data(target_table)

    # Print the contents of target_table
    for row in range(target_table.rowCount()):
        for column in range(target_table.columnCount()):
            item = target_table.item(row, column)
            if item is not None:
                print(item.text())

    main_window.show()

    # Close the database connection
    conn.close()

    app.exec()
