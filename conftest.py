import pytest
from selenium import webdriver

from calculated_variables import *


@pytest.fixture
def chrome_options(chrome_options):
    # chrome_options.binary_location = '/usr/bin/google-chrome-stable'
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--log-level=DEBUG')

    return chrome_options


@pytest.fixture(autouse=False, scope='class')
def open_test_page_login():
    pytest.driver = webdriver.Chrome(driver_path)
    pytest.driver.get(login_form_url)

    yield

    pytest.driver.quit()


@pytest.fixture(autouse=False, scope='class')
def open_test_page_otp():
    pytest.driver = webdriver.Chrome(driver_path)
    pytest.driver.get(otp_form_url)

    yield

    pytest.driver.quit()


@pytest.fixture(autouse=False, scope='class')
def open_test_page_reset():
    pytest.driver = webdriver.Chrome(driver_path)
    pytest.driver.get(reset_form_url)

    yield

    pytest.driver.quit()


@pytest.fixture(autouse=False, scope='class')
def open_test_page_register():
    pytest.driver = webdriver.Chrome(driver_path)
    pytest.driver.get(login_form_url)

    assert is_element_visible(register_link_locator) is True
    assert find_element_and_get_text(register_link_locator) == register_link_text

    find_element_and_click(register_link_locator)
    assert is_element_visible(register_form_locator)
    assert find_element_and_get_text(register_form_title_locator) == register_form_title

    yield

    pytest.driver.quit()


@pytest.fixture(autouse=True, scope='function')
def refresh_test_page():
    yield

    pytest.driver.refresh()


@pytest.fixture(autouse=False, scope='class')
def go_to_reset_choice_form():
    pytest.driver = webdriver.Chrome(driver_path)
    pytest.driver.get(reset_form_url)

    assert is_element_visible(reset_type_menu_tab_phone_locator) is True

    find_element_and_click(reset_type_menu_tab_phone_locator)
    assert find_element(reset_type_menu_tab_phone_locator) == find_element(reset_type_menu_tab_active_locator)
    assert is_element_visible(input_form_username_reset_locator) is True
    assert find_element_and_get_text(input_form_username_placeholder_locator) == \
           input_form_username_phone_placeholder
    assert is_element_visible(input_form_captcha_locator)
    assert is_element_visible(button_reset_locator)

    find_element_and_send_keys(input_form_username_reset_locator, valid_phone)
    find_element_and_click(input_form_captcha_locator)
    assert is_element_visible(input_form_error_text_locator, 1) is False
    assert find_element_and_get_attribute(input_form_username_value_locator, value_attribute) == \
           valid_phone or find_element_and_get_attribute(input_form_username_value_locator, value_attribute) == \
           valid_phone_form

    find_element_and_send_keys(input_form_captcha_locator, valid_captcha)
    find_element_and_click(input_form_username_reset_locator)
    assert find_element_and_get_attribute(input_form_captcha_locator, value_attribute) == valid_captcha

    find_element_and_click(button_reset_locator)
    assert is_element_visible(reset_choice_form_locator) is True  # Форма выбора восстановления пароля
    assert find_element_and_get_text(reset_choice_form_title_locator) == reset_choice_form_title
    assert is_element_visible(radio_input_by_phone_locator) is True  # Выбор "По SMS на номер телефона"
    assert is_element_visible(radio_label_by_phone_locator) is True
    assert find_element_and_get_text(radio_label_by_phone_locator) == radio_label_by_phone_text
    assert is_element_visible(radio_input_by_mail_locator) is True  # Выбор "По ссылке на почту"
    assert is_element_visible(radio_label_by_mail_locator) is True
    assert find_element_and_get_text(radio_label_by_mail_locator) == radio_label_by_mail_text
    assert is_element_visible(button_reset_choice_locator) is True  # Кнопка "Продолжить"
    assert find_element_and_get_text(button_reset_choice_locator) == button_reset_choice_text
    assert is_element_visible(button_reset_choice_back_locator) is True  # Кнопка "Вернуться назад"
    assert find_element_and_get_text(button_reset_choice_back_locator) == button_reset_choice_back_text

    yield

    pytest.driver.quit()


@pytest.fixture(autouse=False, scope='class')
def go_to_reset_confirm_form():
    pytest.driver = webdriver.Chrome(driver_path)
    pytest.driver.get(reset_form_url)

    assert is_element_visible(reset_type_menu_tab_phone_locator) is True

    find_element_and_click(reset_type_menu_tab_phone_locator)
    assert find_element(reset_type_menu_tab_phone_locator) == find_element(reset_type_menu_tab_active_locator)
    assert is_element_visible(input_form_username_reset_locator) is True
    assert find_element_and_get_text(input_form_username_placeholder_locator) == \
           input_form_username_phone_placeholder
    assert is_element_visible(input_form_captcha_locator)
    assert is_element_visible(button_reset_locator)

    find_element_and_send_keys(input_form_username_reset_locator, valid_phone)
    find_element_and_click(input_form_captcha_locator)
    assert is_element_visible(input_form_error_text_locator, 1) is False
    assert find_element_and_get_attribute(input_form_username_value_locator, value_attribute) == \
           valid_phone or find_element_and_get_attribute(input_form_username_value_locator, value_attribute) == \
           valid_phone_form

    find_element_and_send_keys(input_form_captcha_locator, valid_captcha)
    find_element_and_click(input_form_username_reset_locator)
    assert find_element_and_get_attribute(input_form_captcha_locator, value_attribute) == valid_captcha

    find_element_and_click(button_reset_locator)
    assert is_element_visible(reset_choice_form_locator) is True  # Форма выбора восстановления пароля
    assert find_element_and_get_text(reset_choice_form_title_locator) == reset_choice_form_title
    assert is_element_visible(radio_input_by_phone_locator) is True  # Выбор "По SMS на номер телефона"
    assert is_element_visible(radio_label_by_phone_locator) is True
    assert find_element_and_get_text(radio_label_by_phone_locator) == radio_label_by_phone_text
    assert is_element_visible(radio_input_by_mail_locator) is True  # Выбор "По ссылке на почту"
    assert is_element_visible(radio_label_by_mail_locator) is True
    assert find_element_and_get_text(radio_label_by_mail_locator) == radio_label_by_mail_text
    assert is_element_visible(button_reset_choice_locator) is True  # Кнопка "Продолжить"
    assert find_element_and_get_text(button_reset_choice_locator) == button_reset_choice_text
    assert is_element_visible(button_reset_choice_back_locator) is True  # Кнопка "Вернуться назад"
    assert find_element_and_get_text(button_reset_choice_back_locator) == button_reset_choice_back_text

    find_element_and_click(radio_input_by_phone_locator)  # Пользователь выбирает восстановить по номеру телефона
    assert find_element(radio_input_by_phone_locator) == find_element(radio_input_active_locator)

    find_element_and_click(button_reset_choice_locator)
    assert is_element_visible(reset_confirm_form_locator) is True  # Открывается форма с полем для ввода кода из СМС
    assert find_element_and_get_text(reset_confirm_form_title_locator) == reset_confirm_form_title
    assert valid_phone in find_element_and_get_text(reset_confirm_form_description_locator)\
           or valid_phone_form in find_element_and_get_text(reset_confirm_form_description_locator)
    assert is_all_elements_visible(input_reset_code_all_locator) is True  # Шесть отдельных полей для ввода кода
    # подтверждения
    assert len(find_elements(input_reset_code_all_locator)) == count_code_input
    assert is_element_visible(reset_resend_code_timeout_text_locator) is True  # Текст с обратным отсчётом времени
    # до повторной попытки отправки код
    assert resend_code_timeout_text in find_element_and_get_text(reset_resend_code_timeout_text_locator)

    assert is_element_visible(button_reset_resend_code_locator, sleep=resend_code_timeout) is True  # Кнопка
    # "Получить код повторно"
    assert is_element_visible(button_reset_confirm_back_locator) is True  # Кнопка "Вернуться назад"
    assert find_element_and_get_text(button_reset_confirm_back_locator) == button_reset_confirm_back_text

    yield

    pytest.driver.quit()


@pytest.fixture(autouse=False, scope='class')
def go_to_update_password_form():
    pytest.driver = webdriver.Chrome(driver_path)
    pytest.driver.get(reset_form_url)

    assert is_element_visible(reset_type_menu_tab_phone_locator) is True

    find_element_and_click(reset_type_menu_tab_phone_locator)
    assert find_element(reset_type_menu_tab_phone_locator) == find_element(reset_type_menu_tab_active_locator)
    assert is_element_visible(input_form_username_reset_locator) is True
    assert find_element_and_get_text(input_form_username_placeholder_locator) == \
           input_form_username_phone_placeholder
    assert is_element_visible(input_form_captcha_locator)
    assert is_element_visible(button_reset_locator)

    find_element_and_send_keys(input_form_username_reset_locator, valid_phone)
    find_element_and_click(input_form_captcha_locator)
    assert is_element_visible(input_form_error_text_locator, 1) is False
    assert find_element_and_get_attribute(input_form_username_value_locator, value_attribute) == \
           valid_phone or find_element_and_get_attribute(input_form_username_value_locator, value_attribute) == \
           valid_phone_form

    find_element_and_send_keys(input_form_captcha_locator, valid_captcha)
    find_element_and_click(input_form_username_reset_locator)
    assert find_element_and_get_attribute(input_form_captcha_locator, value_attribute) == valid_captcha

    find_element_and_click(button_reset_locator)
    assert is_element_visible(reset_choice_form_locator) is True  # Форма выбора восстановления пароля
    assert find_element_and_get_text(reset_choice_form_title_locator) == reset_choice_form_title
    assert is_element_visible(radio_input_by_phone_locator) is True  # Выбор "По SMS на номер телефона"
    assert is_element_visible(radio_label_by_phone_locator) is True
    assert find_element_and_get_text(radio_label_by_phone_locator) == radio_label_by_phone_text
    assert is_element_visible(radio_input_by_mail_locator) is True  # Выбор "По ссылке на почту"
    assert is_element_visible(radio_label_by_mail_locator) is True
    assert find_element_and_get_text(radio_label_by_mail_locator) == radio_label_by_mail_text
    assert is_element_visible(button_reset_choice_locator) is True  # Кнопка "Продолжить"
    assert find_element_and_get_text(button_reset_choice_locator) == button_reset_choice_text
    assert is_element_visible(button_reset_choice_back_locator) is True  # Кнопка "Вернуться назад"
    assert find_element_and_get_text(button_reset_choice_back_locator) == button_reset_choice_back_text

    find_element_and_click(radio_input_by_phone_locator)  # Пользователь выбирает восстановить по номеру телефона
    assert find_element(radio_input_by_phone_locator) == find_element(radio_input_active_locator)

    find_element_and_click(button_reset_choice_locator)
    assert is_element_visible(reset_confirm_form_locator) is True  # Открывается форма с полем для ввода кода из СМС
    assert find_element_and_get_text(reset_confirm_form_title_locator) == reset_confirm_form_title
    assert valid_phone in find_element_and_get_text(reset_confirm_form_description_locator)\
           or valid_phone_form in find_element_and_get_text(reset_confirm_form_description_locator)
    assert is_all_elements_visible(input_reset_code_all_locator) is True  # Шесть отдельных полей для ввода кода
    # подтверждения
    assert len(find_elements(input_reset_code_all_locator)) == count_code_input
    assert is_element_visible(reset_resend_code_timeout_text_locator) is True  # Текст с обратным отсчётом времени
    # до повторной попытки отправки код
    assert resend_code_timeout_text in find_element_and_get_text(reset_resend_code_timeout_text_locator)

    assert is_element_visible(button_reset_resend_code_locator, sleep=resend_code_timeout) is True  # Кнопка
    # "Получить код повторно"
    assert is_element_visible(button_reset_confirm_back_locator) is True  # Кнопка "Вернуться назад"
    assert find_element_and_get_text(button_reset_confirm_back_locator) == button_reset_confirm_back_text

    elements = find_elements(input_reset_code_all_locator)  # Клиент начинает вводить полученный код
    parent_elements = find_elements(input_code_parent_all_locator)

    i = 0
    while i < count_code_input:
        for element in elements:
            assert parent_elements[i] == find_element(input_code_parent_active_locator)
            element.send_keys(valid_otp[i])
            i += 1

    assert is_element_visible(update_password_form_locator) is True  # Форма для ввода нового пароля
    assert find_element_and_get_text(update_password_form_title_locator) == update_password_form_title
    assert is_element_visible(update_password_form_description_locator) is True  # Правила для создания пароля
    assert find_element_and_get_text(update_password_form_description_locator) == update_password_form_description
    assert is_element_visible(input_form_new_password_locator) is True  # Поле ввода нового пароля
    assert find_element_and_get_text(input_form_new_password_placeholder) == input_form_new_password_placeholder
    assert is_element_visible(input_form_password_confirm_locator) is True  # Поле ввода для подтверждения нового пароля
    assert find_element_and_get_text(input_form_password_confirm_placeholder) == input_form_password_confirm_placeholder
    assert is_element_visible(button_update_locator) is True  # Кнопка "Сохранить" для подтверждения нового пароля
    assert find_element_and_get_text(button_update_locator) == button_update_text
    assert is_element_clickable(button_update_locator) is False

    yield

    pytest.driver.quit()

# def find_element_and_clear(locator: tuple, timeout: int = 10):
#     locator_type = locator[0]
#     locator_value = locator[1]
#     WebDriverWait(pytest.driver, timeout).until(ec.element_to_be_clickable(locator))
#     return pytest.driver.find_element(locator_type, locator_value).clear()
#
#
# def is_element_selected(locator: tuple, timeout: int = 10):
#     locator_type = locator[0]
#     locator_value = locator[1]
#     WebDriverWait(pytest.driver, timeout).until(ec.element_to_be_clickable(locator))
#     return pytest.driver.find_element(locator_type, locator_value).is_selected()


# #!/usr/bin/python3
# # -*- encoding=utf8 -*-
#
# # This is example shows how we can manage failed tests
# # and make screenshots after any failed test case.
#
# import pytest
# import uuid
#
#
#
# @pytest.fixture
# def chrome_options(chrome_options):
#     # chrome_options.binary_location = '/usr/bin/google-chrome-stable'
#     # chrome_options.add_argument('--headless')
#     chrome_options.add_argument('--no-sandbox')
#     chrome_options.add_argument('--log-level=DEBUG')
#
#     return chrome_options
#
#
# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     # This function helps to detect that some test failed
#     # and pass this information to teardown:
#
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item, "rep_" + rep.when, rep)
#     return rep
#
#
# @pytest.fixture
# def web_browser(request, selenium):
#
#     browser = selenium
#     browser.set_window_size(1400, 1000)
#
#     # Return browser instance to test case:
#     yield browser
#
#     # Do teardown (this code will be executed after each test):
#
#     if request.node.rep_call.failed:
#         # Make the screen-shot if test failed:
#         try:
#             browser.execute_script("document.body.bgColor = 'white';")
#
#             # Make screen-shot for local debug:
#             browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')
#
#             # Attach screenshot to Allure report:
#             allure.attach(browser.get_screenshot_as_png(),
#                           name=request.function.__name__,
#                           attachment_type=allure.attachment_type.PNG)
#
#             # For happy debugging:
#             print('URL: ', browser.current_url)
#             print('Browser logs:')
#             for log in browser.get_log('browser'):
#                 print(log)
#
#         except:
#             pass # just ignore any errors here
#
#
# def get_test_case_docstring(item):
#     """ This function gets doc string from test case and format it
#         to show this docstring instead of the test case name in reports.
#     """
#
#     full_name = ''
#
#     if item._obj.__doc__:
#         # Remove extra whitespaces from the doc string:
#         name = str(item._obj.__doc__.split('.')[0]).strip()
#         full_name = ' '.join(name.split())
#
#         # Generate the list of parameters for parametrized test cases:
#         if hasattr(item, 'callspec'):
#             params = item.callspec.params
#
#             res_keys = sorted([k for k in params])
#             # Create List based on Dict:
#             res = ['{0}_"{1}"'.format(k, params[k]) for k in res_keys]
#             # Add dict with all parameters to the name of test case:
#             full_name += ' Parameters ' + str(', '.join(res))
#             full_name = full_name.replace(':', '')
#
#     return full_name
#
#
# def pytest_itemcollected(item):
#     """ This function modifies names of test cases "on the fly"
#         during the execution of test cases.
#     """
#
#     if item._obj.__doc__:
#         item._nodeid = get_test_case_docstring(item)
#
#
# def pytest_collection_finish(session):
#     """ This function modified names of test cases "on the fly"
#         when we are using --collect-only parameter for pytest
#         (to get the full list of all existing test cases).
#     """
#
#     if session.config.option.collectonly is True:
#         for item in session.items:
#             # If test case has a doc string we need to modify it's name to
#             # it's doc string to show human-readable reports and to
#             # automatically import test cases to test management system.
#             if item._obj.__doc__:
#                 full_name = get_test_case_docstring(item)
#                 print(full_name)
#
#         pytest.exit('Done!')
