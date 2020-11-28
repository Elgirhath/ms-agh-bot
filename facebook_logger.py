from time import sleep
import msvcrt
import logging

def flush_input_buffer():
    while msvcrt.kbhit():
        msvcrt.getch()


def remove_element(driver, element):
    driver.execute_script("""
    var element = arguments[0];
    element.parentNode.removeChild(element);
    """, element)

def remove_language_popup(driver):
    try:
        lang_popup = driver.find_element_by_id("u_0_d")
        remove_element(driver, lang_popup)
    except Exception:
        pass

def log_in(driver, email, password):
    logging.info("Logging into Facebook")

    flush_input_buffer()

    driver.get("https://www.facebook.com")

    remove_language_popup(driver)

    driver.find_element_by_id("u_0_h").click()

    sleep(0.1)

    driver.find_element_by_id("email").send_keys(email)

    driver.find_element_by_id("pass").send_keys(password)
    
    sleep(0.1)

    driver.find_element_by_id("u_0_b").click()

    sleep(0.5)