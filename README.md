# Gerador de texto para clientes usando AI

Esse repositório contém o cógido e um arquivo CSV basico para um gerador de texto.

O arquivo CSV contém algumas informações de clientes fictícios de operadoras de telefonia, como nome, número, operadora que ele utiliza, etc..

O objetivo aqui é criar uma mensagem personalizada para cada cliente, utilizando a API do ChatGPT. Para isso, foi levado em consideração qual o tipo do plano que o cliente possui(pré pago, controle ou pós pago). No caso do pós pago, a mensagem seria somente um agradecimento por utilizar o plano, já que não há melhoria para esse tipo de plano.

No final, o programa atualiza o arquivo CSV de origem com a mensagem criada pela AI.
