# Material Tracker

## Descrição

**Material Tracker** é uma aplicação desenvolvida para ajudar uma empresa de óleo e gás a gerenciar o inventário de materiais entre diferentes projetos de instalação de estruturas submarinas. O objetivo é facilitar a reutilização de materiais entre os projetos, permitindo que representantes registrem itens de seu escopo e busquem equipamentos de outros projetos que possam ser reaproveitados. A transferência de itens ocorre através de transações financeiras entre os projetos.

## Motivação

Com o aumento de projetos no setor de óleo e gás, a reutilização de materiais se tornou essencial para reduzir custos e otimizar recursos. O Material Tracker oferece uma plataforma centralizada para que cada projeto gerencie seus materiais e facilite a transferência e o reaproveitamento de recursos.

## Funcionalidades

- **Gerenciamento de Usuários por Projetos**  
  Os usuários pertencem a grupos, cada um representando um projeto.

- **Criação de Itens**  
  Representantes podem criar itens no inventário, preenchendo informações detalhadas sobre cada material.

- **Campos dos Itens**  
  Cada item possui:
  - Data de disponibilidade para reuso
  - Localização atual do material
  - Custo estimado

- **Gestão de Localização**  
  Usuários podem atualizar a localização dos materiais pertencentes ao seu projeto.

- **Reserva de Itens**  
  É possível reservar itens disponíveis em datas específicas. Itens podem ter múltiplas reservas feitas em datas distintas.

- **Acesso a Reservas**  
  Cada projeto pode visualizar as reservas realizadas pelo seu grupo.

## Páginas da Aplicação

1. **Página de Login**  
   Acesso seguro para os usuários cadastrados.

2. **Página Inicial**  
   Visão geral das funcionalidades principais.

3. **Página de Inventário**  
   Exibe uma tabela de todos os itens registrados.
   - Filtrar a tabela pelo valor de qualquer coluna.
   - Atualizar a localização de vários itens simultaneamente.

4. **Página do Item**  
   Exibe todas as informações detalhadas de um item específico.
   - Permite visualização e realização de reservas para o item.

5. **Página de Reserva**  
   Escolha das datas disponíveis para realizar reservas.

6. **Página do Projeto**  
   Exibe indicadores de performance (KPIs) para monitoramento do projeto:
   - Quantidade de itens pertencentes ao projeto.
   - Quantidade de itens vendidos para outros projetos.
   - Quantidade de itens comprados de outros projetos.
   - Valor total das vendas.
   - Valor total das compras.

## Tecnologias Utilizadas

- **Back-end**: (Escolha de framework)
- **Front-end**: (Tecnologia de UI)
- **Banco de Dados**: (Banco de dados utilizado)
- **Hospedagem**: (Serviço de hospedagem, se aplicável)

## Como Contribuir

Contribuições são bem-vindas! Siga os passos abaixo para colaborar:

1. Realize um fork deste repositório.
2. Crie uma branch para a nova feature (`git checkout -b feature/nome-da-feature`).
3. Faça o commit das alterações (`git commit -m 'Descrição da feature'`).
4. Envie a branch (`git push origin feature/nome-da-feature`).
5. Abra um Pull Request.

---

Este README fornece um guia para o uso e desenvolvimento do Material Tracker, ajudando a manter a aplicação organizada e eficiente para seus usuários.
