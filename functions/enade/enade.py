from openai import OpenAI
import json

# Faz uma pesquisa na web para encontrar referências sobre o assunto
def search(curso, assunto, openai_api_key):

    client = OpenAI(api_key = openai_api_key)

    with open("functions/enade/enade_search.json", "r") as file: schema = json.load(file)

    prompt = f"""
    Você é um autor conteudista da educação superior, encarregado de elaborar questões de múltipla escolha para serem usadas em avaliações do aprendizado do aluno.
    Nesse momento, você deverá fazer uma pesquisa na web para encontrar uma referência que sirva como texto-base para a elaboração da questão.
    O texto-base é um elemento que propicia a reflexão sobre um assunto, um contexto, uma situação ou um tema, subsidiando o estudante nos processos de análise e de resolução da questão. O texto-base motiva ou compõe a situação-estímulo ou o caso que será objeto de avaliação da questão. 
    Encontre até 10 notícias na imprensa ou artigos científicos para a prova de {curso} sobre "{assunto}".
    """

    model="gpt-4.1-mini"
    response = client.responses.create(
        model=model, 
        input=prompt, 
        tools=[{"type": "web_search_preview"}],
        text=schema
    )

    response_json = json.loads(response.output_text)
    # return response_json
    return response_json.get("urls", [])

# Cria uma questão do Enade com base no curso, assunto, características, competências, texto-base e tipo de questão
def create(curso, assunto, caracteristicas, competencias, texto_base, tipo, nivel, openai_api_key):
    
    client = OpenAI(api_key = openai_api_key)

    with open(f"functions/enade/enade_create_{tipo}.json", "r", encoding="utf-8") as file: schema = json.load(file)
    with open(f"functions/enade/enade_create_{tipo}.txt", "r", encoding="utf-8") as file: instructions = file.read()

    type = "resposta única"
    if tipo == 1:
        type = "múltipla escolha"
    elif tipo == 2:
        type = "asserção razão"

    prompt = f"""
    Você é um autor conteudista da educação superior, encarregado de elaborar questões de múltipla escolha para serem usadas em avaliações do aprendizado do aluno.
    As questões devem ser elaboradas no padrão do Enade (Exame Nacional de Desempenho de Estudantes).
    Você deverá criar uma questão do tipo "{type}" para a prova do curso de "{curso}" sobre o assunto "{assunto}".
    A questão deverá ser elaborada considerando as seguintes características do perfil do egresso: {caracteristicas}.
    As competências a serem avaliadas são: {competencias}.
    O grau de dificuldade da questão deverá ser {nivel}.
    Conisere esse texto-base: {texto_base}.
    Elabore cinco alternativas de resposta, mas não coloque A, B, C, D ou E antes de cada alternativa.
    A resposta correta deverá ser A, B, C, D ou E.
    Siga essas instruções:
    {instructions}
    """

    model="gpt-4.1-mini"
    response = client.responses.create(
        model=model, 
        input=prompt, 
        text=schema
    )
    
    response_json = json.loads(response.output_text)

    enunciado = response_json["enunciado"]

    if tipo == 1:
        enunciado += "\n\n"
        enunciado += "I. " + response_json["afirmacao_1"] + "\n\n"
        enunciado += "II. " + response_json["afirmacao_2"] + "\n\n"
        enunciado += "III. " + response_json["afirmacao_3"] + "\n\n"
        enunciado += "IV. " + response_json["afirmacao_4"] + "\n\n"
        enunciado += "É correto apenas o que se afirma em:"

    elif tipo == 2:
        enunciado += "\n\n"
        enunciado += "I. " + response_json["assercao_1"] + "\n\n"
        enunciado += "PORQUE\n\n"
        enunciado += "II. " + response_json["assercao_2"] + "\n\n"
        enunciado += "A respeito dessas asserções, assinale a opção correta."

    response_obj = {
        "enunciado": enunciado,
        "alternativa_1": response_json["alternativa_1"],
        "alternativa_2": response_json["alternativa_2"],
        "alternativa_3": response_json["alternativa_3"],
        "alternativa_4": response_json["alternativa_4"],
        "alternativa_5": response_json["alternativa_5"],
        "correta": response_json["correta"],
        "justificativa_1": response_json["justificativa_1"],
        "justificativa_2": response_json["justificativa_2"],
        "justificativa_3": response_json["justificativa_3"],
        "justificativa_4": response_json.get("justificativa_4", ""),
        "justificativa_5": response_json.get("justificativa_5", ""),

    }

    return response_obj

    

