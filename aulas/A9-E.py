string = "Curso em Vídeo"

# Métodos de fatiameno de string
fat1 = string[3]  # Pega o 3º caractere
fat2 = string[
       5:14]  # Pega a string do 5 até o final dela (nesse caso, o último caractere é 13, no entanto, o python trabalha com < e não <=
# Logo, se faz necessário adicionar +1 ao índice do último caractere que queremos pegar
fat3 = string[2:11:2]  # Vai do 2 ao 11 índice, pulando de 2 em 2
fat4 = string[:8]  # Começa do índice 0 e vai até 8
fat5 = string[6:]  # Começa o 6 e vai até o final
fat6 = string[2::3]  # começa do 2 e vai até o final, pulando de 3 em 3
fat7 = string[::2]  # Do começo ao final, pulando de 2 em 2

# Métodos de análise da string
an = len(string)  # Tamanho da string
an1 = string.count('A')  # Quantas vezes o caractere A (Maiúsculo) apareceu na string
an2 = string.count('o', 2, 10)  # Quantas vezes o 'o' apareceu entre os índices 2 e 10
an3 = string.find('deo')  # Retorna índice inicial do trecho dentro da string
an4 = string.find('Daniel')  # Se passamos uma string que não existe, o método find irá retornar -1
an5 = 'em' in string  # in não é funcionalidade, mas operador. No entanto, ele retorna true/false para a presença(ou não) do trecho dentro da string

# Métodos de transformação
string.replace('Vídeo', 'Vídeo Python')  # Subsituição
string.upper()  # Toda a string fica em caixa alta
string.lower()  # Toda a string fica em caixa baixa
string.capitalize()  # Deixa toda a string em letra minúscula, exceto a primeira letra
string.title()  # Deixa toda primeira letra de toda palavra em maíusculo, o resto fica em minúsculo
string.strip()  # Remove espaços em branco inúteis da string (Espaços no início e fim do texto
# Se quisermos tirar o espaço de apenas um dos lados da string, podemos usar o rstrip/lstrip

# Método de divisão
div1 = string.split()  # Por padrão, a divisão é feita a partir dos espaços em branco no meio do texto. Retorna um vetor no qual cada índice aloca uma palavra

# Método de junção
jun = ' '.join(
    div1)  # Se temos uma lista de palavras separadas, podemos unificá-las e formar uma frase, tendo, nesse caso, o ' ' como separador entre elas
