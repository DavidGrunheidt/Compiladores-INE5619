# David Grunheidt Vilela Ordine - 16202253
import sys
import csv
from lexer import generateTokensListFromCode
from non_terminals_enum import NonTermSymb
from terminals_enum import TermSymb

nonTermDict = {}
for nonTerm in NonTermSymb:
    nonTermDict[nonTerm.value] = nonTerm

termDict = {}
for term in TermSymb:
    termDict[term.value] = term

parsingTable = {}
with open('parsing_table.csv') as parsingTableCsv:
    reader = csv.reader(parsingTableCsv, skipinitialspace=True, quotechar='"')
    headers = next(reader, None)[1:]
    for row in reader:
        rowDict = {}
        rowAux = row[1:]
        for index in range(len(rowAux)):
            elem = rowAux[index]
            if elem != '':
                elem = [x for x in elem.split('→', 1)[1].split(' ') if x != '']
                rowDict[headers[index]] = elem
        parsingTable[row[0]] = rowDict

# Get the file path
file_path = sys.argv[1]

stack = [TermSymb.ENDSTACK, NonTermSymb.PROGRAM]
stackTop = None
tokens = generateTokensListFromCode(file_path)
error = False
for token in tokens:
    while True:
        try:
            # Desempilha valor
            stackTop = stack.pop().value
            # Se o simbolo desempilhado for não terminal, talvez empilhar lado direito da produção
            if stackTop in nonTermDict:
                tokValueAux = token.value
                if token.type == 'ID':
                    tokValueAux = 'ident'
                elif token.type == 'IDFUNC':
                    tokValueAux = 'ident_func'
                elif token.type == 'STRINGCONST':
                    tokValueAux = 'string_constant'
                elif token.type == 'FLOATCONST':
                    tokValueAux = 'float_constant'
                elif token.type == 'INTCONST':
                    tokValueAux = 'int_constant'

                # print(str([stackTop, tokValueAux]))
                # print('in : ' + str(parsingTable[stackTop][tokValueAux]))
                # print('out : ' + str(stackTop) + '\n')

                newElements = parsingTable[stackTop][tokValueAux]
                newElements.reverse()
                # Se for igual a epsilon, não empilha nada (não faz nada)
                if newElements == ['ε']:
                    continue
                # Empilha lado direito da produção
                else:
                    for elem in newElements:
                        if elem in nonTermDict:
                            stack.append(nonTermDict[elem])
                        elif elem in termDict:
                            stack.append(termDict[elem])
                        else:
                            error = True
                            break
            # Se o simbolo desempilhado for terminal, avança a entrada
            elif stackTop in termDict:
                break
            else:
                error = True
                break
        except KeyError as e:
            error = True
            break
    if error:
        print('Erro, entrada ' + str(stackTop) + ' → ' + token.value + ' vazia, Token: ' + str(token) + ' linha ' + str(token.lineno) + ', coluna ' + str(token.lexpos))
        break

if not error:
    print('Sucess')









