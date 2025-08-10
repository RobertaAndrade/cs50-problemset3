# ISO 8601 norma internacional para a representação de datas e horas, formatado (YYYY-MM-DD)
# cs50: solicita ao user uma data (Anno Domini - BC), formatado mm/dd/yyyy or month D, YYYY.
# ----- imprime a mesma data no formato yyyy-mm-dd.

# dict.get: pega o valor da chave no dicionário se existir, se não retorna None ou um valor padrão se passar
# ex f"{var:02}": transforma número em str com pelo menos 2 dígitos, adicionando 0's na frente se necessário

meses = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    data = input("Data: ").strip()

    if "/" in data:
        date_slice = data.split("/")
        if len(date_slice) == 3: # verifica se tem 3 elemts
            mes, dia, ano = date_slice

            if mes.isdigit() and dia.isdigit() and ano.isdigit():
                mes = int(mes)
                dia = int(dia)
                ano = int(ano)
                if 1 <= mes <= 12 and 1 <= dia <= 31 and ano > 0:
                    print(f"{ano:04}-{mes:02}-{dia:02}")
                    break

    else:
        if "," not in data:
            continue

        try:
            date_slice = data.replace(",", "").split()
            if len(date_slice) == 3:
                mes_extenso, dia, ano = date_slice

                if mes_extenso in meses and dia.isdigit() and ano.isdigit():
                    mes = meses.index(mes_extenso) + 1 # p/ contar a partir de 1, não 0
                    dia = int(dia)
                    ano = int(ano)

                    if 1 <= dia <= 31 and ano > 0:
                        print(f"{ano:04}-{mes:02}-{dia:02}")
                        break
        except:
            pass
