<!--
  Perfil de Davi Cardozo — "do projeto mecânico ao software".
  Todos os gráficos são SVG autorais gerados por scripts/build.py (sem serviços externos).
  O painel de atividade é atualizado por .github/workflows/activity.yml.
-->

<picture>
  <source media="(max-width: 640px)" srcset="assets/banners/hero-mobile.svg">
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/banners/hero-static.svg">
  <img src="assets/banners/hero.svg" width="100%" alt="Davi Cardozo — precisão de engenharia, aplicada a software. Um flange de desenho técnico cujos seis furos se soltam e se tornam os nós de um diagrama de sistema: ui, api, auth, types, db e deploy. Aberto a oportunidades de estágio ou júnior.">
</picture>

<br><br>

<img src="assets/sections/01-identity.svg" width="100%" alt="01 — Identity">

Sou **Davi dos Santos Cardozo**, desenvolvedor Full Stack. Passei mais de dez anos na indústria como projetista mecânico e hoje aplico a mesma leitura de tolerância, estrutura e consequência a sistemas, em vez de peças.

**Formação** · Análise e Desenvolvimento de Sistemas (graduado) · pós em Ciência de Dados e Big Data Analytics (em curso) · Bootcamp Full Stack +praTi (em curso)<br>
**Busco** · uma oportunidade como Desenvolvedor Full Stack, Estágio ou Júnior<br>
**Base** · Rio Grande do Sul, Brasil

<br>

<img src="assets/sections/02-transition.svg" width="100%" alt="02 — The Transition">

Por mais de uma década desenhei peças mecânicas: tolerâncias milimétricas, montagens que precisam encaixar na primeira tentativa, documentação da qual outra pessoa depende para não errar. Engenharia nunca foi criatividade livre; era precisão dentro de restrições.

Migrar para software não foi um recomeço, foi uma troca de material. As perguntas continuam as mesmas (*o que pode falhar aqui? o que esta peça precisa garantir para quem monta em cima dela?*), só que agora a peça é um endpoint, uma migration, uma trava de concorrência.

<picture>
  <source media="(max-width: 640px)" srcset="assets/graphics/conversion-mobile.svg">
  <img src="assets/graphics/conversion.svg" width="100%" alt="Tabela de conversão, do projeto mecânico para o software. Tolerância dimensional vira tipos e validação (TypeScript, Zod). Encaixe na primeira montagem vira contratos de API (REST versionado, Swagger/OpenAPI). Desenho técnico vira decisões documentadas (PRD, registro de problemas, README). A pergunta 'o que pode falhar aqui?' vira concorrência e segurança (SELECT FOR UPDATE, auditoria de RBAC, IDOR e XSS).">
</picture>

<br><br>

<img src="assets/sections/03-mindset.svg" width="100%" alt="03 — Engineering Mindset">

- **Planejamento antes de código.** Escopo e prioridades são discutidos e cortados antes da primeira linha, inclusive abrindo mão de complexidade que não resolve um problema real do projeto.
- **IA como par de desenvolvimento, não como atalho.** No *Verzel Pass* e no *Elite Events Platform*, cada trecho gerado é revisado, testado manualmente e só então commitado.
- **Decisões técnicas documentadas.** O que foi escolhido, o que foi descartado e por quê fica registrado junto do código, não só na minha cabeça.
- **Segurança como etapa, não como reflexo.** O *Verzel Pass* passou por uma auditoria estática própria (isolamento de dados, RBAC, IDOR, gestão de segredos e XSS), com relatório versionado no repositório.

<br>

<img src="assets/sections/04-technology.svg" width="100%" alt="04 — Technology">

<picture>
  <source media="(max-width: 640px)" srcset="assets/graphics/bom-mobile.svg">
  <img src="assets/graphics/bom.svg" width="100%" alt="Lista de materiais. Linguagens: TypeScript, Java, JavaScript, SQL. Frontend: React, Next.js (App Router), Tailwind CSS, Vite. Backend: Node.js, Fastify, Spring Boot, Spring Security com JWT. Dados: PostgreSQL, Prisma, Flyway, Spring Data JPA. Infra: Docker, Git, Vercel, Render. Em estudo: Python, RAG, IA aplicada, Ciência de Dados.">
</picture>

<sub>Uma lista de materiais só lista o que está na montagem: cada item acima aparece no código dos projetos abaixo. A última linha é estudo, não experiência.</sub>

<br><br>

<img src="assets/sections/05-works.svg" width="100%" alt="05 — Selected Works">

<a href="https://github.com/DaviSCardozo/verzel-pass-redesign">
  <img src="assets/project-covers/verzel-pass.svg" width="100%" alt="Projeto 01 — Verzel Pass. Venda, gestão e validação de ingressos em tempo real: mapa de assentos, QR Code e controle de concorrência. Next.js 16, Fastify 5, Prisma, PostgreSQL.">
</a>

**O problema** · Duas pessoas não podem comprar o mesmo assento, e a portaria precisa saber em segundos se um ingresso é válido.<br>
**O que construí** · Projeto individual, do PRD ao deploy: compra dentro de transação com trava de linha (`SELECT … FOR UPDATE`), três papéis com RBAC (organizador, cliente e portaria), validação por QR Code com a câmera e uma auditoria de segurança própria com relatório em PDF.<br>
**Ver** · [Repositório](https://github.com/DaviSCardozo/verzel-pass-redesign) · [Demo](https://verzel-pass-redesign.vercel.app) · [Relatório de segurança](https://github.com/DaviSCardozo/verzel-pass-redesign/blob/main/docs/security-audit/relatorio-auditoria-seguranca.pdf) · [PRD](https://github.com/DaviSCardozo/verzel-pass-redesign/blob/main/docs/PRD.md)

<br>

<a href="https://github.com/DaviSCardozo/finance-control">
  <img src="assets/project-covers/finance-control.svg" width="100%" alt="Projeto 02 — FinanceControl. Controle financeiro pessoal em formato de planilha, com o saldo projetado até o fim do mês. Java 17, Spring Boot 3, React 18, PostgreSQL.">
</a>

**O problema** · O saldo de hoje não diz se o mês fecha no positivo.<br>
**O que construí** · Projeto individual: API em Spring Boot com Spring Security + JWT e migrations Flyway; interface em React com tabela estilo planilha (TanStack Table), gráficos (Recharts) e exportação para CSV. O saldo projetado soma o que já foi confirmado ao que ainda está pendente no mês.<br>
**Ver** · [Repositório](https://github.com/DaviSCardozo/finance-control) · [Demo](https://finance-control-eight-pi.vercel.app) · [API (Swagger)](https://finance-control-backend-jhdf.onrender.com/swagger-ui.html) <sub>a API hiberna quando ociosa e pode levar alguns segundos para responder</sub>

<br>

<a href="https://github.com/DaviSCardozo/elite-events-platform">
  <img src="assets/project-covers/elite-events.svg" width="100%" alt="Projeto 03 — Elite Events Platform. O desafio técnico original: eventos e ingressos com autenticação, RBAC, QR Code e API externa (TMDb). Next.js, Fastify, Prisma, PostgreSQL.">
</a>

**O contexto** · A revisão A: a entrega original de um desafio técnico, que depois evoluiu para o Verzel Pass.<br>
**Por que está aqui** · Comparar as duas revisões mostra o que mudou entre "entregue no prazo" e "revisado com calma": design system, blindagem de segurança e documentação.<br>
**Ver** · [Repositório](https://github.com/DaviSCardozo/elite-events-platform)

<sub>No laboratório: <a href="https://github.com/DaviSCardozo/daily-dev-studies">daily-dev-studies</a>, meu diário de estudos, e <a href="https://github.com/DaviSCardozo/portfolio-ia">portfolio-ia</a>, o índice dos estudos de IA aplicada.</sub>

<br><br>

<img src="assets/sections/06-focus.svg" width="100%" alt="06 — Current Focus">

<picture>
  <source media="(max-width: 640px)" srcset="assets/graphics/terminal-mobile.svg">
  <img src="assets/graphics/terminal.svg" width="100%" alt="Terminal: davi status --agora. Cursando: Bootcamp Full Stack +praTi, módulo de Java. Pós: Ciência de Dados e Big Data Analytics. Estudando: RAG e IA aplicada à engenharia de software. Buscando: Estágio ou Júnior como Desenvolvedor Full Stack.">
</picture>

<br><br>

<img src="assets/sections/07-activity.svg" width="100%" alt="07 — Activity">

<img src="assets/graphics/activity.svg" width="100%" alt="Registro de atividade no GitHub nos últimos 12 meses: contribuições por semana e distribuição de linguagens nos repositórios públicos. Painel gerado automaticamente a partir de dados reais.">

<br><br>

<img src="assets/sections/08-connection.svg" width="100%" alt="08 — Connection">

<img src="assets/banners/footer.svg" width="100%" alt="Toda peça boa começa com uma boa conversa. Persistência, visão, determinação. Próxima revisão: em andamento.">

<p align="center">
  <a href="mailto:dev.davicardozo@gmail.com"><img src="assets/icons/btn-email.svg" height="44" alt="E-mail: dev.davicardozo@gmail.com"></a>
  &nbsp;
  <a href="https://www.linkedin.com/in/davi-cardozo/"><img src="assets/icons/btn-linkedin.svg" height="44" alt="LinkedIn"></a>
  &nbsp;
  <a href="https://daviscardozo.github.io/landing-page-davi/"><img src="assets/icons/btn-portfolio.svg" height="44" alt="Portfólio"></a>
</p>
