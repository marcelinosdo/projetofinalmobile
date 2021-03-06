import pytest
from selenium import webdriver

@pytest.fixture(scope='class')
def test_setup():

    desired_cap = {
        'platformName': 'Android',
        'deviceName': 'emulator-5554',
        "app": "C:/Users/Marce/OneDrive/DOCUMENTOS/ETA/ETA025-TÓPICOS ESPECIAIS I/projetofinalmobile/resources/apk/br.jus.tse.resultados_5000105_apps.evozi.com.apk",
        'autoGrantPermissions': True
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
    yield driver
    driver.quit()