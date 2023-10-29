import pandas as pd
import openai
import csv
from time import sleep

#GET
df = dict()
filename="lista_clientes.csv"
with open(filename,'r') as data:
    dict_reader = csv.DictReader(data)
    df = list(dict_reader)

id_usuario = int(input(f'De qual usuário deseja escrever uma mensagem? (1 a {len(df)}, 0 para todos) '))

def get_user(id):
    if id_usuario < 0:
        id -= 1
    response = (f'''ID do cliente: {df[id]['user_id']}
Nome do cliente: {df[id]['nome']}
Número do cliente: {df[id]['numero_celular']}                
Operadora do cliente: {df[id]['operadora_celular']}
Plano de celular do cliente: {df[id]['plano_tipo']}    
Valor gasto por mes: {df[id]['gasto_por_mes']}  ''')
    return response
    
#TRANSFORM
openai_api_key = str(input('Cole sua chave da OpenAI: '))
openai.api_key = openai_api_key

def generate_ai_news(user):
    user -= 1
    if df[user]['plano_tipo'] == 'pre':
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[
        {
            "role": "system",
            "content": "Você é um cliente de plano de dados móveis."
        },
        {
            "role": "user",
            "content": f"Crie uma mensagem para {df[user]['nome']} oferecendo um plano controle de internet móvel da {df[user]['operadora_celular']} (máximo de 100 caracteres)"
        }
        ]
  )
    if df[user]['plano_tipo'] == 'con':
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[
        {
            "role": "system",
            "content": "Você é um cliente de plano de dados móveis."
        },
        {
            "role": "user",
            "content": f"Crie uma mensagem para {df[user]['nome']} oferecendo um plano pós pago de internet móvel da {df[user]['operadora_celular']} (máximo de 100 caracteres)"
        }
        ]
  )
    if df[user]['plano_tipo'] == 'pos':
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=[
            {
                "role": "system",
                "content": "Você é um cliente de plano de dados móveis."
            },
            {
                "role": "user",
                "content": f"Crie uma mensagem para {df[user]['nome']} agradecendo por utilizar um plano pós pago da {df[user]['operadora_celular']} (máximo de 150 caracteres)"
            }
            ]
    )
    return completion.choices[0].message.content.strip('\"')

#LOAD
if 0 < id_usuario <= len(df):
    news = generate_ai_news(id_usuario)
    df[id_usuario - 1]['news'] = (news)
    print(get_user(id_usuario))
    print(f'Mensagem para o cliente: {news}')
    print('')
    print('Gerando o arquivo...')
    sleep(5)
elif id_usuario == 0:
    for c in range(0, len(df)):
        news = generate_ai_news(c + 1)
        df[c]['news'] = (news)
        print(get_user(c))
        print(f'Mensagem para o cliente: {news}')
        sleep(20)
        print('')
    print('Gerando o arquivo...')
    sleep(5)

df_atualizado = pd.DataFrame(df)
print(df_atualizado)
df_atualizado.to_csv(filename, index=False)
print('Arquivo CSV criado.')
input()
