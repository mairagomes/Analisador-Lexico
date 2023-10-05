import re
import numpy as np
import pandas as pd

def Distribui_tokens(t_temp,tokens_totais,pos_atual,tipo):
  termo='tk_'+t_temp.lower()
  if termo in list(tokens_totais.keys())[:17] and tipo =='identificador':
    print(termo)
    tokens_totais[termo].append((t_temp,pos_atual-len(t_temp)))
  elif tipo == 'numero':
    tokens_totais['tk_numero'].append((t_temp,pos_atual-len(t_temp)))
  elif termo in list(tokens_totais.keys())[:-1] and tipo == ':':
    tokens_totais['tk_:'].append((t_temp,pos_atual-len(t_temp)))
  elif termo in list(tokens_totais.keys())[:-1] and tipo == ',':
    tokens_totais['tk_)'].append((t_temp,pos_atual-len(t_temp)))
  elif termo in list(tokens_totais.keys())[:-1] and tipo == '(':
    tokens_totais['tk_('].append((t_temp,pos_atual-len(t_temp)))
  elif tipo == 'funcao':
    tokens_totais['tk_funcao'].append((t_temp,pos_atual-len(t_temp)))
  elif tipo == 'cadeia':
    tokens_totais['tk_cadeia'].append((t_temp,pos_atual-len(t_temp)))
  elif tipo == 'comentario_linha':
    tokens_totais['tk_comentario_linha'].append((t_temp,pos_atual-len(t_temp)))
  elif tipo == 'comentario_bloco':
    tokens_totais['tk_comentario_bloco'].append((t_temp,pos_atual-len(t_temp)))
  elif tipo == 'divisao':
    tokens_totais['tk_divisao'].append((t_temp,pos_atual-len(t_temp)))
  elif tipo == 'produto':
    tokens_totais['tk_produto'].append((t_temp,pos_atual-len(t_temp)))
  elif tipo == 'igual':
    tokens_totais['tk_igual'].append((t_temp,pos_atual-len(t_temp)))
  elif tipo == 'maior':
    tokens_totais['tk_maior'].append((t_temp,pos_atual-len(t_temp)))
  elif tipo == 'maior_igual':
    tokens_totais['tk_maior_igual'].append((t_temp,pos_atual-len(t_temp)))
  elif tipo == 'menor':
    tokens_totais['tk_menor'].append((t_temp,pos_atual-len(t_temp)))
  elif tipo == 'diferente':
    tokens_totais['tk_diferente'].append((t_temp,pos_atual-len(t_temp)))
  elif tipo == 'atribuicao':
    tokens_totais['tk_atribuicao'].append((t_temp,pos_atual-len(t_temp)))
  elif tipo == 'menor_igual':
    tokens_totais['tk_menor_igual'].append((t_temp,pos_atual-len(t_temp)))
  elif tipo == 'virgula':
    tokens_totais['tk_virgula'].append((t_temp, pos_atual-len(t_temp)))
  elif tipo == 'til':
    tokens_totais['tk_til'].append((t_temp, pos_atual-len(t_temp)))
  elif tipo == 'aspas':
    tokens_totais['tk_aspas_duplas'].append((t_temp, pos_atual-len(t_temp)))
  elif tipo == 'aspas_simples':
    tokens_totais['tk_aspas_simples'].append((t_temp, pos_atual-len(t_temp)))
  elif tipo == 'exclamacao':
    tokens_totais['tk_exclamacao'].append((t_temp, pos_atual-len(t_temp)))
  elif tipo == 'barra_vertical':
    tokens_totais['tk_barra_vertical'].append((t_temp, pos_atual-len(t_temp)))
  elif tipo == 'cifrao':
    tokens_totais['tk_cifrao'].append((t_temp, pos_atual-len(t_temp)))
  elif tipo == 'operacao_sum_sub':
    if t_temp =='+':
      tokens_totais['tk_soma'].append((t_temp,pos_atual-len(t_temp)))
    else:
      tokens_totais['tk_subtracao'].append((t_temp,pos_atual-len(t_temp)))
  else:
    tokens_totais['tk_IDs'].append((t_temp,pos_atual-len(t_temp)))
  return tokens_totais
# Abrir o arquivo de texto em modo de leitura
with open('ex1.cic', 'r') as file:

    # Ler todo o conteúdo do arquivo e armazená-lo em uma string
    ex1 = file.read()
lista=list(ex1)
lista=['\n']+lista+['\n']
textotemp=''.join(lista)

texto=textotemp+' '
state = 0
token_temp = []
tokens_totais ={
  #Palavras reservadas
                'tk_programa':[],
                'tk_fim_programa':[],
                'tk_se':[],
                'tk_entao':[],
                'tk_senao':[],
                'tk_leia':[],
                'tk_imprima':[],
                'tk_enquanto':[],
                'tk_menor_igual':[],
                'tk_atribuicao':[],
                'tk_diferente':[],
                'tk_menor':[],
                'tk_maior_igual':[],
                'tk_maior':[],
                'tk_igual':[],
                'tk_produto':[],
                'tk_subtracao':[],
                'tk_soma':[],
                'tk_divisao':[],
                'tk_comentario_linha':[],
                'tk_comentario_bloco':[],
                'tk_(':[],
                'tk_)':[],
                'tk_:':[],
                'tk_,':[],
                'tk_IDs':[],
                'tk_virgula':[],
                'tk_aspas':[],
                'tk_aspas_simples':[],
                'tk_til':[],
                'tk_exclamacao':[],
                'tk_barra_vertical':[],
                
                }
fim=len(texto)
count=0
openComent=False
closeComent=False
quebraLinha=[]
erros=[]
while count < fim:
  #print(texto[count])
  if state == 0:
    if re.match('[|]', texto[count]):#
      state=47
      token_temp.append( texto[count])
    elif re.match('[:]', texto[count]):#diferente
      state=45
      token_temp.append( texto[count])
    elif re.match('[&]]', texto[count]):#moeda
      state=44
      token_temp.append( texto[count])
    elif re.match('[!]', texto[count]):#diferente
      state=42
      token_temp.append( texto[count])
    elif re.match('[(]', texto[count]):#abre_parentese
      state=40
      token_temp.append( texto[count])
    elif re.match('[)]', texto[count]):#fecha_parentese
      state=41
      token_temp.append( texto[count])
    elif re.match('[<A-Za-z0-9>]', texto[count]):#Identificador
      state=8
      token_temp.append( texto[count])
    elif re.match('[/]', texto[count]):#  divisao
      state=36
      token_temp.append( texto[count])
    elif re.match('[<]', texto[count]):# (menor,menor igual,diferente)
      state=8
      token_temp.append( texto[count])
    elif re.match('[>]', texto[count]):#(maior, maior igual)
      state=33
      token_temp.append( texto[count])
    elif re.match('[=]', texto[count]):# igual, atricuicao, menor igual, maior igual, diferente
      state=35
      token_temp.append( texto[count])
    elif re.match('[*]', texto[count]):# produto
      state=37
      token_temp.append( texto[count])
    elif re.match('[+]', texto[count]):# soma
      state=38
      token_temp.append( texto[count])
    elif re.match('[-]', texto[count]):# subtracao
      state=39
      token_temp.append( texto[count])
    elif re.match('[~]', texto[count]):#unario
      state=49
      token_temp.append(texto[count])
    elif re.match('[,]', texto[count]):
      token= 48
      token_temp.append(texto[count])
    elif re.match('[""]', texto [count]):
      token=14
      token_temp.append(texto[count])
    elif re.match('[0-9A-F]', texto[count]):
      print('erro comecar em numero')
      erros.append(('erro de numero',texto[count],count))
      state=0
    else:
      state=0
      token_temp=[]



  elif state == 1:
    if re.match('[0-9A-F]', texto[count]):# numeros
      state=16
      token_temp.append( texto[count])
    elif re.match('[^\d.!@#$%¨&*]', texto[count]):# soma ou subtracao
      print('soma ou subtracao',''.join(token_temp))
      tokens_totais=Distribui_tokens(''.join(token_temp),tokens_totais,count,tipo='operacao_sum_sub')
      token_temp=[]
      state=0
      count=count-1
    else:
      erros.append(('erro sinal ',texto[count],count))
      state=0
      token_temp=[]
      count=count-1
  elif state == 8:
    if re.match('[<>]', texto[count]):# numeros
      state=10
      token_temp.append( texto[count])
    else:
      erros.append(('erro de funcao',texto[count],count))
      state=0
      token_temp=[]
      count=count-1
  elif state == 14:
    if re.match('[^"\n]', texto[count]):# cadeia
      state=16
      token_temp.append( texto[count])
    elif re.match('["]', texto[count]):
      token_temp.append( texto[count])
      tokens_totais=Distribui_tokens(''.join(token_temp),tokens_totais,count,tipo='cadeia')
      print("cadeia",''.join(token_temp))
      state=0
      token_temp=[]

    else:
      erros.append(('erro de cadeia',texto[count],count))
      print("ERRO de cadeia")
      state=0
      token_temp=[]
      count=count-1
  elif state == 40:
    if re.match('.', texto[count]):
      state=0
      tokens_totais=Distribui_tokens(''.join(token_temp),tokens_totais,count,tipo='(')
      print("Parentese aberto",''.join(token_temp))
      token_temp=[]
      count=count-1
    else:
      state=0
      token_temp=[]
      
  elif state == 41:
    
    if re.match('.', texto[count]):
      print('1')
      print("Parentese fechado",''.join(token_temp))
      tokens_totais=Distribui_tokens(''.join(token_temp),tokens_totais,count,tipo=')')
      state=0
      token_temp=[]
      count=count-1
    else:
      print("Parentese fechado",''.join(token_temp))
      tokens_totais=Distribui_tokens(''.join(token_temp),tokens_totais,count,tipo=')')
      state=0
      token_temp=[]
  elif state == 8:
    if re.match('[<A-Z0-9>]', texto[count]):
      state=10
      token_temp.append( texto[count])
    else:
      erros.append(('erro de identificador',texto[count],count))
      state=0
      token_temp=[]
      count=count-1
  elif state==10:
    if re.match('[A-Za-z]', texto[count]):
      state=24
      token_temp.append( texto[count])
    elif re.match("[ ,\n( )]",texto[count]):
      print("Identificador",''.join(token_temp))
      tokens_totais=Distribui_tokens(''.join(token_temp),tokens_totais,count,tipo='identificador')
      token_temp=[]
      state=0
      count=count-1
    else:
      tokens_totais=Distribui_tokens(''.join(token_temp),tokens_totais,count,tipo='identificador')
      erros.append(('erro de identificador',texto[count],count))
      state=0
      token_temp=[]
      count=count-1
  elif state== 36:
    if re.match('[^/]',texto[count]):
      print('Divisao',''.join(token_temp))
      tokens_totais=Distribui_tokens(''.join(token_temp),tokens_totais,count,tipo='divisao')
      state=0
      token_temp=[]
      count=count-1
  elif state==12:#//joao
    if re.match('[#]',texto[count]):#estrutura para verificar fim da string
      state=12
      token_temp.append(texto[count])
    elif re.match('[\n]',texto[count]):
      print("Comentario em linha",''.join(token_temp))
      tokens_totais=Distribui_tokens(''.join(token_temp),tokens_totais,count,tipo='comentario_linha')
      state=0
      token_temp=[]
    else:
      erros.append(('erro de comentario',texto[count],count))
      state=0
      token_temp=[]
      count=count-1
  elif state == 14:
    if re.match('[```]',texto[count]):######
        if re.match('[\n]',texto[count]):
            quebraLinha.append(count)
        else:
          pass
        state=14
        token_temp.append(texto[count])
    elif re.match('[```]',texto[count]):
      token_temp.append(texto[count])
      state=14
    else:
      erros.append(('erro de comentario em bloco',texto[count],count))

      token_temp=[]
      state=0
      count=count-1
  elif state==14:
    if re.match('[```]',texto[count]):
      state=14
      token_temp.append(texto[count])
    elif re.match('[^```]',texto[count]):
        if re.match('[\n]',texto[count]):
            quebraLinha.append(count)
        else:
          pass
        state=14
        token_temp.append(texto[count])
    elif re.match('[``````]',texto[count]):
      token_temp.append(texto[count])
      print('Comentario em Bloco',''.join(token_temp))
      closeComent=True
      tokens_totais=Distribui_tokens(''.join(token_temp),tokens_totais,count,tipo='comentario_bloco')
      state=0
      token_temp=[]
    else:
      erros.append(('erro de comentario em bloco',texto[count],count))
      token_temp=[]
      state=0
      count=count-1
  elif state==8:
    if re.match('[=]',texto[count]):
      token_temp.append(texto[count])
      print('Menor igual',''.join(token_temp))
      tokens_totais=Distribui_tokens(''.join(token_temp),tokens_totais,count,tipo='menor_igual')
      token_temp=[]
      state=0
    elif re.match('[:]',texto[count]):
      token_temp.append(texto[count])
      print('Atribuicao',''.join(token_temp))
      tokens_totais=Distribui_tokens(''.join(token_temp),tokens_totais,count,tipo='atribuicao')
      token_temp=[]
      state=0
    elif re.match('[!]',texto[count]):
      token_temp.append(texto[count])
      tokens_totais=Distribui_tokens(''.join(token_temp),tokens_totais,count,tipo='diferente')
      print('Diferente',''.join(token_temp))
      token_temp=[]
      state=0
    elif  re.match('[^=>-]',texto[count]):
      print('Menor',''.join(token_temp))
      tokens_totais=Distribui_tokens(''.join(token_temp),tokens_totais,count,tipo='menor')
      token_temp=[]
      state=0
    else:
      erros.append(('erro de operador <',texto[count],count))
      token_temp=[]
      state=0
      count=count-1
  elif state == 33:
    if re.match('[^=]',texto[count]):
      print('maior',''.join(token_temp))
      tokens_totais=Distribui_tokens(''.join(token_temp),tokens_totais,count,tipo='maior')
      state=0
      token_temp=[]
    elif re.match('[=]',texto[count]):
      token_temp.append(texto[count])
      print('maior igual',''.join(token_temp))
      tokens_totais=Distribui_tokens(''.join(token_temp),tokens_totais,count,tipo='maior_igual')
      state=0
      token_temp=[]
      
    else:
      erros.append(('erro de operador maior',texto[count],count))
      token_temp=[]
      state=0
      count=count-1
  elif state == 35:
    if re.match('[=]',texto[count]):
      state=0
      token_temp.append(texto[count])
      print('igual',''.join(token_temp))
      tokens_totais=Distribui_tokens(''.join(token_temp),tokens_totais,count,tipo='igual')
      token_temp=[]
    else:
      erros.append(('erro de operador =',texto[count],count))
      state=0
      token_temp=[]
      count=count-1
  elif state == 37:
    if re.match('[^*]',texto[count]):
      print('produto')
      tokens_totais=Distribui_tokens(''.join(token_temp),tokens_totais,count,tipo='produto')
      state=0
      token_temp=[]
      count=count-1
    else:
      erros.append(('erro de operador produto',texto[count],count))
      state=0
      token_temp=[]
      count=count-1
  elif state== 8:
    if re.match('[<]',texto[count]):
      state=19
      token_temp.append(texto[count])
    elif re.match('[A-Za-z]',texto[count]):
      state=20
      token_temp.append(texto[count])
    else:
      erros.append(('erro de funcao',texto[count],count))
      state=0
      token_temp=[]
      count=count-1
  elif state==10:
    if re.match('[A-Za-z0-9]',texto[count]):
      state=10
      token_temp.append(texto[count])
    elif re.match('[>]',texto[count]):
      state=21
      token_temp.append(texto[count])
    else:
      erros.append(('erro de funcao',texto[count],count))
      state=0
      token_temp=[]
      count=count-1
  elif state==10:
    if re.match('[<]',texto[count]):
      token_temp.append(texto[count])
      tokens_totais=Distribui_tokens(''.join(token_temp),tokens_totais,count,tipo='funcao')
      print('funcao',''.join(token_temp))
      state=0
      token_temp=[]
    else:
      erros.append(('erro de funcao',texto[count],count))
      state=0
      token_temp=[]
      count=count-1



  elif state==7:
    if re.match('[0-9A-F]',texto[count]):
      token_temp.append(texto[count])
      state=17
    elif re.match('[.]',texto[count]):
      token_temp.append(texto[count])
      state=9
    else:
      #print('Inteiro 1 digito ',''.join(token_temp))
      tokens_totais=Distribui_tokens(''.join(token_temp),tokens_totais,count,tipo='numero')
      token_temp=[]
      state=0
      count=count-1
  elif state == 17:
    if re.match('[0-9A-F]',texto[count]):
      token_temp.append(texto[count])
      state=17
    elif re.match('[.]',texto[count]):
      token_temp.append(texto[count])
      state = 18 
    else:
      #print('Inteiro n digitos ',''.join(token_temp))
      tokens_totais=Distribui_tokens(''.join(token_temp),tokens_totais,count,tipo='numero')
      token_temp=[]
      state=0
      count=count-1
  elif state == 18:
    if re.match('[0-9A-F]',texto[count]):
      token_temp.append(texto[count])
      state=19
    else:
      erros.append(('erro de numero',texto[count],count))
      state=0
      token_temp=[]
  elif state ==19:
    if re.match('[0-9A-F]',texto[count]):
      token_temp.append(texto[count])
      state=19
    elif re.match('[^e]',texto[count]):
      #print("decimal do tipo xx.xx",''.join(token_temp))
      tokens_totais=Distribui_tokens(''.join(token_temp),tokens_totais,count,tipo='numero')
      token_temp=[]
      state=0
      count=count-1
    else:
      erros.append(('erro de numero',texto[count],count))
      print('ERRO de simbolo e')
      state=0
      token_temp=[]
  elif state == 19:
    if re.match('[0-9]',texto[count]):
      state=21
      token_temp.append(texto[count])
    else:
      erros.append(('erro de numero',texto[count],count))
      state=0
      token_temp=[]
  elif state==21:
    if re.match('[0-9A-F]',texto[count]):
      state=19
      token_temp.append(texto[count])
    elif re.match('[e]',texto[count]):
      state=21
      token_temp.append(texto[count])
    else:
      #print('Float tipo x.xxxx',''.join(token_temp))
      tokens_totais=Distribui_tokens(''.join(token_temp),tokens_totais,count,tipo='numero')
      state=0
      token_temp=[]
      count=count-1
  elif state == 21:
    if re.match('[+-]',texto[count]):
      state=23
      token_temp.append(texto[count])
    else:
      erros.append(('erro de numero',texto[count],count))
      state=0
      token_temp=[]
  elif state==24:
    if re.match('[0-9A-F]',texto[count]):
      state=24
      token_temp.append(texto[count])
    else:
      erros.append(('erro de numero',texto[count],count))
      state=0
      token_temp=[]
  elif state==24:
    if re.match('[0-9A-F]',texto[count]):
      state=15
      token_temp.append(texto[count])
    else:
      #print('Exponencial do tipo +x.xxxxe+x',''.join(token_temp))
      tokens_totais=Distribui_tokens(''.join(token_temp),tokens_totais,count,tipo='numero')
      state=0
      token_temp=[]
      count=count-1

  elif state == 1:
    if re.match('G-ZA-F', texto[count]):
      state=0
      print("moeda", ''.join(token_temp))
      tokens_totais=Distribui_tokens(''.join(token_temp), tokens_totais, count, tipo='G-Z')
      token_temp=[]
      count=count-1
    elif re.match('[$]', texto[count]):
      token_temp.append(texto[count])
      state = 9 
    else:
      tokens_totais = Distribui_tokens(''.join(token_temp), tokens_totais, count, tipo='moeda')
      token_temp = []
      state = 0
      count = count - 1
  elif state == 3:
    if re.match('[1-9]',texto[count]):
      token_temp.append(texto[count])
      state=3
    elif re.match('[.]',texto[count]):
      token_temp.append(texto[count])
      state = 18 
    else:
      #print('Inteiro n digitos ',''.join(token_temp))
      tokens_totais=Distribui_tokens(''.join(token_temp),tokens_totais,count,tipo='moeda')
      token_temp=[]
      state=0
      count=count-1
  elif state == 4:
    if re.match('[1-9]',texto[count]):
      token_temp.append(texto[count])
      state=5
    elif re.match('[.]',texto[count]):
      token_temp.append(texto[count])
      state = 18 
    if re.match('[]',texto[count]):
      token_temp.append(texto[count])
      tokens_totais=Distribui_tokens(''.join(token_temp),tokens_totais,count,tipo='moeda')
      print('moeda',''.join(token_temp))
      state=0
      token_temp=[]
    else:
      erros.append(('erro de moeda',texto[count],count))
      state=0
      token_temp=[]
      count=count-1


  elif state == 45:
    if re.match('.', texto[count]):
      state=0
      print("dois pontos",''.join(token_temp))
      tokens_totais=Distribui_tokens(''.join(token_temp),tokens_totais,count,tipo=':')
      token_temp=[]
      count=count-1
    elif re.match('[\n]', texto[count]):
      state=0
      print("dois pontos",''.join(token_temp))
      tokens_totais=Distribui_tokens(''.join(token_temp),tokens_totais,count,tipo=':')
      token_temp=[]
      count=count-1
    else:
      erros.append(('erro de dois pontos',texto[count],count))
      state=0
      token_temp=[]
  elif state == 49:
    if re.match('~', texto[count]):
      state=0
      print("til",''.join(token_temp))
      tokens_totais=Distribui_tokens(''.join(token_temp),tokens_totais,count,tipo=',')
      token_temp=[]
      count=count-1
    elif re.match('[\n]', texto[count]):
      state=0
      print("til",''.join(token_temp))
      tokens_totais=Distribui_tokens(''.join(token_temp),tokens_totais,count,tipo=',')
      token_temp=[]
      count=count-1
    else:
      erros.append(('erro de til',texto[count],count))
      state=0
      token_temp=[]
  else:
    state=0
    token_temp=[]

  count=count+1
  if count == len(texto):
    if openComent==True and closeComent==True:
        openComent=False
        closeComent==False
        state=0
        token_temp=[]
    elif openComent==True and closeComent==False:
        count=quebraLinha.pop(0)+1
        print(f'ERRO NA POSICAO {count-1}')
        erros.append(('erro de comentario em bloco',texto[count-1],count-1))
        quebraLinha=[]
        openComent=False
        state=0
        token_temp=[]
    else:
        pass
  else:
    pass
  

#print(tokens_totais,erros)

#######################GERANDO RELATORIO####################################

quebra_rec=[]
linhas_colunas=[]
final=[]
for k,c in enumerate(texto):
  if re.match('[\n]',c):
    quebra_rec.append(k)
for k,qr in enumerate(quebra_rec):
  if k+1 < len(quebra_rec):
    linhas_colunas.append((qr,quebra_rec[k+1]))
for k,(ini,fim) in enumerate(linhas_colunas):
  final.append(np.arange(ini+1,fim+1,1))
final=pd.DataFrame(final)
final=final.set_axis(range(1, len(final)+1), axis=0)
final=final.set_axis(range(1, len(final.columns)+1), axis=1)

print(final)
######percorre erros################
erros_para_relatorio=[]
for comentario,caracter_erro,pos_erro in erros:
  #print(comentario,caracter_erro,pos_erro)
  linha, coluna = np.where(final == pos_erro)
  print(f'Erro léxico na linha {int(linha+1)} coluna {int(coluna+1)}')
  erros_para_relatorio.append((int(linha+1),int(coluna+1)))

print(erros_para_relatorio)
 #######################################PREENCHER TABELA1#######################

dataTable1 = {'token': [], 'lexema': [], 'posicao na entrada': []}
for token, entries in tokens_totais.items():
    for  position in entries:
      dataTable1['token'].append(token)
      dataTable1['lexema'].append(position[0])
      linha, coluna = np.where(final == position[1])
      if len(linha) > 0:
        dataTable1['posicao na entrada'].append(f'({int(linha[0]+1)},{int(coluna[0]+1)})')
      else:
        # handle the case where linha is empty, for example by appending a default value
        dataTable1['posicao na entrada'].append('(N/A)')

dataFrame=pd.DataFrame(dataTable1)
tabela1 = dataFrame.groupby(['token','lexema']).agg(list)
print(tabela1)

print('#'*40)
tabela2 = dataFrame.groupby(['token']).agg(list)
resumo={'token':[],'usos':[]}
for index,row in tabela2.iterrows():
  resumo['usos'].append(len(row['posicao na entrada']))
  resumo['token'].append(index)
resumo=pd.DataFrame(resumo)
#inserir os casos 0 uso se existir
total_sum = resumo['usos'].sum()
diferenca=set(tokens_totais.keys()) - set(dataFrame['token'].value_counts().index)
for e in diferenca:
    print(type(e), "não está na lista")
    resumo.loc[resumo.shape[0]] = [e, 0]
resumo.loc[resumo.shape[0]] = ['total', total_sum]
print(resumo)


##########################MOSTRANDO ERROS########################
def decora_erros(texto, posicoes):
    linhas = texto.split('\n')
    num_linhas = len(str(len(linhas) - 2))
    
    for i, l in enumerate(linhas):
        linha_atual = i
        print(f'[{str(linha_atual).rjust(num_linhas)}]{l}')
            
        for posicao in posicoes:
            linha_erro, coluna_erro = posicao
            if linha_atual == linha_erro:
                mensagem_erro = f'Erro lexico na linha {linha_erro} e coluna {coluna_erro}'
                print(' '*(coluna_erro-1 + num_linhas + 2) + '^' + '-'*(len(l)-coluna_erro) + f' {mensagem_erro}')


print(decora_erros(texto,erros_para_relatorio))
