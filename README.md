# Desafio 09 | Banco do Brasil

## 1 - Introdução
O Banco do Brasil, maior banco da América Latina, com destaque em segmentos como agronegócio, infraestrutura, micro e pequenas empresas.
O seu maior propósito é estar próximo das pessoas e ajudar a preservar o que é importante para seus clientes, acionistas, funcionários e toda a sociedade.
Por esta razão, pensando no pequeno e médio agricultor, que muitas vezes não tem acesso, desconhece ou não tem capacidade financeira para contratar soluções robustas que os auxiliem na gestão e monitoramento de seus processos produtivos, o Banco do Brasil quer desenvolver solução de baixo custo, para que estes proprietários através do controle de temperatura e umidade do solo, possam planejar melhor sistemas de irrigação baseado no tipo do produto, além de sistema de reconhecimento de pragas e qualidade do plantio através de processamento de imagens capturadas com drones.


## 2 - Desafio
Nesta solução deverá ser usado, kit com microcontrolador com sensor de temperatura ambiente e umidade do solo, Watson IoT Platform para integração e gerenciamento dos sensores / devices, container na plataforma OpenShift para hospedar programa de gerenciamento e controle, desenvolvido em Python com Flask, Watson Studio para desenvolvimento de modelos de aprendizado de máquina profundo, utilizando Jupyter Notebook e Python, Watson Machine Learning para utilização do modelo gerado, e novamente container em OpenShift para expor API em Python com Flask para processar as imagens.

<div align="center">
    <img width="750" src="assets/arquitetura-iot.png" />
    <p>Imagem 1: Arquitetura IOT.</p>
</div>
<div align="center">
    <img width="750" src="assets/arquitetura-ai.png" />
    <p>Imagem 2: Arquitetura AI.</p>
</div>
<br>
<br>
<br>


## 3 - Pré-requisitos

Você deverá cumprir os seguintes itens:

- Instalar e configurar [Python 3.6](https://www.python.org/downloads/release/python-360/) ou mais recente;
- Instalar e configurar o [Postman](https://www.getpostman.com/downloads/) para testar sua solução;
- Ter uma conta no [GitHub](https://github.com/) ou criar uma nova;
- Ter Conhecimentos gerais de [Tensor Flow](https://www.tensorflow.org/api_docs), [Keras](https://keras.io/) e [Numpy](https://www.numpy.org/doc/); 
- Ter conhecimentos gerais em [Red Hat OpenShift](https://learn.redhat.com/) para subir a aplicação;

## License

Copyright 2019 Maratona Behind the Code

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
