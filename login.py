from playwright.sync_api import sync_playwright
import time
from datetime import datetime


with  sync_playwright() as pw:
    navegador = pw.chromium.launch(headless=False)

    pagina = navegador.new_page()

    pagina.goto("https://hml-app.zafchat.com.br/onboarding")

    pagina.get_by_role("textbox", name="Nome do negócio").fill("Empresa teste")
    pagina.get_by_role("button", name="Continuar").click()

    pagina.get_by_role("textbox", name="Número do WhatsApp").fill("+01(0)123456789")
    pagina.get_by_role("button", name="Continuar").click()

    pagina.get_by_role("button", name="Outros").click()
    pagina.get_by_role("button", name="Continuar").click()

    pagina.wait_for_load_state("networkidle")
    pagina.get_by_role("button", name="Continuar").click()
    pagina.get_by_role("button", name="Ir para Pagamento").click()

    pagina.get_by_role("textbox", name="CPF/CNPJ do Titular").fill("123.456.789-01")
    pagina.get_by_role("textbox", name="Nome do Titular").fill("Nome teste")
    pagina.get_by_role("textbox", name="Email do Titular").fill("email_teste@email.com")
    pagina.get_by_role("textbox", name="CEP").fill("68628-320")
    pagina.get_by_role("textbox", name="Número", exact=True).fill("123")
    pagina.get_by_role("textbox", name="Nome no Cartão").fill("Nome teste")
    pagina.get_by_role("textbox", name="Número do Cartão").fill("0000 1111 2222 3333")
    pagina.get_by_role("textbox", name="Validade").fill("12/34")
    pagina.get_by_role("textbox", name="CVV").fill("123")
    pagina.get_by_role("button", name="Pagar com Cartão").click()

    #Criei essa função para ter um Email diferente a todo momento
    
    def data_hora_atual():
        agora = datetime.now()
        return agora.strftime("%d/%m/%Y_%H:%M:%S")
    

    pagina.get_by_role("textbox", name="Nome", exact=True).fill("Nome teste")
    pagina.get_by_role("textbox", name="Email").fill("teste_email@email.com.br")
    pagina.get_by_role("textbox", name="Senha", exact=True).fill("passwd")
    pagina.get_by_role("textbox", name="Confirme a Senha").fill("passwd")
    pagina.get_by_role("button", name="Continuar").click()

    pagina.get_by_role("button", name="Configurar depois", exact=True).click()

    pagina.get_by_role("button", name="Finalizar e Começar 🚀", exact=True).click()

    time.sleep(10)
    navegador.close()