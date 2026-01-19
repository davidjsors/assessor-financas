# 💰 Assessor Financeiro Inteligente por Voz com IA

> "A maioria dos brasileiros admite que entende pouco ou nada de educação financeira, mas reconhece que o tema é muito importante" — Febraban (2025)

![Google Colab](https://img.shields.io/badge/Google_Colab-00599C?style=for-the-badge&logo=google-colab&logoColor=white)
![Technology](https://img.shields.io/badge/AI-Google%20Gemini%20%2B%20Edge%20TTS-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 🎯 O Desafio & Motivação

Este projeto nasceu do meu desejo de aplicar conceitos e práticas de Inteligência Artificial e Python, apreendidos no Boootcamp Bradesco - GenAI & Dados (DIO), para resolver um problema crítico da sociedade brasileira: **a falta de literacia financeira**.

Segundo dados da **[Federação Brasileira de Bancos(Febraban)](https://portal.febraban.org.br/noticia/4324/pt-br/)**, a maioria da população admite ter pouco conhecimento sobre como gerir seu dinheiro, o que gera insegurança e estresse familiar.

**A Solução:**
um **Assessor Financeiro por Voz** acessível, que atua como um "Gerente Pessoal de Bolso". Ele não apenas responde dúvidas, mas **orienta ativamente** o usuário sobre alocação de orçamento e tipos de investimento, usando linguagem natural e empática.

## 💡 Stack

Este projeto implementa uma arquitetura **Lean & Powerful** no Google Colab:

1.  **Google Gemini (Multimodal):** atua duplamente como o ouvido (Speech-to-Text) e o cérebro (Consultor Financeiro), reduzindo latência e custos.
2.  **Microsoft Edge TTS:** substitui vozes robóticas antigas por uma **Voz Neural (Francisca)** de alta fidelidade, garantindo uma experiência humanizada.

## 🛠️ Como Funciona

1.  **Captura:** o usuário fala suas dúvidas ou situação financeira (ex: "Ganho R$ 3.000 e gasto tudo").
2.  **Processamento:** O áudio é transcrito e analisado pelo Gemini com um prompt de sistema especializado em *Finanças Pessoais*.
3.  **Resposta:** a IA gera um plano de ação prático e o converte em áudio neural para o usuário ouvir.

## 🚀 Tecnologias Utilizadas

* **Linguagem:** Python
* **IA Generativa:** Google GenAI SDK (Gemini 2.5 Flash)
* **Síntese de Voz:** Edge TTS (pt-BR-FranciscaNeural
* **Frontend/Captura:** JavaScript (integração via Browser/Colab)

## 💻 Como Executar

Este projeto foi otimizado para rodar diretamente na nuvem via **Google Colab**, eliminando a necessidade de configurações complexas de ambiente local.

### Passo a Passo

1.  **Acesse o Google Colab:**
    * Crie um novo notebook em [colab.research.google.com](https://colab.research.google.com/).

2.  **Prepare a API Key:**
    * Gere sua chave gratuita no [Google AI Studio](https://aistudio.google.com/).

3.  **Execute o Código:**
    * Copie o script contido no arquivo `personal_finance_gemini.py` deste repositório.
    * Cole em uma célula de código do Colab.
    * Substitua `GOOGLE_API_KEY = "..."` pela sua chave real.
    * Pressione `Play` (ou `Ctrl + Enter`).

4.  **Interaja:**
    * Permita o acesso ao microfone quando o navegador solicitar.
    * Fale sua dúvida financeira (ex: *"Como começar uma reserva de emergência?"*).
    * Aguarde a resposta em áudio e texto.

---
*Projeto desenvolvido como aplicação prática de IA Generativa para o setor financeiro.*
