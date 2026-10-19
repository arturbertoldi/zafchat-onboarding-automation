# Automação de Onboarding – ZafChat (Homologação)

Script em Python que usa o [Playwright](https://playwright.dev/python/) para percorrer o fluxo completo de onboarding do ZafChat no ambiente de **homologação** (`hml-app.zafchat.com.br`): cadastro do negócio, pagamento com cartão, criação de conta e finalização.

> ⚠️ Use apenas em homologação, com dados e cartões de teste.

## O que o script faz

1. Abre o Chromium (com interface visível) em `/onboarding`.
2. **Negócio**: preenche o nome do negócio e avança.
3. **WhatsApp**: informa o número e avança.
4. **Segmento**: seleciona "Outros" e avança.
5. **Plano**: aguarda a rede ficar ociosa, avança e clica em "Ir para Pagamento".
6. **Pagamento**: preenche titular (CPF/CNPJ, nome, e-mail), endereço (CEP, número) e cartão (nome, número, validade, CVV) e clica em "Pagar com Cartão".
7. **Conta**: preenche nome, e-mail, senha e confirmação de senha e avança.
8. Clica em "Configurar depois" e em "Finalizar e Começar 🚀".
9. Aguarda 10 segundos e fecha o navegador.

## Requisitos

- Python 3.9+
- Playwright

## Instalação

```bash
pip install playwright
playwright install chromium
```

## Execução

```bash
python onboarding.py
```

## Dados utilizados

Todos os dados do script são fictícios e servem apenas para o ambiente de homologação.

| Etapa | Campo | Observação |
|---|---|---|
| Negócio | Nome do negócio | `Empresa teste` |
| WhatsApp | Número | Número fictício |
| Pagamento | CPF/CNPJ, nome, e-mail, CEP, número | Dados fictícios |
| Pagamento | Cartão, validade, CVV | Cartão fictício; se o gateway validar, use um cartão de teste dele |
| Conta | Nome, e-mail, senha | Senha de teste |

## Pontos de atenção

- **E-mail da conta é fixo** (`teste_email@email.com.br`). Se o sistema bloquear e-mails já cadastrados, a segunda execução falha. A função `data_hora_atual()` foi criada para resolver isso, mas ainda não é usada. Exemplo de uso:

  ```python
  def data_hora_atual():
      return datetime.now().strftime("%Y%m%d_%H%M%S")

  email = f"teste_{data_hora_atual()}@email.com.br"
  pagina.get_by_role("textbox", name="Email").fill(email)
  ```

  Use `%Y%m%d_%H%M%S`: o formato com `/` e `:` gera e-mails inválidos.

- **Espera final**: o script termina com `time.sleep(10)` para dar tempo de ver o resultado. Se alguma etapa falhar (elemento não encontrado, timeout), o Playwright interrompe a execução e mostra o erro. A espera em si não confirma que o onboarding foi concluído com sucesso.

- **Seletores** usam `get_by_role` com o texto visível dos campos e botões. Se os rótulos da tela mudarem, o script quebra.

## Estrutura

```
.
├── onboarding.py
└── README.md
```
