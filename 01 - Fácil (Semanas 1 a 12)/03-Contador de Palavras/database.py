from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

#Contar Palavras
def contar_palavras(texto:str) -> int:
    return len(texto.split())

#Contar Caracteres com espaços
def contar_caracteres(texto:str) -> int:
    return len(texto)

#Contar Caracteres sem espaços
def contar_caracteres_sem_espacos(texto:str) -> int:
    return len(texto.replace(" ", ""))

#Contar Palavras únicas
def CONTAR_PALAVRAS_UNICAS(texto:str) -> int:
    return len(set(texto.split()))

#Contar Frequência de Palavras
def contar_frequencia_palavras(texto:str) -> str:
    palavras = texto.split()
    frequencia = {}
    for palavra in palavras:
        frequencia[palavra] = frequencia.get(palavra, 0) + 1  
        return max (frequencia, key=frequencia.get)

#analise de sentimento
def analise_sentimento(texto:str) -> str:
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(texto)
    if scores['compound'] > 0.02:
        return "Positivo"
    elif scores['compound'] < -0.02:
        return "Negativo"
    return "Neutro"


def exibir_resultados(texto:str):
    print(f"Quantidade de palavras: {contar_palavras(texto)}")
    print(f"Quantidade de caracteres: {contar_caracteres(texto)}")
    print(f"Quantidade de caracteres sem espaços: {contar_caracteres_sem_espacos(texto)}")
    print(f"Quantidade de palavras únicas: {CONTAR_PALAVRAS_UNICAS(texto)}")
    print(f"Palavra mais frequente: {contar_frequencia_palavras(texto)}")
    print(f"Sentimento do texto: {analise_sentimento(texto)}")