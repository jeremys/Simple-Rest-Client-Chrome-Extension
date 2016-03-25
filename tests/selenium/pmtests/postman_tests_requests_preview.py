from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.chrome.service as service
import traceback     
import inspect
import time
from postman_tests import PostmanTests

class PostmanTestsRequestsPreview(PostmanTests):
    def click_preview_button(self):
        preview_button = self.browser.find_element_by_id("preview-request")
        preview_button.click()

    def preview_has_text(self, text):
        preview_content_div = self.browser.find_element_by_id("request-preview-content")
        preview_content = self.browser.execute_script("return arguments[0].innerHTML", preview_content_div)

        if preview_content.find(text) >= 0:
            return True
        else:
            return False

    def test_1_get_basic(self):
        self.reset_request()
        self.set_url_field(self.browser, "http://localhost:5000/get")
        self.click_preview_button()
        r = self.preview_has_text("get")
        return r

    def test_2_get_only_key(self):
        self.reset_request()
        self.set_url_field(self.browser, "http://localhost:5000/get?start")

        self.click_preview_button()
        r = self.preview_has_text("get?start")
        return r

    def test_3_delete_basic(self):
        self.reset_request()

        self.set_url_field(self.browser, "http://localhost:5000/delete")

        method_select = self.browser.find_element_by_id("request-method-selector")    
        Select(method_select).select_by_value("DELETE")

        self.click_preview_button()
        r = self.preview_has_text("DELETE")
        return r


    def test_4_head_basic(self):
        self.reset_request()

        self.set_url_field(self.browser, "http://localhost:5000/html")
        method_select = self.browser.find_element_by_id("request-method-selector")    
        Select(method_select).select_by_value("HEAD")
        self.click_preview_button()
        r = self.preview_has_text("HEAD")
        return r

    def test_5_options_basic(self):
        self.reset_request()

        self.set_url_field(self.browser, "http://localhost:5000/html")
        method_select = self.browser.find_element_by_id("request-method-selector")    
        Select(method_select).select_by_value("OPTIONS")
        self.click_preview_button()
        r = self.preview_has_text("OPTIONS")
        return r

    def test_6_post_basic(self):
        self.reset_request()

        self.set_url_field(self.browser, "http://localhost:5000/post")
        method_select = self.browser.find_element_by_id("request-method-selector")    
        Select(method_select).select_by_value("POST")
        self.click_preview_button()
        r = self.preview_has_text("POST")
        return r

    def test_7_put_basic(self):
        self.reset_request()

        self.set_url_field(self.browser, "http://localhost:5000/put")
        method_select = self.browser.find_element_by_id("request-method-selector")    
        Select(method_select).select_by_value("PUT")
        self.click_preview_button()
        r = self.preview_has_text("PUT")
        return r

    def test_8_init_environment(self):
        self.reset_request()

        environment_selector = self.browser.find_element_by_id("environment-selector")
        environment_selector.click()

        time.sleep(0.1)

        manage_env_link = self.browser.find_element_by_css_selector("#environment-selector .dropdown-menu li:last-child a")
        manage_env_link.click()

        time.sleep(1)

        add_env_button = self.browser.find_element_by_css_selector("#environments-list-wrapper .toolbar .environments-actions-add")
        add_env_button.click()
        time.sleep(0.3)

        environment_name = self.browser.find_element_by_id("environment-editor-name")
        environment_name.clear()
        environment_name.send_keys("Requests environment")

        first_key = self.browser.find_element_by_css_selector("#environment-keyvaleditor .keyvalueeditor-row:first-child .keyvalueeditor-key")
        first_key.clear()
        first_key.send_keys("path_get")

        first_val = self.browser.find_element_by_css_selector("#environment-keyvaleditor .keyvalueeditor-row:first-child .keyvalueeditor-value")
        first_val.clear()
        first_val.send_keys("get?start=something")

        second_key = self.browser.find_element_by_css_selector("#environment-keyvaleditor .keyvalueeditor-row:nth-of-type(2) .keyvalueeditor-key")
        second_key.clear()
        second_key.send_keys("path_post")

        second_val = self.browser.find_element_by_css_selector("#environment-keyvaleditor .keyvalueeditor-row:nth-of-type(2) .keyvalueeditor-value")
        second_val.clear()
        second_val.send_keys("post")

        third_key = self.browser.find_element_by_css_selector("#environment-keyvaleditor .keyvalueeditor-row:nth-of-type(3) .keyvalueeditor-key")
        third_key.clear()
        third_key.send_keys("Foo")

        third_val = self.browser.find_element_by_css_selector("#environment-keyvaleditor .keyvalueeditor-row:nth-of-type(3) .keyvalueeditor-value")
        third_val.clear()
        third_val.send_keys("Bar")

        fourth_key = self.browser.find_element_by_css_selector("#environment-keyvaleditor .keyvalueeditor-row:nth-of-type(4) .keyvalueeditor-key")
        fourth_key.clear()
        fourth_key.send_keys("Name")

        fourth_val = self.browser.find_element_by_css_selector("#environment-keyvaleditor .keyvalueeditor-row:nth-of-type(4) .keyvalueeditor-value")
        fourth_val.clear()
        fourth_val.send_keys("John Appleseed")

        fifth_key = self.browser.find_element_by_css_selector("#environment-keyvaleditor .keyvalueeditor-row:nth-of-type(5) .keyvalueeditor-key")
        fifth_key.clear()
        fifth_key.send_keys("nonce")

        fifth_val = self.browser.find_element_by_css_selector("#environment-keyvaleditor .keyvalueeditor-row:nth-of-type(5) .keyvalueeditor-value")
        fifth_val.clear()
        fifth_val.send_keys("kllo9940pd9333jh")

        sixth_key = self.browser.find_element_by_css_selector("#environment-keyvaleditor .keyvalueeditor-row:nth-of-type(6) .keyvalueeditor-key")
        sixth_key.clear()
        sixth_key.send_keys("timestamp")

        sixth_val = self.browser.find_element_by_css_selector("#environment-keyvaleditor .keyvalueeditor-row:nth-of-type(6) .keyvalueeditor-value")
        sixth_val.clear()
        sixth_val.send_keys("1191242096")

        seventh_key = self.browser.find_element_by_css_selector("#environment-keyvaleditor .keyvalueeditor-row:nth-of-type(7) .keyvalueeditor-key")
        seventh_key.clear()
        seventh_key.send_keys("url")

        seventh_val = self.browser.find_element_by_css_selector("#environment-keyvaleditor .keyvalueeditor-row:nth-of-type(7) .keyvalueeditor-value")
        seventh_val.clear()
        seventh_val.send_keys("http://photos.example.net/photos")

        eigth_key = self.browser.find_element_by_css_selector("#environment-keyvaleditor .keyvalueeditor-row:nth-of-type(8) .keyvalueeditor-key")
        eigth_key.clear()
        eigth_key.send_keys("file")

        eigth_val = self.browser.find_element_by_css_selector("#environment-keyvaleditor .keyvalueeditor-row:nth-of-type(8) .keyvalueeditor-value")
        eigth_val.clear()
        eigth_val.send_keys("vacation.jpg")

        ninth_key = self.browser.find_element_by_css_selector("#environment-keyvaleditor .keyvalueeditor-row:nth-of-type(9) .keyvalueeditor-key")
        ninth_key.clear()
        ninth_key.send_keys("size")

        ninth_val = self.browser.find_element_by_css_selector("#environment-keyvaleditor .keyvalueeditor-row:nth-of-type(9) .keyvalueeditor-value")
        ninth_val.clear()
        ninth_val.send_keys("original")

        submit_button = self.browser.find_element_by_css_selector("#modal-environments .environments-actions-add-submit")
        submit_button.click()
        time.sleep(0.3)

        close_button = self.browser.find_element_by_css_selector("#modal-environments .modal-header .close")
        close_button.click()

        time.sleep(1)

        environment_selector = self.browser.find_element_by_id("environment-selector")
        environment_selector.click()

        # Select the environment
        manage_env_link = self.browser.find_element_by_css_selector("#environment-selector .dropdown-menu li:nth-of-type(1) a")
        manage_env_link.click()

        return True

    def test_9_get_environment(self):
        self.reset_request()

        self.set_url_field(self.browser, "http://localhost:5000/{{path_get}}")

        self.click_preview_button()
        r = self.preview_has_text("get?start=something")
        return r

    def test_10_post_formdata_environment(self):
        self.reset_request()

        self.set_url_field(self.browser, "http://localhost:5000/{{path_post}}")

        method_select = self.browser.find_element_by_id("request-method-selector")    
        Select(method_select).select_by_value("POST")

        first_formdata_key = self.browser.find_element_by_css_selector("#formdata-keyvaleditor .keyvalueeditor-row:nth-of-type(1) .keyvalueeditor-key")
        first_formdata_key.clear()
        first_formdata_key.send_keys("size")

        first_formdata_value = self.browser.find_element_by_css_selector("#formdata-keyvaleditor .keyvalueeditor-row:nth-of-type(1) .keyvalueeditor-value")
        first_formdata_value.clear()
        first_formdata_value.send_keys("{{size}}")

        second_formdata_key = self.browser.find_element_by_css_selector("#formdata-keyvaleditor .keyvalueeditor-row:nth-of-type(2) .keyvalueeditor-key")
        second_formdata_key.clear()
        second_formdata_key.send_keys("file")

        second_formdata_value = self.browser.find_element_by_css_selector("#formdata-keyvaleditor .keyvalueeditor-row:nth-of-type(2) .keyvalueeditor-value")
        second_formdata_value.clear()
        second_formdata_value.send_keys("{{file}}")

        self.click_preview_button()
        r = self.preview_has_text("original")
        return r

    def test_11_post_urlencoded_environment(self):
        self.reset_request()

        self.set_url_field(self.browser, "http://localhost:5000/{{path_post}}")

        method_select = self.browser.find_element_by_id("request-method-selector")    
        Select(method_select).select_by_value("POST")

        # Select urlencoded
        self.browser.find_element_by_css_selector("#data-mode-selector a:nth-of-type(2)").click()

        first_formdata_key = self.browser.find_element_by_css_selector("#urlencoded-keyvaleditor .keyvalueeditor-row:nth-of-type(1) .keyvalueeditor-key")
        first_formdata_key.clear()
        first_formdata_key.send_keys("size")

        first_formdata_value = self.browser.find_element_by_css_selector("#urlencoded-keyvaleditor .keyvalueeditor-row:nth-of-type(1) .keyvalueeditor-value")
        first_formdata_value.clear()
        first_formdata_value.send_keys("{{size}}")

        second_formdata_key = self.browser.find_element_by_css_selector("#urlencoded-keyvaleditor .keyvalueeditor-row:nth-of-type(2) .keyvalueeditor-key")
        second_formdata_key.clear()
        second_formdata_key.send_keys("file")

        second_formdata_value = self.browser.find_element_by_css_selector("#urlencoded-keyvaleditor .keyvalueeditor-row:nth-of-type(2) .keyvalueeditor-value")
        second_formdata_value.clear()
        second_formdata_value.send_keys("{{file}}")

        self.click_preview_button()
        r = self.preview_has_text("original")
        return r


    def test_12_post_raw_environment(self):
        self.reset_request()

        self.set_url_field(self.browser, "http://localhost:5000/{{path_post}}")

        method_select = self.browser.find_element_by_id("request-method-selector")    
        Select(method_select).select_by_value("POST")

        # Select urlencoded
        self.browser.find_element_by_css_selector("#data-mode-selector a:nth-of-type(3)").click()

        self.set_code_mirror_raw_value("{{Foo}}={{Name}}")

        self.click_preview_button()
        r = self.preview_has_text("John Appleseed")
        return r

    def test_13_post_raw_json_environment(self):
        self.reset_request()

        self.set_url_field(self.browser, "http://localhost:5000/{{path_post}}")

        method_select = self.browser.find_element_by_id("request-method-selector")    
        Select(method_select).select_by_value("POST")

        self.browser.find_element_by_css_selector("#data-mode-selector a:nth-of-type(3)").click()

        self.set_code_mirror_raw_value("{\"{{Foo}}\":\"{{Name}}\"")

        self.click_preview_button()
        r = self.preview_has_text("John Appleseed")
        return r

    # https://github.com/a85/POSTMan-Chrome-Extension/issues/174
    def test_14_url_with_semicolon(self):
        self.reset_request()

        self.set_url_field(self.browser, "http://localhost:5000/get?some=start;val")

        send_button = self.browser.find_element_by_id("submit-request")

        self.click_preview_button()
        r = self.preview_has_text("/get?some=start;val")
        return r

    def test_16_with_no_cache(self):
        self.reset_request()
        self.set_url_field(self.browser, "http://localhost:5000/get")
        
        settings_button = self.browser.find_element_by_css_selector(".preferences a:nth-of-type(2)")
        settings_button.click()

        time.sleep(1)

        no_cache_select = self.browser.find_element_by_id("send-no-cache-header")    
        Select(no_cache_select).select_by_value("true")
        
        close_button = self.browser.find_element_by_css_selector("#modal-settings .modal-header .close")
        close_button.click()

        time.sleep(1)

        self.set_url_field(self.browser, "http://localhost:5000/get")
        self.click_preview_button()
        r = self.preview_has_text("no-cache")
        return r

    def test_17_without_no_cache(self):
        self.reset_request()
        self.set_url_field(self.browser, "http://localhost:5000/get")
        
        settings_button = self.browser.find_element_by_css_selector(".preferences a:nth-of-type(2)")
        settings_button.click()

        time.sleep(1)

        no_cache_select = self.browser.find_element_by_id("send-no-cache-header")    
        Select(no_cache_select).select_by_value("false")
        
        close_button = self.browser.find_element_by_css_selector("#modal-settings .modal-header .close")
        close_button.click()

        time.sleep(1)

        self.set_url_field(self.browser, "http://localhost:5000/get")

        self.set_url_field(self.browser, "http://localhost:5000/get")
        self.click_preview_button()
        r = self.preview_has_text("no-cache")
        return not r

PostmanTestsRequestsPreview().run()
