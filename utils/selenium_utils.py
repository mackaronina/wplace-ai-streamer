def hide_element(driver, element):
    driver.execute_script('arguments[0].style.visibility="hidden";', element)


def show_element(driver, element):
    driver.execute_script('arguments[0].style.visibility="visible";', element)
