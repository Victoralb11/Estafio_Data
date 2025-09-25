import pandas as pd

data = pd.read_csv('tb_geral.csv')

media_pago = data['pago'].sum() / data.shape[0]

data['maior_que_media'] = data['pago'] > media_pago

filtro_nome_unidade = data['nome_unidade'] == 'Agência Espacial Brasileira'

filtro_data = (data['data_ano'] >= 2004) & (data['data_ano'] <= 2020)

filtro_dotacao_pago = (data['dotacao_atual'] > 0) & (data['pago'] > 0)

filtros_aplicados = filtro_nome_unidade & filtro_data & filtro_dotacao_pago & data['maior_que_media']

data_filtrada = data[filtros_aplicados]

data_filtrada['dotacao_atual'] = 'R$ ' + data_filtrada['dotacao_atual'].astype(str)

data_filtrada.columns = [col.capitalize() for col in data_filtrada.columns]

data_filtrada.to_csv('dados_filtrados.csv', index=False)

print("Novo CSV gerado com sucesso!")
