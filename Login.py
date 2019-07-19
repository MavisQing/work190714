from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re,os,sys

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)
class LoginDemo(unittest.TestCase):
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    base_url = "http://www.doclever.cn"
    verificationErrors = []
    accept_next_alert = True

    def test_1_login(self):
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url + "/controller/index/index.html")
        driver.find_element_by_link_text("登录").click()
        driver.find_element_by_css_selector("input.el-input__inner").clear()
        driver.find_element_by_css_selector("input.el-input__inner").send_keys("Mavis")
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys("SKN961006")
        driver.find_element_by_id("login").click()
        time.sleep(5)
        self.assertTrue(self.is_element_present(By.ID,"tab-interface"))

    def test_2_create_group(self):
        driver = self.driver
        driver.find_element_by_xpath("//*[contains(text(),'PyautoDemo')]").click()
        time.sleep(5)
        # driver.find_element_by_xpath(".//*[contains(text(),'HomeWork')]").perform()
        ActionChains(driver).move_to_element(
            driver.find_element_by_xpath(
                ".//div[contains(text(),'HomeWork')]")).perform()


    def test_3_create_interface (self):
        driver = self.driver
        driver.find_element_by_xpath("//*[@title='新建接口']").click()
        driver.find_element_by_css_selector(
            "div.el-form-item__content > div.el-input.el-input--small > input.el-input__inner").send_keys("Login")
        time.sleep(1)

        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='路径'])[2]/following::input[1]").click()
        time.sleep(1)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='GET'])[1]/following::li[1]").click()
        time.sleep(1)
        driver.find_element_by_css_selector(
            "div.row.el-row > div.el-form-item > div.el-form-item__content > div.el-input.el-input--small > input.el-input__inner").send_keys(
            "/user/login")

        time.sleep(1)

        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Raw'])[1]/following::input[1]").send_keys("name")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='必选'])[2]/following::span[2]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='状态码映射'])[1]/following::input[1]").send_keys("Mavis")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='新增'])[2]/following::span[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='已填值'])[1]/following::input[1]").send_keys("password")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='必选'])[3]/following::span[2]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='状态码映射'])[1]/following::input[1]").send_keys(
            "SKN961006")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='新增'])[2]/following::span[1]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='btnSave']/div/button/span/span[contains(text(), '保存')]").click()
        time.sleep(2)
        # 运行接口
        driver.find_element_by_xpath(
            ".//*[@id='interfaceContent']/div/div/div/button/span[contains(text(), '运行')]").click()
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[5]").send_keys('http://www.doclever.cn:8090')
        time.sleep(1)
        driver.find_element_by_xpath(
            ".//*[@id='interfaceContent']/div/div/div/button/span[contains(text(), '运行')]").click()
        time.sleep(5)
        self.assertTrue(self.is_element_present(By.XPATH, './/*[contains(text(),\'"code":200\')]'))

    def test_4_logout(self):
        driver = self.driver
        ActionChains(driver).move_to_element(
            driver.find_element_by_css_selector('i.el-icon-caret-bottom.el-icon--right')).perform()  # 把鼠标放到元素上，其他的什么都不动
        time.sleep(1)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='帮助中心'])[1]/following::li[1]").click()
        time.sleep(5)
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "登录"))
        driver.quit()


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True


if __name__ == "__main__":

    suite = unittest.TestSuite()
    tests = [LoginDemo("test_1_login"), LoginDemo("test_2_create_group"), LoginDemo("test_3_create_interface"), LoginDemo("test_4_logout")]
    suite.addTests(tests)
    runner = unittest.TextTestRunner()
    runner.run(suite)