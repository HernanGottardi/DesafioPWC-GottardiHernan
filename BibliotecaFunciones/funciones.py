def dar_formato_row(row):
    return "${:,.2f}".format(row)

def conver_num_a_string(group):
    list = []
    for elemento in group:
        list.append(str(elemento))   
    return list

def conver_num_a_stringPrecio(group):
    list = []
    for elemento in group:
        list.append(dar_formato_row(elemento))
    return list