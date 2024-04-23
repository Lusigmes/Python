import streamlit as st
import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
import psycopg2

#instalar conda e python
#conda create -n stenv python=3.11
#conda activate stenv
#pip install streamlit
#pip install psycopg2
#pip install psycopg2-binary
#pip show psycopg2
#pip install pandas
#pip instal matplotlib

hostDB = "localhost"
portDB = 5432
nameDB = "sindrome_gripal_leve2022"
userDB = "postgres"
pswDB = "1234"

#conexão
def connection():
	conn = psycopg2.connect(
		host=hostDB,
		port=portDB,
		database=nameDB,
		user=userDB,
		password=pswDB
	)
	return conn

#executar consulta sql e retornar dataframe
def run_query(query):
	conn = connection()
	df = pd.read_sql(query, conn)
	conn.close()

	return df

conn = connection()

st.title('Consultas: Notificações de Sindrome Gripal Leve 2022 - SP')

#Opções de consulta
consulta_opcoes = ['Consulta 1','Consulta 2', 'Consulta 3','Consulta 4']
consulta_selecionada = st.sidebar.selectbox('Selecione a consulta', consulta_opcoes)

#exibir resultados da consulta selecionada
def resultados():
	#consulta 1 OK
	if consulta_selecionada == 'Consulta 1':
		query = '''
				select i.racaCor, round(avg(i.idade), 0) as idade_media
				from individuo i inner join situacao s
				on i.source_id = s.source_id
				where i.racaCor in ('Parda','Branca')
				group by i.racaCor;

		'''
		df = run_query(query)

		#Exibir em tabela
		st.subheader('Tabela da Consulta 1\nSelecionar a idade média dos indivíduos por raça/cor, limitando aos registros das raças/cor "Parda" e "Branca".')
		st.dataframe(df)

		#Exibir gráfico de barras
		st.subheader("Gráfico da Consulta 1")
		fig, ax = plt.subplots()
		ax.bar(df['racacor'], df['idade_media'])
		ax.set_xlabel('Raça')
		ax.set_ylabel('Idade')
		ax.set_title("Idade média de invidíduos pardos e brancos")
		st.pyplot(fig)

	#consulta 2 OK
	elif consulta_selecionada == 'Consulta 2':
		query = ''' 
				select i.racaCor,count(*) as quantidade_registros from individuo i
				inner join situacao s on i.source_id = s.source_id 
				where s.sintomas like '%Febre%' and s.dataPrimeiraDose is not null and s.dataSegundaDose is not null
				group by i.racaCor order by i.racaCor asc;

		'''
		df = run_query(query)

		#exibir tabela
		st.subheader('Tabela da Consulta 2\nSelecionar a raça e a quantidade de registros que possuem febre, e que tomaram a primeira e seguda dose.')
		st.dataframe(df)

		#removendo os valores nulos('None')
		df = df.dropna()

		#Exibir gráfico de barra
		st.subheader("Gráfico da Consulta 2")
		fig, ax = plt.subplots()
		ax.bar(df['racacor'], df['quantidade_registros'])
		ax.set_xlabel('Raça')
		ax.set_ylabel('Quantidade de registros')
		ax.set_title("Distribuição da quantidade por raça de indivíduos que tiveram febre e tomaram a primeira e segunda dose.")
		st.pyplot(fig)

	#consulta 3 OK
	elif consulta_selecionada == 'Consulta 3':
		query = '''
			select i.estado, min(i.idade) as idade_Min, max(i.idade) as idade_Max
			from individuo i inner join situacao s on i.source_id = s.source_id
			where i.racaCor='Ignorado' group by i.estado;
		'''
		df = run_query(query)

		#Exibir tabela
		st.subheader('Tabela da Consulta 3\nSelecionar o estado, idade mínima, idade máxima dos indivíduos por estado, cuja raça não foi especificado(ignorado).')
		st.dataframe(df)


		#substituir nulos por 0
		#df['idade_max'] = df['idade_max'].dropna(float)
		#df['idade_max'] = df['idade_max'].astype(float)
		df = df.dropna()

		#Exibir gráfico de barras
		st.subheader("Gráfico da Consulta 3")
		fig, ax = plt.subplots()
		ax.bar(df['estado'], df['idade_min'], label='Idade Mínima')
		ax.bar(df['estado'], df['idade_max'], label='Idade Máxima')
		ax.set_xlabel('Estado')
		ax.set_ylabel('Idade')
		ax.set_title("Idade Mínima e Máxima de indivíduos por estado cuja raça não foi especificada(Ignorada).")
		st.pyplot(fig)

	#consulta 4 OK
	elif consulta_selecionada == 'Consulta 4':
		query = '''
				select distinct(i.estado), count(*) as quantidade_descartados
				from individuo i inner join datas_doses dd on i.source_id = dd.source_id
				where dd.classificacaoFinal='Descartado'
				and dd.dataInicioSintomas !='None'and dd.dataEncerramento!='None'
				group by i.estado order by quantidade_descartados asc limit 5;
		'''
		df = run_query(query)

		#Exibir Tabela
		st.subheader('Tabela da Consulta 4\nSelecionar os cinco primeiros estados e a quantidade de registros que cuja classificacao final foi dada como descartado, e que tiveram o inicio e fim dos sintomas registrados')
		st.dataframe(df)

		#Exibir gráfico de barras
		st.subheader("Gráfico da Consulta 4")
		fig, ax = plt.subplots()
		ax.bar(df['estado'], df['quantidade_descartados'])
		ax.set_xlabel('Estado')
		ax.set_ylabel('Quantidade de registros descartados')
		ax.set_title('Quantidade dos cinco primeiros registros classificados como descartados por estado')
		st.pyplot(fig)

	#

	#

if consulta_selecionada:
	resultados()

#conn.close()
