import requests

real = float(input('Digite um valor em R$ : '))
r = requests.get('https://api.hgbrasil.com/finance?key=d0b84560')

valor_dolar = r.json()['results']['currencies']['USD']['buy']
valor_euro = r.json()['results']['currencies']['EUR']['buy']

conv_dolar = real*valor_dolar
conv_euro = real*valor_euro

print (f'A cotação atual da moeda USD é: ${valor_dolar:.2f}')
print (f'A cotação atual da moeda EUR é: €{valor_euro:.2f}')
print (f'O valor digitado convertido em dolar é: ${conv_dolar:.2f}')
print (f'O valor digitado convertido em euro é: €{conv_euro:.2f}')



