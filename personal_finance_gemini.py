language = 'pt'
# Captura de Áudio
from IPython.display import Audio, display, Javascript
from google.colab import output
from base64 import b64decode

# Código JavaScript para gravar áudio do usuário usando a "MediaStream Recording API"
RECORD = """
const sleep  = time => new Promise(resolve => setTimeout(resolve, time))
const b2text = blob => new Promise(resolve => {
  const reader = new FileReader()
  reader.onloadend = e => resolve(e.srcElement.result)
  reader.readAsDataURL(blob)
})
var record = time => new Promise(async resolve => {
  stream = await navigator.mediaDevices.getUserMedia({ audio: true })
  recorder = new MediaRecorder(stream)
  chunks = []
  recorder.ondataavailable = e => chunks.push(e.data)
  recorder.start()
  await sleep(time)
  recorder.onstop = async ()=>{
    blob = new Blob(chunks)
    text = await b2text(blob)
    resolve(text)
  }
  recorder.stop()
})
"""

def record(sec=5):
  # Executa o código JavaScript para gravar o áudio
  display(Javascript(RECORD))
  # Recebe o áudio gravado como resultado do JavaScript
  js_result = output.eval_js('record(%s)' % (sec * 1000))
   # Decodifica o áudio em base64
  audio = b64decode(js_result.split(',')[1])
  # Salva o áudio em um arquivo
  file_name = 'request_audio.wav'
  with open(file_name, 'wb') as f:
    f.write(audio)
  # Retorna o caminho do arquivo de áudio (pasta padrão do Google Colab)
  return f'/content/{file_name}'

# Grava o áudio do usuário por um tempo determinado (padrão 5 segundos)
print('Ouvindo...\n')
record_file = record()

# Exibe o áudio gravado
display(Audio(record_file, autoplay=False))

# Trasnscrição do áudio via Gemini
!pip install -q -U google-genai
from google import genai
import os

# --- 1. Configuração ---
GOOGLE_API_KEY = "AIzaSyBJk7QiX1GClYORU6DOe7NOP0HhofQAu9o"
client = genai.Client(api_key=GOOGLE_API_KEY)

# --- 2. Função de Transcrição ---
def transcrever_audio(caminho_arquivo):
    # Verifica se o arquivo existe
    if not os.path.exists(caminho_arquivo):
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return None

    print(f"1. Processando o áudio: {caminho_arquivo}")

    try:
        # Upload do arquivo para o Gemini
        arquivo_upload = client.files.upload(file=caminho_arquivo)
        print("2. Áudio enviado. Gerando transcrição...")

        # Solicita a transcrição ao modelo Flash
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                arquivo_upload,
                "Transcreva este áudio exatamente como foi falado."
            ]
        )

        return response.text

    except Exception as e:
        print(f"Erro na API: {e}")
        return None

# --- 3. Execução ---
if 'record_file' in locals():
    texto_usuario = transcrever_audio(record_file)

    if texto_usuario:
        print("\n--- Transcrição do áudio ---")
        print(texto_usuario)
        print("------------------------------")
else:
    print("A variável 'record_file' não foi encontrada. Envie um novo áudio.")

# Interagindo com o Gemini
# --- 1. Definição da Personalidade e Objetivo (Prompt) ---
prompt_sistema = """
Você é um Assessor Financeiro Pessoal focado em maximizar riqueza e realizar sonhos e desejos.
Sua missão vai além de explicar conceitos: você deve ajudar o usuário a alocar seus recursos na prática.

Diretrizes de comportamento:
1. ATITUDE: seja amigável, motivador e extremamente prático. Fale como um parceiro experiente.
2. ALOCAÇÃO: se o usuário informar valores (salário, gastos, dívidas), sugira divisões inteligentes (ex: regra 50-30-20) para que ele possa economizar, investir e viajar.
3. CONCISÃO: responda em no máximo 5 frases curtas. O usuário está te ouvindo por áudio, não lendo um e-mail.
4. INVESTIMENTOS: explique e sugira TIPOS de investimentos disponíveis no Brasil (CDB, Tesouro Direto, LCI/LCA, Fundos), adequados ao perfil que o usuário demonstrar considerando a resolução Comissão de Valores Mobiliários nº 30/2021.
5. RESTRIÇÃO CRÍTICA: NUNCA recomende a compra de ativos específicos (ex: "Compre ações da empresa X"). Apenas a classe do ativo.
6. SEGURANÇA: baseie-se em boas práticas de mercado, instituições como ANBIMA, CVM e Bradesco e fontes caracterizadas como seguras e responsáveis. Se a pergunta for muito específica ou jurídica e você não tiver certeza, diga: "Eu não sei. Fale com o gerente do seu banco para que ele possa te orientar de forma efetiva"
"""
# --- 2. Gera Resposta ---
def gerar_resposta_financeira(texto_pergunta):
    print("1. Hummm vou pensar e já te respondo...")

    try:
        # Combina a instrução com a pergunta do usuário
        conteudo_completo = f"{prompt_sistema}\n\nUsuário perguntou: {texto_pergunta}"

        # Envia para o modelo
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=conteudo_completo
        )

        return response.text

    except Exception as e:
        print(f"Erro na geração da resposta: {e}")
        return "Desculpe, não consegui processar sua resposta agora. Faça sua pergunta novamente, por gentileza"

# --- 3. Execução ---
# Verifica se há a transcrição do passo anterior
if 'texto_usuario' in locals() and texto_usuario:
    print(f"Pergunta original: '{texto_usuario}'")

    resposta_gemini = gerar_resposta_financeira(texto_usuario)

    print("\n--- Aqui está sua resposta ---")
    print(resposta_gemini)
    print("--------------------------")
else:
    print("Nenhum texto encontrado. Por favor, rode a etapa de transcrição primeiro.")

# Interação em áudio com o Edge TTS
# 1. Instalação da biblioteca Edge TTS
!pip install -q edge-tts

import edge_tts
from IPython.display import Audio, display

# 2. Função para gerar o áudio natural
async def gerar_audio_final(texto):
    if not texto:
        print("Erro: Não há texto para ler.")
        return None

    print(f"Gerando áudio para: ... ")

    # Escolha da voz ("pt-BR-FranciscaNeural" ou "pt-BR-AntonioNeural")
    VOZ = "pt-BR-FranciscaNeural"
    arquivo_saida = "/content/resposta_final_neural.mp3"

    # Geração
    communicate = edge_tts.Communicate(texto, VOZ)
    await communicate.save(arquivo_saida)

    print("✅ Áudio pronto. Ouça abaixo:")
    display(Audio(arquivo_saida, autoplay=True))

# 3. Execução
# Pegamos a variável 'resposta_gemini' que foi gerada no seu passo anterior
if 'resposta_gemini' in locals() and resposta_gemini:
    # O comando 'await' é necessário aqui pois a biblioteca é assíncrona
    await gerar_audio_final(resposta_gemini)
else:
    print("A variável 'resposta_gemini' não foi encontrada. Verifique se a etapa de geração de texto foi concluída.")
