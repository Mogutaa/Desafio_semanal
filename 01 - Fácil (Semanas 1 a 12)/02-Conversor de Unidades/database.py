


#converte metros para quilometros
def metro_para_quilometros(metros):
    quilometros = metros / 1000
    return quilometros

#converte metros para centimetros
def metro_para_centimetros(metros):
    centimetros = metros * 100
    return centimetros

#converte metros para milimetros
def metro_para_milimetros(metros):
    milimetros = metros * 1000
    return milimetros

#converte quilometros para metros
def quilometros_para_metros(quilometros):
    metros = quilometros * 1000
    return metros

#converte quilometros para centimetros
def quilometros_para_centimetros(quilometros):
    centimetros = quilometros * 100000
    return centimetros

#converte quilometros para milimetros
def quilometros_para_milimetros(quilometros):
    milimetros = quilometros * 1000000
    return milimetros  

#converte centimetros para metros
def centimetros_para_metros(centimetros):
    metros = centimetros / 100
    return metros

#converte centimetros para quilometros
def centimetros_para_quilometros(centimetros):
    quilometros = centimetros / 100000
    return quilometros

#converte centimetros para milimetros
def centimetros_para_milimetros(centimetros):
    milimetros = centimetros * 10
    return milimetros

#converte milimetros para metros
def milimetros_para_metros(milimetros):
    metros = milimetros / 1000
    return metros

#converte milimetros para quilometros
def milimetros_para_quilometros(milimetros):
    quilometros = milimetros / 1000000
    return quilometros

#converte milimetros para centimetros
def milimetros_para_centimetros(milimetros):
    centimetros = milimetros / 10
    return centimetros

#converte litros para mililitros
def litros_para_mililitros(litros):
    mililitros = litros * 1000
    return mililitros

#converte mililitros para litros
def mililitros_para_litros(mililitros):
    litros = mililitros / 1000
    return litros

#converte litros para galões
def litros_para_galoes(litros):
    galoes = litros / 3.785
    return galoes

#converte galões para litros
def galoes_para_litros(galoes):
    litros = galoes * 3.785
    return litros

#converte celcius para fahrenheit
def celcius_para_fahrenheit(celcius):
    fahrenheit = celcius * 1.8 + 32
    return fahrenheit

#converte fahrenheit para celcius
def fahrenheit_para_celcius(fahrenheit):
    celcius = (fahrenheit - 32) / 1.8
    return celcius

#converte celcius para kelvin
def celcius_para_kelvin(celcius):
    kelvin = celcius + 273.15
    return kelvin

#converte kelvin para celcius
def kelvin_para_celcius(kelvin):
    celcius = kelvin - 273.15
    return celcius

#lista de conversões para comprimento
conversoes_comprimento = {
    "1": ("Metro para Quilometros", metro_para_quilometros ,"Metro(s)","Quilometro(s)"),
    "2": ("Metro para Centimetros",metro_para_centimetros,"Metro(s)","Centimetro(s)"),
    "3": ("Metro para Milimetros",metro_para_milimetros,"Metro(s)","Milimetro(s)"),
    "4": ("Quilometros para Metros",quilometros_para_metros,"Quilometro(s)","Metro(s)"),
    "5": ("Quilometros para Centimetros",quilometros_para_centimetros,"Quilometro(s)","Centimetro(s)"),
    "6": ("Quilometros_para_centimetros",quilometros_para_milimetros,"Quilometro(s)","Milimetro(s)"),
    "7": ("Centimetros para Metros",centimetros_para_metros,"Centimetro(s)","Metro(s)"),
    "8": ("Centimetros para Quilometros",centimetros_para_quilometros,"Centimetro(s)","Quilometro(s)"),
    "9": ("Centimetros para Milimetros",centimetros_para_milimetros,"Centimetro(s)","Milimetro(s)"),
    "10": ("Milimetros para Metros",milimetros_para_metros,"Milimetro(s)","Metro(s)"),
    "11": ("Milimetros para Quilometros",milimetros_para_quilometros,"Milimetro(s)","Quilometro(s)"),
    "12": ("Milimetros para Centimetros",milimetros_para_centimetros,"Milimetro(s)","Centimetro(s)"),}

#lista de conversões para temperatura
conversoes_temperatura = {
    "1": ("Celcius para Fahrenheit",celcius_para_fahrenheit,"Celcius","Fahrenheit"),
    "2": ("Fahrenheit para Celcius",fahrenheit_para_celcius,"Fahrenheit","Celcius"),
    "3": ("Celcius para Kelvin",celcius_para_kelvin,"Celcius","Kelvin"),
    "4": ("Kelvin para Celcius",kelvin_para_celcius,"Kelvin","Celcius"),
}


#lista de conversões para volume
conversoes_volume = {
    "1": ("Litros para Mililitros",litros_para_mililitros,"Litro(s)","Mililitro(s)"),
    "2": ("Mililitros para Litros",mililitros_para_litros,"Mililitro(s)","Litro(s)"),
    "3": ("Litros para Galoes",litros_para_galoes,"Litro(s)","Galo(s)"),
    "4": ("Galoes para Litros",galoes_para_litros,"Galo(s)","Litro(s)"),
}
