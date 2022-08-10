from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup 

with sync_playwright() as p:
        # browser = p.chromium.launch(headless=False, slow_mo=50)  # browser is zichtbaar
        browser = p.chromium.launch()                              # browser is onzichtbaar

        page = browser.new_page()
        page.goto('https://myedenred.be/', timeout = 100000)
        # timeout = 0 means that there is no timeout. Script will wait till page is loaded.

        # click on the first image "toegang gebruiker"
        page.locator('body > edn-root > edn-layout > main > ng-component > div > div.row.chooseYourProfil > div:nth-child(1) > div.profil-img.col-xs-6.col-xs-offset-3.col-sm-12.col-sm-offset-0 > img').click()

        wait('00:00:05')

        page.fill('input#Username', "bartland@gmail.com")
        page.fill('input#Password', "BVL18660md")

        wait('00:00:10')

        html = page.inner_html('##balanceBeneficiaryCarousel > div > div > edn-balance-details > div > owl-carousel-o > div > div.owl-stage-outer.ng-star-inserted > owl-stage > div > div > div:nth-child(1) > div > edn-product-balance > div > div.balanceAmount > span.amount')
        soup = BeautifulSoup(html, 'html.parser')
        soup = str(soup).strip()
        print(f'Saldo: {soup}')        