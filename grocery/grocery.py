# solicita ao user uma "lista de compras", retornando a lista dos elementos citados enumerada com a quantidade digitada
# try... except EOFError: encerra o programa após pressionar Ctrl + d
# https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

# SORTED
# usada para ordenar elementos de um iterável(lista, tupla, str, itens de um dict) e retornar uma nova lista ordenada
# ----------- sempre retorna uma nova lista contendo os elementos ordenados. O iterável original permanece inalterado
# sorted(iterable, *, key=None, reverse=False)

compras = {}

while True:
    try:
        item = input().strip().lower()
    except EOFError:
        break

    if item == "":
        continue

    compras[item] = compras.get(item, 0) + 1

print()
for item in sorted(compras):
    print(f"{compras[item]} {item.upper()}")
