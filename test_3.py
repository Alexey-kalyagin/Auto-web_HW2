import yaml
from module import Site

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])

def test_step1(): 
    x_selector1 = """//*[@id="login"]/div[1]/label/input""" #  вставляем xpath элемента
    input1 = site.find_element("xpath", x_selector1) # ищем элемент по xpath
    input1.send_keys("Aliv358")                         # вводим в поле test
    
    x_selector2 = """//*[@id="login"]/div[2]/label/input""" #  вставляем xpath элемента
    input2 = site.find_element("xpath", x_selector2) # ищем элемент по xpath
    input2.send_keys("e42c86ecd3")
    
    btn_selector = "button"  # вставляем xpath элемента по selector
    btn = site.find_element("css",btn_selector) # ищем элемент "кнопку ввода" по css
    btn.click()   # кликаем на кнопку
        
    btn_create_post_selector = '//*[@id="create-btn"]'
    btn_create_post = site.find_element ("xpath",btn_create_post_selector)
    btn_create_post.click()
    
    x_selector3 = """//*[@id="create-item"]/div/div/div[1]/div/label/input"""
    input3 = site.find_element("xpath", x_selector3)
    input3.send_keys("Auto-test post")

    btn_save_post_selector = '//*[@id="create-item"]/div/div/div[7]/div/button/span'
    btn_save_post = site.find_element ("xpath",btn_save_post_selector)
    btn_save_post.click()

    x_selector4 = """//*[@id="app"]/main/div/div[1]/h1"""
    err_name_post = site.find_element("xpath", x_selector4)
    #print(err_name_post.text)
    
    assert err_name_post.text == "Create Post"
#test_step1()

