import pytest

from calculated_variables import *
from locators import *


class TestRegisterForm:
    def test_pass(self):
        pass

    @pytest.mark.usefixtures('open_test_page_register')
    class TestRegisterFormElements:
        def test_input_form_first_name_success(self):
            assert is_element_visible(input_form_first_name_locator) is True

            for name in valid_name_list:
                find_element_and_send_keys(input_form_first_name_locator, name)
                find_element_and_click(input_form_last_name_locator)
                name_value = find_element_and_get_attribute(input_form_first_name_locator, value_attribute)
                print(name, name_value)
                assert name_value.lower() == name.lower()

                for i in range(len(name)):
                    if i == 0:
                        assert name_value[i].isupper()
                    elif name_value[i] in special_chars_name:
                        assert name_value[i + 1].isupper()
                    elif name_value[i].isupper():
                        assert name_value[i - 1] in special_chars_name
                    else:
                        assert name_value[i].islower()

                assert is_element_visible(input_form_first_name_error_text_locator, 1) is False

                refresh_page()

        def test_input_form_last_name_success(self):
            assert is_element_visible(input_form_last_name_locator) is True

            for name in valid_name_list:
                find_element_and_send_keys(input_form_last_name_locator, name)
                find_element_and_click(input_form_first_name_locator)
                name_value = find_element_and_get_attribute(input_form_last_name_locator, value_attribute)
                print(name, name_value)
                assert name_value.lower() == name.lower()

                for i in range(len(name)):
                    if i == 0:
                        assert name_value[i].isupper()
                    elif name_value[i] in special_chars_name:
                        assert name_value[i + 1].isupper()
                    elif name_value[i].isupper():
                        assert name_value[i - 1] in special_chars_name
                    else:
                        assert name_value[i].islower()

                assert is_element_visible(input_form_last_name_error_text_locator, 1) is False

                refresh_page()

        class TestInputFormFirstNameFailure:
            def test_input_form_first_name_failure_valid_chars_invalid_len(self):
                for name in valid_chars_invalid_len_name_list:
                    find_element_and_send_keys(input_form_first_name_locator, name)
                    find_element_and_click(input_form_last_name_locator)
                    name_value = find_element_and_get_attribute(input_form_first_name_locator, value_attribute)
                    print(name, name_value)
                    assert name_value.lower() == name.lower()

                    if 0 < len(name) < password_valid_len_interval_list[0]:
                        assert is_element_visible(input_form_first_name_error_text_locator, 1) is True
                        assert find_element_and_get_text(input_form_first_name_error_text_locator) == \
                               input_form_name_error_text
                    elif len(name) > password_valid_len_interval_list[1]:
                        assert is_element_visible(input_form_first_name_error_text_locator, 1) is True
                        assert find_element_and_get_text(input_form_first_name_error_text_locator) == \
                               input_form_name_error_text
                    elif len(name) == 0:
                        assert is_element_visible(input_form_first_name_error_text_locator, 1) is False

                    refresh_page()

            def test_input_form_first_name_failure_not_only_cyrillic_letters(self):
                for name in not_only_cyrillic_letters_name_list:
                    find_element_and_send_keys(input_form_first_name_locator, name)
                    find_element_and_click(input_form_last_name_locator)
                    name_value = find_element_and_get_attribute(input_form_first_name_locator, value_attribute)
                    print(name, name_value)
                    assert name_value.lower() == name.lower()
                    assert is_element_visible(input_form_first_name_error_text_locator, 1) is True
                    assert find_element_and_get_text(input_form_first_name_error_text_locator) == \
                           input_form_name_error_text

                    refresh_page()

            def test_input_form_first_name_failure_with_digits(self):
                for name in with_digits_name_list:
                    find_element_and_send_keys(input_form_first_name_locator, name)
                    find_element_and_click(input_form_last_name_locator)
                    name_value = find_element_and_get_attribute(input_form_first_name_locator, value_attribute)
                    print(name, name_value)
                    assert name_value.lower() == name.lower()
                    assert is_element_visible(input_form_first_name_error_text_locator, 1) is True
                    assert find_element_and_get_text(input_form_first_name_error_text_locator) == \
                           input_form_name_error_text

                    refresh_page()

            def test_input_form_first_name_failure_with_other_special_chars(self):
                for name in with_other_special_chars_name_list:
                    find_element_and_send_keys(input_form_first_name_locator, name)
                    find_element_and_click(input_form_last_name_locator)
                    name_value = find_element_and_get_attribute(input_form_first_name_locator, value_attribute)
                    print(name, name_value)
                    assert name_value.lower() == name.lower()
                    assert is_element_visible(input_form_first_name_error_text_locator, 1) is True
                    assert find_element_and_get_text(input_form_first_name_error_text_locator) == \
                           input_form_name_error_text

                    refresh_page()

        class TestInputFormLastNameFailure:
            def test_input_form_last_name_failure_valid_chars_invalid_len(self):
                for name in valid_chars_invalid_len_name_list:
                    find_element_and_send_keys(input_form_last_name_locator, name)
                    find_element_and_click(input_form_first_name_locator)
                    name_value = find_element_and_get_attribute(input_form_last_name_locator, value_attribute)
                    print(name, name_value)
                    assert name_value.lower() == name.lower()

                    if 0 < len(name) < password_valid_len_interval_list[0]:
                        assert is_element_visible(input_form_last_name_error_text_locator, 1) is True
                        assert find_element_and_get_text(input_form_last_name_error_text_locator) == \
                               input_form_name_error_text
                    elif len(name) > password_valid_len_interval_list[1]:
                        assert is_element_visible(input_form_last_name_error_text_locator, 1) is True
                        assert find_element_and_get_text(input_form_last_name_error_text_locator) == \
                               input_form_name_error_text
                    elif len(name) == 0:
                        assert is_element_visible(input_form_last_name_error_text_locator, 1) is False

                    refresh_page()

            def test_input_form_last_name_failure_not_only_cyrillic_letters(self):
                for name in not_only_cyrillic_letters_name_list:
                    find_element_and_send_keys(input_form_last_name_locator, name)
                    find_element_and_click(input_form_first_name_locator)
                    name_value = find_element_and_get_attribute(input_form_last_name_locator, value_attribute)
                    print(name, name_value)
                    assert name_value.lower() == name.lower()
                    assert is_element_visible(input_form_last_name_error_text_locator, 1) is True
                    assert find_element_and_get_text(input_form_last_name_error_text_locator) == \
                           input_form_name_error_text

                    refresh_page()

            def test_input_form_last_name_failure_with_digits(self):
                for name in with_digits_name_list:
                    find_element_and_send_keys(input_form_last_name_locator, name)
                    find_element_and_click(input_form_first_name_locator)
                    name_value = find_element_and_get_attribute(input_form_last_name_locator, value_attribute)
                    print(name, name_value)
                    assert name_value.lower() == name.lower()
                    assert is_element_visible(input_form_last_name_error_text_locator, 1) is True
                    assert find_element_and_get_text(input_form_last_name_error_text_locator) == \
                           input_form_name_error_text

                    refresh_page()

            def test_input_form_last_name_failure_with_other_special_chars(self):
                for name in with_other_special_chars_name_list:
                    find_element_and_send_keys(input_form_last_name_locator, name)
                    find_element_and_click(input_form_first_name_locator)
                    name_value = find_element_and_get_attribute(input_form_last_name_locator, value_attribute)
                    print(name, name_value)
                    assert name_value.lower() == name.lower()
                    assert is_element_visible(input_form_last_name_error_text_locator, 1) is True
                    assert find_element_and_get_text(input_form_last_name_error_text_locator) == \
                           input_form_name_error_text

                    refresh_page()

    @pytest.mark.usefixtures('open_test_page_login')
    class TestRegisterFormScenario:
        def test_auth_page(self):
            assert get_current_url(auth_page_title_locator).startswith(auth_url)

        class TestRegisterFormScenarioSuccess:
            def test_register_form_by_phone_scenario_success(self):
                assert is_element_visible(login_form_locator) is True  # Клиент переходит на страницу авторизации
                assert find_element_and_get_text(login_form_title_locator) == login_form_title

                assert is_element_visible(register_link_locator) is True  # Клиент нажимает на ссылку
                # "Зарегистрироваться"
                assert find_element_and_get_text(register_link_locator) == register_link_text
                find_element_and_click(register_link_locator)

                assert is_element_visible(register_form_locator) is True  # Система отображает форму регистрации,
                # которая делится по вертикали на две половины;
                assert find_element_and_get_text(register_form_title_locator) == register_form_title
                assert is_element_visible(page_right_locator) is True
                assert is_element_visible(page_left_locator) is True

                assert find_element(register_form_locator) == find_element(register_form_page_right_locator)  # Правая
                # часть содержит:

                assert is_element_visible(input_form_first_name_locator) is True  # Поле ввода имени
                assert find_element_and_get_text(input_form_first_name_placeholder_locator) == \
                       input_form_first_name_placeholder

                assert is_element_visible(input_form_last_name_locator) is True  # Поле ввода фамилии
                assert find_element_and_get_text(input_form_last_name_placeholder_locator) == \
                       input_form_last_name_placeholder

                assert is_element_visible(select_input_form_region_locator) is True  # Поле выбора региона
                assert find_element_and_get_text(select_input_form_region_placeholder_locator) == \
                       select_input_form_region_placeholder

                assert is_element_visible(input_form_address_locator) is True  # Поле ввода email или мобильного
                # телефона
                assert find_element_and_get_text(input_form_address_placeholder_locator) == \
                       input_form_address_placeholder

                assert is_element_visible(input_form_password_register_locator) is True  # Поле ввода пароля
                assert find_element_and_get_text(input_form_password_register_placeholder_locator) == \
                       input_form_password_register_placeholder

                assert is_element_visible(input_form_password_confirm_register_locator) is True  # Поле подтверждения
                # пароля
                assert find_element_and_get_text(input_form_password_confirm_register_placeholder_locator) == \
                       input_form_password_confirm_register_placeholder

                assert is_element_visible(button_register_locator) is True  # Кнопка "Продолжить"
                assert find_element_and_get_text(button_register_locator) == button_register_text

                assert is_element_visible(link_agreement_locator) is True  # Ссылки на политику конфиденциальности и
                # пользовательское соглашение
                assert find_element_and_get_attribute(link_agreement_locator, href_attribute) == link_agreement_href
                assertion_error = None

                for word in link_agreement_text_parts_list:
                    try:
                        assert word in find_element_and_get_text(link_agreement_locator)
                    except AssertionError:
                        assertion_error = f"{word} not in {find_element_and_get_text(link_agreement_locator)}"
                        print("\n", "\033[31m{}".format(AssertionError), "\033[0m{}".format(assertion_error))
                if assertion_error:
                    fail_test()

                assert is_element_visible(what_is_logo_locator) is True  # Левая часть содержит логотип и продуктовый
                # слоган кабинета
                assert is_element_visible(what_is_title_locator) is True
                assert is_element_visible(what_is_description_locator) is True
                assert find_element_and_get_text(what_is_title_locator) == what_is_title_text
                assert find_element_and_get_text(what_is_description_locator) is not None

                find_element_and_send_keys(input_form_first_name_locator, valid_name)  # Пользователь заполняет
                # поле для ввода имени
                name_value = find_element_and_get_attribute(input_form_first_name_locator, value_attribute)
                assert name_value.lower() == valid_name.lower()
                assert is_element_visible(input_form_first_name_error_text_locator, 1) is False  # Система проверяет на
                # корректность введенные данные

                find_element_and_send_keys(input_form_last_name_locator, valid_name)  # Пользователь заполняет
                # поле для ввода фамилии
                name_value = find_element_and_get_attribute(input_form_last_name_locator, value_attribute)
                assert name_value.lower() == valid_name.lower()
                assert is_element_visible(input_form_last_name_error_text_locator, 1) is False  # Система проверяет на
                # корректность введенные данные

                assert region_default in find_element_and_get_attribute(select_input_form_region_locator,
                                                                        value_attribute)  # Регион по умолчанию

                find_element_and_click(select_input_form_region_locator)
                assert is_element_visible(select_item_list_region_locator) is True
                random_region_locator = add_index_to_locator(select_item_region_locator, regions_count)
                random_region_text = find_element_and_get_text(random_region_locator)
                move_to_element(random_region_locator)
                find_element_and_click(random_region_locator)
                assert find_element_and_get_attribute(select_input_form_region_locator, value_attribute) ==\
                       random_region_text

                find_element_and_send_keys(input_form_address_locator, valid_phone)  # Пользователь
                # вводит email или телефон
                find_element_and_click(input_form_password_register_locator)
                assert find_element_and_get_attribute(input_form_address_locator, value_attribute) == valid_phone_form\
                       or find_element_and_get_attribute(input_form_address_locator, value_attribute) == valid_phone
                assert is_element_visible(input_form_address_error_text_locator, 1) is False  # Система проверяет формат
                # введенного адреса\телефона

                find_element_and_send_keys(input_form_password_register_locator, new_valid_password)  # Пользователь
                # вводит пароль
                find_element_and_click(input_form_password_confirm_register_locator)
                assert find_element_and_get_attribute(input_form_password_register_locator, value_attribute) ==\
                       new_valid_password
                assert is_element_visible(input_form_password_register_error_text_locator, 1) is False  # Система
                # проверяет корректность пароля

                find_element_and_send_keys(input_form_password_confirm_register_locator, new_valid_password)
                # Пользователь вводит подтверждение пароля
                find_element_and_click(input_form_password_register_locator)
                assert find_element_and_get_attribute(input_form_password_confirm_register_locator, value_attribute) ==\
                       new_valid_password
                assert is_element_visible(input_form_password_confirm_register_error_text_locator, 1) is False
                # Система проверяет корректность пароля

                find_element_and_click(button_register_locator)  # Пользователь нажимает кнопку "Продолжить"

                assert is_element_visible(register_confirm_form_locator) is True  # Открывается форма с полем для ввода
                # кода
                assert find_element_and_get_text(register_confirm_form_title_locator) ==\
                       register_confirm_form_title_phone
                assert valid_phone in find_element_and_get_text(register_confirm_form_description_locator)\
                       or valid_phone_form in find_element_and_get_text(register_confirm_form_description_locator)
                assert is_all_elements_visible(input_register_code_all_locator) is True  # Шесть отдельных полей для
                # ввода кода подтверждения
                assert len(find_elements(input_register_code_all_locator)) == count_code_input
                assert is_element_visible(register_resend_code_timeout_text_locator) is True  # Текст с обратным
                # отсчётом времени до повторной попытки отправки код
                assert resend_code_timeout_text in find_element_and_get_text(register_resend_code_timeout_text_locator)

                assert is_element_visible(button_register_resend_code_locator, sleep=resend_code_timeout) is True
                # Кнопка "Получить код повторно"
                assert is_element_visible(button_register_confirm_back_locator) is True  # Кнопка "Вернуться назад"
                assert find_element_and_get_text(button_register_confirm_back_locator) ==\
                       button_register_confirm_back_text_phone

                elements = find_elements(input_register_code_all_locator)  # Клиент начинает вводить полученный код
                parent_elements = find_elements(input_code_parent_all_locator)

                i = 0
                while i < count_code_input:
                    for element in elements:
                        assert parent_elements[i] == find_element(input_code_parent_active_locator)
                        element.send_keys(valid_otp[i])
                        i += 1

                assert get_current_url(account_page_title_locator).startswith(account_url)  # Пользователь
                # перенаправляется в кабинет инициатор

                find_element_and_click(button_account_page_logout_locator)  # Возвращение на страницу авторизации
                assert get_current_url(auth_page_title_locator).startswith(auth_url)

            def test_register_form_by_mail_scenario_success(self):
                assert is_element_visible(login_form_locator) is True  # Клиент переходит на страницу авторизации
                assert find_element_and_get_text(login_form_title_locator) == login_form_title

                assert is_element_visible(register_link_locator) is True  # Клиент нажимает на ссылку
                # "Зарегистрироваться"
                assert find_element_and_get_text(register_link_locator) == register_link_text
                find_element_and_click(register_link_locator)

                assert is_element_visible(register_form_locator) is True  # Система отображает форму регистрации,
                # которая делится по вертикали на две половины;
                assert find_element_and_get_text(register_form_title_locator) == register_form_title
                assert is_element_visible(page_right_locator) is True
                assert is_element_visible(page_left_locator) is True

                assert find_element(register_form_locator) == find_element(register_form_page_right_locator)  # Правая
                # часть содержит:

                assert is_element_visible(input_form_first_name_locator) is True  # Поле ввода имени
                assert find_element_and_get_text(input_form_first_name_placeholder_locator) == \
                       input_form_first_name_placeholder

                assert is_element_visible(input_form_last_name_locator) is True  # Поле ввода фамилии
                assert find_element_and_get_text(input_form_last_name_placeholder_locator) == \
                       input_form_last_name_placeholder

                assert is_element_visible(select_input_form_region_locator) is True  # Поле выбора региона
                assert find_element_and_get_text(select_input_form_region_placeholder_locator) == \
                       select_input_form_region_placeholder

                assert is_element_visible(input_form_address_locator) is True  # Поле ввода email или мобильного
                # телефона
                assert find_element_and_get_text(input_form_address_placeholder_locator) == \
                       input_form_address_placeholder

                assert is_element_visible(input_form_password_register_locator) is True  # Поле ввода пароля
                assert find_element_and_get_text(input_form_password_register_placeholder_locator) == \
                       input_form_password_register_placeholder

                assert is_element_visible(input_form_password_confirm_register_locator) is True  # Поле подтверждения
                # пароля
                assert find_element_and_get_text(input_form_password_confirm_register_placeholder_locator) == \
                       input_form_password_confirm_register_placeholder

                assert is_element_visible(button_register_locator) is True  # Кнопка "Продолжить"
                assert find_element_and_get_text(button_register_locator) == button_register_text

                assert is_element_visible(link_agreement_locator) is True  # Ссылки на политику конфиденциальности и
                # пользовательское соглашение
                assert find_element_and_get_attribute(link_agreement_locator, href_attribute) == link_agreement_href
                assertion_error = None

                for word in link_agreement_text_parts_list:
                    try:
                        assert word in find_element_and_get_text(link_agreement_locator)
                    except AssertionError:
                        assertion_error = f"{word} not in {find_element_and_get_text(link_agreement_locator)}"
                        print("\n", "\033[31m{}".format(AssertionError), "\033[0m{}".format(assertion_error))
                if assertion_error:
                    fail_test()

                assert is_element_visible(what_is_logo_locator) is True  # Левая часть содержит логотип и продуктовый
                # слоган кабинета
                assert is_element_visible(what_is_title_locator) is True
                assert is_element_visible(what_is_description_locator) is True
                assert find_element_and_get_text(what_is_title_locator) == what_is_title_text
                assert find_element_and_get_text(what_is_description_locator) is not None

                find_element_and_send_keys(input_form_first_name_locator, valid_name)  # Пользователь заполняет
                # поле для ввода имени
                name_value = find_element_and_get_attribute(input_form_first_name_locator, value_attribute)
                assert name_value.lower() == valid_name.lower()
                assert is_element_visible(input_form_first_name_error_text_locator, 1) is False  # Система проверяет на
                # корректность введенные данные

                find_element_and_send_keys(input_form_last_name_locator, valid_name)  # Пользователь заполняет
                # поле для ввода фамилии
                name_value = find_element_and_get_attribute(input_form_last_name_locator, value_attribute)
                assert name_value.lower() == valid_name.lower()
                assert is_element_visible(input_form_last_name_error_text_locator, 1) is False  # Система проверяет на
                # корректность введенные данные

                assert region_default in find_element_and_get_attribute(select_input_form_region_locator,
                                                                        value_attribute)  # Регион по умолчанию

                find_element_and_click(select_input_form_region_locator)
                assert is_element_visible(select_item_list_region_locator) is True
                random_region_locator = add_index_to_locator(select_item_region_locator, regions_count)
                random_region_text = find_element_and_get_text(random_region_locator)
                move_to_element(random_region_locator)
                find_element_and_click(random_region_locator)
                assert find_element_and_get_attribute(select_input_form_region_locator, value_attribute) == \
                       random_region_text

                find_element_and_send_keys(input_form_address_locator, valid_mail)  # Пользователь
                # вводит email или телефон
                find_element_and_click(input_form_password_register_locator)
                assert find_element_and_get_attribute(input_form_address_locator, value_attribute) == valid_mail
                assert is_element_visible(input_form_address_error_text_locator, 1) is False  # Система проверяет формат
                # введенного адреса\телефона

                find_element_and_send_keys(input_form_password_register_locator, new_valid_password)  # Пользователь
                # вводит пароль
                find_element_and_click(input_form_password_confirm_register_locator)
                assert find_element_and_get_attribute(input_form_password_register_locator, value_attribute) == \
                       new_valid_password
                assert is_element_visible(input_form_password_register_error_text_locator, 1) is False  # Система
                # проверяет корректность пароля

                find_element_and_send_keys(input_form_password_confirm_register_locator, new_valid_password)
                # Пользователь вводит подтверждение пароля
                find_element_and_click(input_form_password_register_locator)
                assert find_element_and_get_attribute(input_form_password_confirm_register_locator, value_attribute) ==\
                       new_valid_password
                assert is_element_visible(input_form_password_confirm_register_error_text_locator, 1) is False
                # Система проверяет корректность пароля

                find_element_and_click(button_register_locator)  # Пользователь нажимает кнопку "Продолжить"

                assert is_element_visible(register_confirm_form_locator) is True  # Открывается форма с полем для ввода
                # кода
                assert find_element_and_get_text(register_confirm_form_title_locator) == \
                       register_confirm_form_title_mail
                assert valid_mail in find_element_and_get_text(register_confirm_form_description_locator)
                assert is_all_elements_visible(input_register_code_all_locator) is True  # Шесть отдельных полей для
                # ввода кода подтверждения
                assert len(find_elements(input_register_code_all_locator)) == count_code_input
                assert is_element_visible(register_resend_code_timeout_text_locator) is True  # Текст с обратным
                # отсчётом времени до повторной попытки отправки код
                assert resend_code_timeout_text in find_element_and_get_text(register_resend_code_timeout_text_locator)

                assert is_element_visible(button_register_resend_code_locator, sleep=resend_code_timeout) is True
                # Кнопка "Получить код повторно"
                assert is_element_visible(button_register_confirm_back_locator) is True  # Кнопка "Вернуться назад"
                assert find_element_and_get_text(button_register_confirm_back_locator) == \
                       button_register_confirm_back_text_mail

                elements = find_elements(input_register_code_all_locator)  # Клиент начинает вводить полученный код
                parent_elements = find_elements(input_code_parent_all_locator)

                i = 0
                while i < count_code_input:
                    for element in elements:
                        assert parent_elements[i] == find_element(input_code_parent_active_locator)
                        element.send_keys(valid_otp[i])
                        i += 1

                assert get_current_url(account_page_title_locator).startswith(account_url)  # Пользователь
                # перенаправляется в кабинет инициатор

                find_element_and_click(button_account_page_logout_locator)  # Возвращение на страницу авторизации
                assert get_current_url(auth_page_title_locator).startswith(auth_url)
