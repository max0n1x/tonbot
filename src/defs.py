
#Перевод в человеческий вид
def price_to_human(count):
    centsStr = str(count)
    d, c = centsStr[:-2], centsStr[-2:]
    fix = ''
    if len(c) == 1:
        fix = 0
    if int(centsStr) > 99:
        return f'{d}.{c}'
    else:
        return f'0.{fix}{c}'