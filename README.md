# 💰 Assessor Financeiro Inteligente por Voz com IA

> "A maioria dos brasileiros admite que entende pouco ou nada de educação financeira, mas reconhece que o tema é muito importante" — Febraban (2025)

![Google Colab](https://img.shields.io/badge/Status-Concluído-success)
![Technology](https://img.shields.io/badge/AI-Google%20Gemini%20%2B%20Edge%20TTS-blue)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)

## 🎯 O Desafio & Motivação

Este projeto nasceu da necessidade de aplicar conceitos e práticas de Inteligência Artificial para resolver um problema crítico da sociedade brasileira: **a falta de literacia financeira**.

Segundo dados da **[Federação Brasileira de Bancos(Febraban)](https://portal.febraban.org.br/noticia/4324/pt-br/)**, a maioria da população admite ter pouco conhecimento sobre como gerir seu dinheiro, o que gera insegurança e estresse familiar.

**A Solução:**
Desenvolvi um **Assessor Financeiro por Voz** acessível, que atua como um "Gerente Pessoal de Bolso". Ele não apenas responde dúvidas, mas **orienta ativamente** o usuário sobre alocação de orçamento e tipos de investimento, usando linguagem natural e empática.

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

## 📄 Como Executar

1.  Clone este repositório.
2.  Instale as dependências:
    ```bash
    pip install google-genai edge-tts
    ```
3.  Defina sua `GOOGLE_API_KEY` no script.
4.  Execute o notebook no Google Colab e permita o acesso ao microfone.

---
*Projeto desenvolvido como aplicação prática de IA Generativa para o setor financeiro.*
