import sqlite3

def main():
    conn = sqlite3.connect('contacts.db')
    cur = conn.cursor()
    
    # Here, perform operations on the database.

    # Add the Phonebook table.
    cur.execute('''CREATE TABLE Entries (phone INTEGER NOT NULL PRIMARY KEY,
                                           name TEXT)''')

    while again != '5':

        # Add another?
        print ('1) Buscar persona:')
        print ('2) Agregar persona:')
        print ('3) Eliminar persona:')
        print ('4) Actualizar persona:')
        print ('5) Salir...')
        again = input('Seleccione la opcion? 1-5: ')    
    
        if (again==1):
            buscarPersona(cur)
            pass
        elif (again==2):

            pass
        elif (again==3):

            pass
        elif (again==4):

            pass

    # Commit the chan
    conn.commit()
    conn.close()

# Execute the main function.
if __name__ == '__main__':
    main()

def buscarPersona(cur):
    name = input ('Escribe el nombre a buscar: ')
    cur.execute('SELECT phone, name FROM Entries WHERE name like %' + name + '%')
    # Fetch the results of the SELECT statement.
    results = cur.fetchall()

    # Display the results.
    for row in results:
        print(f'{row[0]:30} {row[1]:>5}')