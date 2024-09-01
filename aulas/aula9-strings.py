# Fatiamento de String, Análise com len(), count(), find(),
#  transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().

#1. len()
# A função len() retorna o número de itens de um objeto. Em strings, ela retorna o número de caracteres.

texto = "Python"
tamanho = len(texto)
print(tamanho)  # Saída: 6

#2. count()
# O método count() retorna o número de ocorrências de um substring dentro de uma string.

texto = "banana"
contagem = texto.count('a')
print(contagem)  # Saída: 3

#3. find()

# O método find() retorna o índice da primeira ocorrência de uma substring dentro de uma string. Se a substring não for encontrada, retorna -1.

texto = "banana"
indice = texto.find('nana')
print(indice)  # Saída: 2

#4. Transformações com replace()
# O método replace() substitui todas as ocorrências de uma substring por outra.

texto = "banana"
novo_texto = texto.replace('a', 'o')
print(novo_texto)  # Saída: "bonono"

#5. upper()
# O método upper() converte todos os caracteres de uma string para maiúsculas.

texto = "Python"
texto_maiusculo = texto.upper()
print(texto_maiusculo)  # Saída: "PYTHON"

#6. lower()
# O método lower() converte todos os caracteres de uma string para minúsculas.

texto = "Python"
texto_minusculo = texto.lower()
print(texto_minusculo)  # Saída: "python"

# 7. capitalize()
# O método capitalize() converte o primeiro caractere de uma string para maiúscula e os restantes para minúsculas.

texto = "python é legal"
texto_capitalizado = texto.capitalize()
print(texto_capitalizado)  # Saída: "Python é legal"

# 8. title()
# O método title() converte o primeiro caractere de cada palavra em uma string para maiúscula.

texto = "python é legal"
texto_titulo = texto.title()
print(texto_titulo)  # Saída: "Python É Legal"

#9. strip()

# O método strip() remove espaços em branco do início e do fim de uma string. Há também os métodos lstrip() e rstrip() que removem espaços apenas à esquerda ou à direita, respectivamente.

texto = "   Python   "
texto_sem_espacos = texto.strip()
print(texto_sem_espacos)  # Saída: "Python"

#0. Junção com join()

# O método join() junta elementos de uma lista em uma única string, com um separador especificado.

palavras = ["Python", "é", "legal"]
frase = " ".join(palavras)
print(frase)  # Saída: "Python é legal"