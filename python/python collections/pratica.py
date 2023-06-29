from collections import Counter

texto1 = '''
    A principal diferença entre uma operação B2B (Business to Business ou venda entre empresas) e B2C (Business to Consumer ou venda para o consumo) é no tipo de cliente e no tipo de operação. Na venda B2B, o cliente normalmente é outra empresa, comprando para seu consumo, para revenda ou como insumo para sua cadeia produtiva. São operações de venda atacado, para revenda ou corporativa. Já a venda B2C é para o cliente final, normalmente pessoa física, são as operações tradicionais de varejo.
'''

texto2 = '''
Apesar de termos mais contato e ser mais visível a venda do varejo para os clientes finais (B2C), a venda entre empresas (B2B) é estimada em ser pelo menos o dobro da venda varejo. Em e-Commerce as operações de varejo iniciaram muito antes das operações entre empresas. Nos Estados Unidos, existe uma previsão feita pela Forrester de que a venda através de e-Commerce B2B atinja U$ 1.1 trilhão até 2020. E para termos uma visão melhor dos grandes players do mercado, o principal site B2B é o chinês Alibaba. Ele movimenta praticamente a soma da Amazon e do eBay juntos, que são os dois maiores sites de e-Commerce dos Estados Unidos.

Para entendermos melhor cada um destes mercados, vamos primeiro listar exemplos de operações B2B e B2C:
'''
def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())

    proporcoes = [(letra, frequencia / total_de_caracteres * 100) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print(f'{caractere}, =>, {proporcao:.2f}%')

analisa_frequencia_de_letras(texto1)
print()
analisa_frequencia_de_letras(texto2)