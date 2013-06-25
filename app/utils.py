import unicodedata
import re

BMP_MAX = 0xFFFF  # Unicode Basic Multilingual Plane
LATIN_CHAR_NAME = re.compile(r'(LATIN \w+ LETTER \w) WITH')

def mapear_latinos():
    mapa = {}
    for i in range(BMP_MAX):
        c = chr(i)
        try:
            nome = unicodedata.name(c)
        except ValueError:
            continue
        padrao = LATIN_CHAR_NAME.match(nome)
        if padrao:
            c_latino = unicodedata.lookup(padrao.group(1))
            mapa[c] = c_latino
    return mapa

MAPA_LATINOS = mapear_latinos()

def remover_acentos(txt):
    '''converte caracteres latinos acentuados em suas versões sem acentos'''
    return ''.join(MAPA_LATINOS.get(car, car) for car in txt)

def test():
    s = 'Ação, Álvaro! ☂ 氣'
    assert 'Acao, Alvaro! ☂ 氣' == remover_acentos(s)

if __name__=='__main__':
    test()
