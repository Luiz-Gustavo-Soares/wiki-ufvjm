# Wiki Colaborativa da UFVJM

## Descrição do Projeto
A Wiki Colaborativa da UFVJM é uma aplicação web desenvolvida para a criação, organização e consulta colaborativa de informações relacionadas à Universidade Federal dos Vales do Jequitinhonha e Mucuri (UFVJM). O sistema visa centralizar o conhecimento sobre cursos, disciplinas, laboratórios, projetos de extensão e eventos da comunidade acadêmica.

Este projeto foi idealizado como projeto integrador durante a Guilda Django, servindo como ambiente prático para o desenvolvimento e aplicação de conceitos de engenharia de software e desenvolvimento web.

## Arquitetura e Módulos
O sistema foi projetado com base em uma arquitetura modular, seguindo o padrão MVT (Model-View-Template) do framework Django, dividindo as responsabilidades em quatro aplicações principais:

*   **core:** Gerenciamento das configurações globais, páginas institucionais estáticas e templates base do sistema.
*   **accounts:** Módulo responsável por autenticação, registro, gestão de sessões e perfis de usuários, além do controle de permissões.
*   **wiki:** Núcleo da base de conhecimento, contemplando o fluxo de criação, edição, categorização de páginas e o armazenamento imutável do histórico de versões.
*   **events:** Gerenciamento da agenda universitária, permitindo o cadastro e a visualização de eventos integrados aos locais e entidades definidos na wiki.

## Principais Funcionalidades
*   Sistema de permissões baseado em perfis de acesso (Visitante, Comum, Colaborador, Moderador e Administrador).
*   Criação e formatação de páginas de conteúdo estruturado.
*   Versionamento automático de edições de páginas para auditoria e reversão (histórico de modificações).
*   Organização de conteúdo através de categorias hierárquicas e tags.
*   Motor de busca interno integrado ao banco de dados relacional.
*   Painel de controle de eventos e atividades acadêmicas.

## Tecnologias Utilizadas
*   **Linguagem:** Python 3
*   **Framework Back-end:** Django
*   **Banco de Dados:** PostgreSQL (Produção) / SQLite (Desenvolvimento)
*   **Front-end:** HTML5, CSS3, JavaScript
*   **Controle de Versão:** Git

## Pré-requisitos
Antes de iniciar, certifique-se de ter as seguintes ferramentas instaladas em seu ambiente local:
*   Python 3.12 ou superior
*   Pip (Gerenciador de pacotes do Python)
*   Git
*   Virtualenv (Recomendado para isolamento de dependências)
