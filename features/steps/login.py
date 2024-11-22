from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# نصب خودکار chromedriver
chromedriver_autoinstaller.install()

@given(u'کاربر وارد پلتفرم ثبتنام یا ورود کوروک به آدرس "{url}"')
def step_impl(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)
    time.sleep(2)

@when(u'کاربر در فیلد مربوط به شماره تلفن عبارت "{phone}" را وارد می کند')
def step_impl(context,phone):
        phone_field = context.driver.find_element("name", "phone") 
        phone_field.send_keys(phone)


@when(u'کاربر روی کلید "ادامه" کلیک می کند')
def step_impl(context):
        login_button = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "fxt-btn-fill"))
        )
        login_button.click()
        time.sleep(6)

@when(u'کاربر وارد صفحه کد تایید پیامکی شده و روی کلید "ورود به وسیله رمز عبور" کلیک می کند')
def step_impl(context):
        password_link = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.fxt-btn-fill")) #<a href="https://kowork.work/login/pass" class="fxt-btn-fill mt-2 btn-home">ورود به وسیله کلمه عبور</a>
        )
        password_link.click()
        time.sleep(10)
@when('کاربر در فیلد مربوط به رمز عبور عبارت "{password}" را وارد می کند')
def step_impl(context, password):
    password_field = context.driver.find_element("name", "password") 
    password_field.send_keys(password)
    time.sleep(10)

@when('کاربر روی کلید "ورود به حساب کاربری" کلیک می کند')
def step_impl(context):
    login_button = context.driver.find_element(By.CSS_SELECTOR, "button.fxt-btn-fill")
    login_button.click()
    time.sleep(10)

