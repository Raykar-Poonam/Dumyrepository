pytest -v -s -n=2 --html=HtmlReports/my_htmlreport.html --alluredir="AllureReports"

allure serve "AllureReports"