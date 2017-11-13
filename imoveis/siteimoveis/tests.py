from django.test import TestCase

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver


class SeleniumTestCase(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.PhantomJS()
        self.browser.set_window_size(1024, 768)
        self.browser.get(self.live_server_url)
        print(self.live_server_url)

    def test_user_registration(self):
        self.browser.find_element_by_link_text("Cadastrar Vendedor").click()
        self.browser.find_element_by_id("id_nome").clear()
        self.browser.find_element_by_id("id_nome").send_keys("jamesteste")
        self.browser.find_element_by_id("id_sobrenome").clear()
        self.browser.find_element_by_id("id_sobrenome").send_keys("peresteste")
        self.browser.find_element_by_id("id_telefone").clear()
        self.browser.find_element_by_id("id_telefone").send_keys("123123123")
        self.browser.save_screenshot("teste001.png")
        self.browser.find_element_by_xpath("(//button[@type='submit'])[2]").click()
        self.browser.save_screenshot("teste002.png")

    def test_cadastrar_imovel(self):
        self.browser.find_element_by_link_text("Cadastrar Imovel").click()
        self.browser.find_element_by_id("id_endereco").clear()
        self.browser.find_element_by_id("id_endereco").send_keys("teste123")
        self.browser.find_element_by_id("id_valor").clear()
        self.browser.find_element_by_id("id_valor").send_keys("12")
        self.browser.find_element_by_id("id_bairro").clear()
        self.browser.find_element_by_id("id_bairro").send_keys("teste")
        self.browser.find_element_by_id("id_cidade").clear()
        self.browser.find_element_by_id("id_cidade").send_keys("teste")
        self.browser.find_element_by_id("id_anuncio").clear()
        self.browser.find_element_by_id("id_anuncio").send_keys("123testea")
        self.browser.save_screenshot("teste003.png")
