#coding: utf-8
import requests
import json
import sys
import os
from threading import Thread
cyanClaro="\033[1;36m"
vermelho = '\033[31;1m'
verde = '\033[32;1m'
azul = '\033[34;1m'
normal = '\033[0;0m'
purpleClaro= '\033[1;35m'
amarelo= '\033[1;33m'
ciano='\033[46m'
magenta='\033[45m'
normal = '\033[0;0m'
os.system('clear')
Baner = """

__________$_______________$_____________
_________$$_________________$$__________
________$$___________________$$_________
_______$$_____________________$$________
_______$$_____________________$$________
_______$$_____________________$$________        
________$$_☯C0nsult3r_Danger☯_$$________
_____ $_$$___________________$$_$_______ [1] ☯ CNPJ Consulter ☯ 
____$$__$$___________________$$__$$_____ 
___$$____$$_________________$$___$$_____
___$______$$$__$_______$___$$$___$$_____
___$$______$$$__$_____$___$$$____$$_____
___$$$______$$$__$$$$$__$$$_____$$$$____
____$$$$$$___$$$$$$$$$$$$___$$$$$$$_____
________$$$$$$$$$$$$$$$$$$$$$$__________ [2] ☯ BIN Checker ☯
____$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$____
___$$$____$$$$$$$$$$$$$$$$$$$___$$$_____
__$$$___________$$$$$$$$_________$$_____
__$$__________$$$$$$$$$$$$_______ $$____
_$$__________$$$$$$$$$$$$$$$_______$$___
_$$_____$$$$$$$$$$$$$$$$$$$$$$$$____$$__ [3] ☯ Consultas Por Placas ☯
$$_____$$$__$$$$$$$$$$$$$$$$__$$____$$__ 
_$$____$$___$$$$$$$__$$$$$$$__$$____$___
__$____$$___$$$$$$$__$$$$$$$__$$___ $___
___$___$$___$$$$$$$$$$$$$$$$__$$___$____
____$__$$____$$$$$$$$$$$$$$___$$__$_____
_______$$_____$$$$$$$$$$$$____$$________ [4] ☯ Pesquisa de Filmes (IMDB) ☯
_______$$_______$$$$$$$$______$$________
________$$________$$$$________$$________
_________$_________$$_________$_________
          łαbørαŧøriø Fαηŧαsмα
                   ૐ	
 ☪ sєαrcЋ før yøur fαvøriŧє C0nsult3r_Danger
☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢
☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢
☢☢☢ ૐ  Coded by : @łuŧЋ1єr - ルシアー  ૐ      ☢☢☢
☢☢☢ ☮ date : 06.02.17   (@Xcultevil) Telegram ☢☢☢
☢☢☢ ☎ Facebook: TerminalRoot404               ☢☢☢
☢☢☢ ♝ Usage : Use this Options!               ☢☢☢
☢☢☢ ♜ SCRIPT PRIV8 ♜                          ☢☢☢
☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢
☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢☢
"""
CNPJBANER = """
   	  █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
          █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
          █░░║║║╠─║─║─║║║║║╠─░░█ 
          █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
          █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
          ▒▒▄▀▀▀▀▀▄▒▒▒▒▒▄▄▄▄▄▒▒▒
          ▒▐░▄░░░▄░▌▒▒▄█▄█▄█▄█▄▒
          ▒▐░▀▀░▀▀░▌▒▒▒▒▒░░░▒▒▒▒
          ▒▒▀▄░═░▄▀▒▒▒▒▒▒░░░▒▒▒▒
          ▒▒▐░▀▄▀░▌▒▒▒▒▒▒░░░▒▒▒▒
        +=========================+
        |   łαbørαŧøriø Fαηŧαsмα  |
        +=========================+
        | Coded : łuŧЋ1єr         |
        | Consultor : CPNJ        |
        | Usage : 06714992000103  |
        |  Numeros sem espaço     |
        +=========================+
        +=========================+
"""
PLACABANER = """
   	  █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
          █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
          █░░║║║╠─║─║─║║║║║╠─░░█ 
          █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
          █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
          ▒▒▄▀▀▀▀▀▄▒▒▒▒▒▄▄▄▄▄▒▒▒
          ▒▐░▄░░░▄░▌▒▒▄█▄█▄█▄█▄▒
          ▒▐░▀▀░▀▀░▌▒▒▒▒▒░░░▒▒▒▒
          ▒▒▀▄░═░▄▀▒▒▒▒▒▒░░░▒▒▒▒
          ▒▒▐░▀▄▀░▌▒▒▒▒▒▒░░░▒▒▒▒
        +=========================+
        |   łαbørαŧøriø Fαηŧαsмα  |
        +=========================+
        | Coded : łuŧЋ1єr         |
        | Consultor : PLACA       |
        | Usage : JSQ7436         |
        +=========================+
        +=========================+
"""
FILMESBANER = """
   	  █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
          █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
          █░░║║║╠─║─║─║║║║║╠─░░█ 
          █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
          █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
          ▒▒▄▀▀▀▀▀▄▒▒▒▒▒▄▄▄▄▄▒▒▒
          ▒▐░▄░░░▄░▌▒▒▄█▄█▄█▄█▄▒
          ▒▐░▀▀░▀▀░▌▒▒▒▒▒░░░▒▒▒▒
          ▒▒▀▄░═░▄▀▒▒▒▒▒▒░░░▒▒▒▒
          ▒▒▐░▀▄▀░▌▒▒▒▒▒▒░░░▒▒▒▒
        +=========================+
        |   łαbørαŧøriø Fαηŧαsмα  |
        +=========================+
        | Coded : łuŧЋ1єr         |
        | IMDB : FILMES           |
        | Usage : Matrix          |
        +=========================+
        +=========================+
"""
BINBANER = """
   	  █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
          █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
          █░░║║║╠─║─║─║║║║║╠─░░█ 
          █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
          █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
          ▒▒▄▀▀▀▀▀▄▒▒▒▒▒▄▄▄▄▄▒▒▒
          ▒▐░▄░░░▄░▌▒▒▄█▄█▄█▄█▄▒
          ▒▐░▀▀░▀▀░▌▒▒▒▒▒░░░▒▒▒▒
          ▒▒▀▄░═░▄▀▒▒▒▒▒▒░░░▒▒▒▒
          ▒▒▐░▀▄▀░▌▒▒▒▒▒▒░░░▒▒▒▒
        +=========================+
        |   łαbørαŧøriø Fαηŧαsмα  |
        +=========================+
        | Coded : łuŧЋ1єr         |
        | Consultor : BIN         |
        | Usage : 41472022        |
        +=========================+
        +=========================+
"""
########################################################################################################
#####                      CNPJ    CNPJ      CNPJ        CPNJ                                   ########
########################################################################################################
def requisicao(titulo):
	try:
		req = requests.get('https://www.receitaws.com.br/v1/cnpj/' + titulo)
		cnpj = json.loads(req.text)
		return cnpj
	
	except:
		print('Error na Conexão')
		return None
def printar_detalhes(cnpj):
	print(verde+'+ ================================================================================== +')
	print('\n'+verde+'               Atividade Principal!..[./]\n')
	print(verde+'+ ================================================================================== +\n')
	print(vermelho+'Comerce:'+normal, amarelo+ cnpj['atividade_principal'][0]['text']+normal )
	print(vermelho+'ID/Codigo:'+normal, amarelo+ cnpj['atividade_principal'][0]['code']+normal )
	print(vermelho+'Situação Data:'+normal, amarelo+ cnpj['data_situacao']+normal+'\n')

	print(vermelho+'+ ================================================================================== +')
	print(vermelho+'\n'+vermelho+'          Detalhes Sobre o Comercio..[./]\n')
	print('+ ================================================================================== +\n')
	print(verde+'Sobre: '+normal, cyanClaro+cnpj['atividades_secundarias'][0]['text'])
	print(verde+'Sobre: '+normal, cyanClaro+cnpj['atividades_secundarias'][1]['text'])
	print(verde+'sobre:'+normal, cyanClaro+cnpj['atividades_secundarias'][2]['text']+'\n')

	print(amarelo+'+ ================================================================================== +')
	print(amarelo+'\n'+amarelo+'          Detalhes Sobre Proprietários..[./]\n')
	print('+ ================================================================================== +\n')
	print(amarelo+'Cargo e Associação: '+normal,verde+cnpj['qsa'][0]['qual'])
	print(amarelo+'Dados e informações adicionais: '+normal,verde+cnpj['qsa'][0]['nome'])
	print(amarelo+'Cargo e Associação: '+normal,verde+cnpj['qsa'][1]['qual'])
	print(amarelo+'Dados e informações adicionais: '+normal,verde+cnpj['qsa'][1]['nome'])
	print(amarelo+'Cargo e Associação: '+normal,verde+cnpj['qsa'][2]['qual'])
	print(amarelo+'Dados e informações adicionais: '+normal,verde+cnpj['qsa'][2]['nome']+'\n')
	print(purpleClaro+'+ ================================================================================== +')
	print('\n'+purpleClaro+'          Dados e Informações Complementares..[./]\n')
	print(purpleClaro+'+ ================================================================================== +\n')			
	print(cyanClaro+'Situação: '+normal,vermelho+cnpj['situacao'])
	print(cyanClaro+'Bairro: '+normal,vermelho+cnpj['bairro'])
	print(cyanClaro+'logradouro: '+normal,vermelho+cnpj['logradouro'])
	print(cyanClaro+'Numero da Casa: '+normal,vermelho+cnpj['numero'])
	print(cyanClaro+'Cep: '+normal,vermelho+cnpj['cep'])
	print(cyanClaro+'Municipio: '+normal,vermelho+cnpj['municipio'])
	print(cyanClaro+'Data de Abertura: '+normal,vermelho+cnpj['abertura'])
	print(cyanClaro+'Natureza Juridica: '+normal,vermelho+cnpj['natureza_juridica'])
	print(cyanClaro+'fantasia: '+normal,vermelho+cnpj['fantasia'])
	print(cyanClaro+'CNPJ: '+normal,vermelho+cnpj['cnpj'])
	print(cyanClaro+'Data de Abertura: '+normal,vermelho+cnpj['abertura'])
	print(cyanClaro+'Ultima Atualizaçao (Data): '+normal,vermelho+cnpj['ultima_atualizacao'])
	print(cyanClaro+'Status: '+normal,vermelho+cnpj['status'])
	print(cyanClaro+'Tipo: '+normal,vermelho+cnpj['tipo'])
	print(cyanClaro+'complemento: '+normal,vermelho+cnpj['complemento'])
	print(cyanClaro+'Email: '+normal,vermelho+cnpj['email'])
	print(cyanClaro+'Telefone: '+normal,vermelho+cnpj['telefone'])
	print(cyanClaro+'EFR: '+normal,vermelho+cnpj['efr'])
	print(cyanClaro+'Motivo Situação: '+normal,vermelho+cnpj['motivo_situacao'])
	print(cyanClaro+'Situação Especial: '+normal,vermelho+cnpj['situacao_especial'])
	print(cyanClaro+'Situação Especial (Data): '+normal,vermelho+cnpj['data_situacao_especial'])
	print(cyanClaro+'Capital Social: '+normal,vermelho+cnpj['capital_social'])
	print(purpleClaro+'+ ================================================================================== +\n')		
################################################################################################################################
######         BIN BIN BIN BIN                                                                                             #####
################################################################################################################################
def requisicao2(titulo):

	try:
		req = requests.get('https://bins.payout.com/api/v1/bins/' + titulo)
		BIN = json.loads(req.text)
		return BIN
	
	except:
		print('Error na Conexão')
		return None

def printar_detalhesBIN(BIN):

	print('\n'+azul+'Bin Information:'+normal, vermelho+ BIN['bin']+normal )

	print(azul+'Brand Of Card:'+normal, BIN['brand'])

	print(azul+'Bank:'+normal, vermelho +BIN['issuer']+ normal)

	print(azul+'Tipo:'+normal, BIN['type'])

	print(azul+'Country:'+normal, vermelho+ BIN['country_code']+ normal+'\n')

###################################################################################################################################
####                                     Filmes Filmes Filmes                                                                 #####                       ##
####                                     Movies Movies Movies                                                                 #####                       ##
###################################################################################################################################
def requisicao4(titulo):
	try:
		req = requests.get('http://www.omdbapi.com/?t=' + titulo + '&type=movie')
		filme = json.loads(req.text)
		return filme
	
	except:
		print('Error na Conexão')
		return None
def printar_detalhesFILME(filme):
	print('\n'+azul+'Titulo:'+normal, vermelho+ filme['Title']+normal )

	print(azul+'Diretor:'+normal, filme['Director'])

	print(azul+'Atores:'+normal, vermelho +filme['Actors']+ normal)

	print(azul+'Nota:'+normal, filme['imdbRating'])

	print(azul+'Premios:'+normal, vermelho+ filme['Awards']+ normal)

	print(azul+'Poster:'+normal, filme['Poster'],'\n')

#################################################################################################################################
##   PLACAS
#################################################################################################################################
def requisicao3(titulo):

	try:
		req = requests.get('https://www.checkmeucarro.com.br/minha-conta/pesquisaGratis/pesquisar/?placa=' + titulo) # JSQ7436
		PLACA = json.loads(req.text)
		return PLACA
	
	except:
		print('Error na Conexão')
		return None

def printar_detalhesPLACA(PLACA):
	print('')
	print(amarelo+'consulta_id:'+normal+cyanClaro+ PLACA['consulta_id']+normal )

	print(amarelo+'veiculo_id:'+normal+cyanClaro+ PLACA['veiculo_id']+normal )

	print(amarelo+'Placa:'+normal+cyanClaro+ PLACA['dados_veiculo']['placa']+normal )

	print(amarelo+'marca:'+normal+ cyanClaro+PLACA['dados_veiculo']['marca']+normal )

	print(amarelo+'modelo:'+normal+cyanClaro+ PLACA['dados_veiculo']['modelo']+normal )

	print(amarelo+'chassi:'+normal+cyanClaro+ PLACA['dados_veiculo']['chassi']+normal )

	print(amarelo+'ano_fabricacao:'+normal+cyanClaro+ PLACA['dados_veiculo']['ano_fabricacao']+normal )

	print(amarelo+'ano_modelo:'+normal+ cyanClaro+PLACA['dados_veiculo']['ano_modelo']+normal )

	print(amarelo+'cor:'+normal+ cyanClaro+PLACA['dados_veiculo']['cor']+normal )

	print(amarelo+'combustivel:'+normal+ cyanClaro+PLACA['dados_veiculo']['combustivel']+normal )

	print(amarelo+'especie:'+normal+cyanClaro+ PLACA['dados_veiculo']['especie']+normal )

	print(amarelo+'procedencia:'+normal+ cyanClaro+PLACA['dados_veiculo']['procedencia']+normal )

	print(amarelo+'tipo:'+normal+cyanClaro+ PLACA['dados_tecnicos']['tipo']+normal )

	print(amarelo+'motor:'+normal+ cyanClaro+PLACA['dados_tecnicos']['motor']+normal )

	print(amarelo+'potencia:'+normal+ cyanClaro+PLACA['dados_tecnicos']['potencia']+normal )

	print(amarelo+'subsegmento:'+normal+ cyanClaro+PLACA['dados_tecnicos']['subsegmento']+normal )

	print(amarelo+'montagem:'+normal+cyanClaro+ PLACA['dados_tecnicos']['montagem']+normal )

	print(amarelo+'cambio:'+normal+cyanClaro+ PLACA['dados_tecnicos']['cambio']+normal )

	print(amarelo+'cilindrada:'+normal+cyanClaro+ PLACA['dados_tecnicos']['cilindrada']+normal )

	print('')

print('')
print(cyanClaro+Baner)
escolha = input(vermelho+"☪ Escolha uma das opções: ")
###################################################################################################
try:
	if escolha == '1':
		os.system('clear')
		print (vermelho+CNPJBANER)
		op = input(vermelho + '        ☪ Escreva Uma CNPJ Válid0: '+normal).upper()
		try:
			cnpj = requisicao(op)
			printar_detalhes(cnpj)
		except:
			print("[404] ERROR NOT FOUND! CNPJ NÃO ENCONTRADO!..[./]")
###################################################################################################
	elif escolha == '2':
		os.system('clear')
		print(purpleClaro+BINBANER)
		op = input(purpleClaro + '        ☪ Escreva Uma Bin Válida: '+normal).upper()
		try:
			BIN = requisicao2(op)
			printar_detalhesBIN(BIN)
		except:
			print("[404] ERROR NOT FOUND! Invalid bin, must be exactly 6 digits.")
###################################################################################################
	elif escolha == '3':
		os.system('clear')
		print(verde+PLACABANER)
		op = input(verde + '        ☪ Escreva Uma PLACA Válida: '+normal)
		try:
			PLACA = requisicao3(op)
			printar_detalhesPLACA(PLACA)
		except:
			print("[404] ERROR NOT FOUND! PLACA NÃO ENCONTRADA!..[./]")
#####################################################################################################
	elif escolha == '4':
		os.system('clear')
		print(amarelo+FILMESBANER)
		op = input(amarelo + '☪ Escreva Um FILME Válid0: '+normal)
		try:
			filme = requisicao4(op)
			printar_detalhesFILME(filme)
		except:
			print("[404] ERROR NOT FOUND! Filme Não Encontrado...")			
	else:
		print ("☪ Escolha uma opção valida!...")
except KeyboardInterrupt:
	print("[!] PARADO!...[;/]")

######################################################################################################
