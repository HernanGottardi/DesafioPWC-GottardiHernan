# Se importan las librerías necesarias.
import pandas as pd  
from mailmerge import MailMerge 
# Módulo hecho por mi para guardar algunas funciones.
import BibliotecaFunciones.funciones as func  

# Se lee el archivo de Excel con los datos de los clientes.
df = pd.read_excel('datos\Datos Clientes.xlsx')

# Agrupo los datos por cada cliente.
grouped = df.groupby('Cliente')

template = "datos\BANCO ABC - Carta.docx"

# Voy a generar una carta personalizada para cada cliente.
for name, group in grouped:

    # Creo un objeto MailMerge con la plantilla de Word definida anteriormente.
    document = MailMerge(template)

    # Lista vacía para guardar los números de cuenta y saldos de cada cliente.
    numDeCuentaYSaldo = []

    # Utilizo para los argumento de Zip funciones traidas del Modulo agregado por mi.
    zipeado = zip(func.conver_num_a_string(group['N de Cuenta']), func.conver_num_a_stringPrecio(group['Saldo']))

    # Se recorre la tupla zipeada y se crea una cadena de texto para cada número de cuenta y saldo, guardandola en una lista.
    for n, s in zipeado:
        cadena = f"{n}{' '*30}{s}" 
        numDeCuentaYSaldo.append(cadena)

    # Se utiliza el objeto MailMerge para fusionar los datos del cliente, números de cuenta y saldos en la plantilla
    # Se utiliza '\n'.join para unir las cadenas de números de cuenta y saldos separadas por un salto de línea
    document.merge(Cliente=name, N_de_Cuenta='\n'.join(numDeCuentaYSaldo), Saldo='')

    # Se escribe la carta personalizada para cada cliente en un archivo de Word separado
    document.write(f"CartasGeneradas/{name}.docx")















