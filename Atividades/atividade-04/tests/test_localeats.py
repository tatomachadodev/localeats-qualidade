# Responsável: Tácio Wurdig
from playwright.sync_api import Page, expect

LOGIN_URL = "https://local-eats-unisenac.vercel.app/static/login.html"
EMAIL = "wurdigtm@outlook.com"  # trocar pela conta de teste
SENHA = "1234"               # trocar pela senha da conta de teste

def test_selecionar_categoria_italiana_exibe_restaurantes_da_categoria(page: Page):
    # preparação: entrar no sistema
    page.goto(LOGIN_URL)
    page.get_by_role("textbox", name="teste@teste.com").fill(EMAIL)
    page.get_by_role("textbox", name="Sua senha secreta").fill(SENHA)
    page.locator("#loginForm").get_by_role("button", name="Entrar").click()

    # espera a lista de restaurantes carregar antes de interagir
    cards = page.get_by_role("link").filter(has_text="Restaurante Sabor")
    expect(cards.first).to_be_visible()

    # interação: clicar na categoria Italiana
    page.get_by_role("button", name="Italiana").click()

    # assertion 1: aparecem os 3 restaurantes italianos
    expect(page.get_by_role("link").filter(has_text="Italiana")).to_have_count(3)

    # assertion 2: restaurantes de outra categoria (Japonesa) saem da lista
    expect(page.get_by_role("link").filter(has_text="Japonesa")).to_have_count(0)