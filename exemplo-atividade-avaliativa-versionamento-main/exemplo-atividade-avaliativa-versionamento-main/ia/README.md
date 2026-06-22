# 🤖 Inteligência Artificial (IA)

## 📝 Descrição do Projeto/Atividade

Este projeto utiliza Inteligência Artificial integrada a APIs externas para automatizar a geração de imagens personalizadas. O sistema realiza o upload de uma imagem para um servidor temporário, envia a URL da imagem para uma API de geração gráfica e, posteriormente, faz o download automático do resultado final.

A aplicação demonstra a integração entre Python, APIs REST e automação de tarefas digitais utilizando recursos modernos amplamente utilizados no mercado.

---

## 🧠 Reflexão de Aprendizado

### 1. O que aprendi?

Durante esta atividade aprendi conceitos importantes relacionados à Inteligência Artificial e integração de serviços online, como:

* Consumo de APIs REST utilizando Python.
* Envio e recebimento de dados em formato JSON.
* Upload automático de arquivos para servidores externos.
* Manipulação de respostas de APIs.
* Automação de geração de conteúdo digital.
* Tratamento de erros em requisições HTTP.
* Integração entre múltiplos serviços online.
* Estruturação de aplicações que utilizam recursos de IA.

Além disso, compreendi como sistemas modernos utilizam APIs para automatizar tarefas que antes exigiam intervenção manual.

---

### 2. Para que serve (Por que aprendi)?

A Inteligência Artificial e a automação estão cada vez mais presentes em sistemas empresariais e aplicações web.

Esse conhecimento permite:

* Automatizar processos repetitivos.
* Gerar conteúdo digital de forma rápida.
* Integrar sistemas com serviços externos.
* Criar soluções escaláveis para empresas.
* Reduzir tempo e custos operacionais.
* Desenvolver aplicações inovadoras utilizando IA.

No mercado atual, tecnologias semelhantes são utilizadas em geração de imagens, chatbots, análise de dados, marketing digital e automação de processos.

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

* Python 3
* Requests
* APIs REST
* JSON
* Catbox API
* DynaPictures API
* Visual Studio Code

---

## 💻 Demonstração e Como Rodar

### Código Relevante Comentado

```python
import requests

url_api = f"https://api.dynapictures.com/designs/{template_id}"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

payload = {
    "format": "png",
    "params": [
        {
            "name": "Title",
            "text": "Agora a imagem vai carregar!"
        }
    ]
}

response = requests.post(
    url_api,
    headers=headers,
    json=payload
)
```

### Explicação

* `requests.post()` realiza a comunicação com a API.
* `headers` contém a chave de autenticação.
* `payload` define os parâmetros enviados.
* A API processa os dados e retorna a imagem gerada.
* O sistema realiza o download automático do resultado final.

---

## 🚀 Instruções para Executar

### Instalar dependências

```bash
pip install requests
```

### Configurar o projeto

Defina sua chave de API e o Template ID dentro do código:

```python
api_key = "SUA_API_KEY"
template_id = "SEU_TEMPLATE_ID"
```

Adicione a imagem que será utilizada no mesmo diretório do projeto.

---

### Executar o sistema

```bash
python app.py
```

---

## 🎯 Resultado Esperado

Ao executar o programa:

1. A imagem será enviada para um servidor temporário.
2. A URL gerada será enviada para a API.
3. A API criará automaticamente uma nova imagem personalizada.
4. O arquivo final será baixado e salvo como:

```text
resultado.png
```

---

## ✅ Conclusão

Esta atividade permitiu compreender na prática como aplicações modernas utilizam APIs e recursos de Inteligência Artificial para automatizar tarefas. O projeto demonstrou conceitos importantes de integração de sistemas, processamento de dados e geração automática de conteúdo digital, habilidades cada vez mais valorizadas no mercado de tecnologia.
