def decimal_to_hexa(decimal):
    num = decimal
    count = str(decimal)
    hexa = " "
    c = len(count)
    while c != 0:
        resto = num%16
        r = str(resto)
        num = int(num//16)
        if resto >= 10:
            if r == '10':
                r = 'A'
            if r == '11':
                r = 'B'
            if r == '12':
                r = 'C'
            if r  == '13':
                r = 'D'
            if r == '14':
                r = 'E'
            if r == '15':
                r = 'F'
        if num == 0:
            c = 1
        hexa += r
    result = hexa[::-1]
    return result