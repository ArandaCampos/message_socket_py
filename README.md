## Message Socket Py
![Badge de licença](http://img.shields.io/static/v1?label=LICENÇA&message=GNU&color=sucess&style=for-the-badge)   ![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=CONCLUÍDO&color=sucess&style=for-the-badge)   ![Badge versionamento](http://img.shields.io/static/v1?label=VERSAO&message=1.0&color=sucess&style=for-the-badge)

### Sobre

&emsp;`Message Socket Py` é um script Python que cria um serviço para troca de mensagens. No projeto foi usado o protocolo UDP (User Data Protocol), não orientado à conexão, e com formato de enderço IPv4. 

### Bora ver como o projeto ficou?

![message_socket_py](https://user-images.githubusercontent.com/87876734/183315361-67d6209c-ff31-43ee-9000-dfc3bf9f1663.gif)

### Pré-requisitos

  - Python >= 3.8
  
### Instalação
  
    # Clone o repositório
    >> git clone https://github.com/ArandaCampos/message_socket_py.git

    # Crie um ambiente virtual
    >> cd message_socket_py
    >> virtualenv .
    >> source bin/activate

    # Instale as dependências
    (message_socket_py) >> pip install -r requirements.txt
    
    # Para rodar o servidor
    (message_socket_py) >> python message_socket_py/server/server.py
    
    # Para rodar o lado cliente
    (message_socket_py) >> python message_socket_py/client/client.py
  
### Tecnologias empregadas
  - Python
    - Socket
    - Threading
    - signal
