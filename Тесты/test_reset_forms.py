import pytest

from calculated_variables import *
from locators import *


@pytest.mark.usefixtures('open_test_page_reset')
class TestResetForm:
    def test_reset_page(self):
        assert get_current_url(auth_page_title_locator).startswith(reset_form_url)

    class TestResetFormElementsVisibility:  # Видимость элементов формы восстановления пароля
        def test_reset_form_visible(self):  # Система отображает форму «Восстановление пароля»
            assert is_element_visible(reset_form_locator) is True

        def test_reset_form_title_visible(self):
            assert is_element_visible(reset_form_title_locator) is True
            assert find_element_and_get_text(reset_form_title_locator) == reset_form_title

        def test_reset_type_menu_visible(self):  # Меню выбора типа ввода контактных данных
            assert is_element_visible(reset_type_menu_locator) is True

        def test_reset_type_menu_tab_phone_visible(self):  # Таб выбора восстановления пароля по номеру, "Телефон"
            assert is_element_visible(reset_type_menu_tab_phone_locator) is True
            assert find_element_and_get_text(reset_type_menu_tab_phone_locator) == auth_type_menu_tab_phone_text

        def test_reset_type_menu_tab_mail_visible(self):  # Таб выбора восстановления пароля по почте, "Почта"
            assert is_element_visible(reset_type_menu_tab_mail_locator) is True
            assert find_element_and_get_text(reset_type_menu_tab_mail_locator) == auth_type_menu_tab_mail_text

        def test_reset_type_menu_tab_login_visible(self):  # Таб выбора восстановления пароля по логину, "Логин"
            assert is_element_visible(reset_type_menu_tab_login_locator) is True
            assert find_element_and_get_text(reset_type_menu_tab_login_locator) == auth_type_menu_tab_login_text

        def test_auth_type_menu_tab_personal_account_visible(self):  # Таб выбора восстановления пароля по лицевому
            # счёту, "Лицевой счёт"
            assert is_element_visible(reset_type_menu_tab_personal_account_locator) is True
            assert find_element_and_get_text(reset_type_menu_tab_personal_account_locator) == \
                   auth_type_menu_tab_personal_account_text

        def test_input_form_phone_visible_default(self):  # Форма ввода "Телефон" по умолчанию
            assert is_element_visible(reset_type_menu_tab_phone_locator) is True
            assert is_element_visible(input_form_username_reset_locator) is True
            assert find_element(reset_type_menu_tab_phone_locator) == find_element(reset_type_menu_tab_active_locator)
            assert find_element_and_get_text(input_form_username_placeholder_locator) == \
                   input_form_username_phone_placeholder

        def test_input_form_mail_visible(self):  # Форма ввода "Почта"
            assert is_element_visible(reset_type_menu_tab_mail_locator) is True
            find_element_and_click(reset_type_menu_tab_mail_locator)

            assert is_element_visible(input_form_username_reset_locator) is True
            assert find_element_and_get_text(input_form_username_placeholder_locator) == \
                   input_form_username_mail_placeholder
            assert find_element_and_get_text(input_form_password_placeholder_locator) == \
                   input_form_password_placeholder

        def test_input_form_login_visible(self):  # Форма ввода "Логин"
            assert is_element_visible(reset_type_menu_tab_login_locator) is True
            find_element_and_click(reset_type_menu_tab_login_locator)

            assert is_element_visible(input_form_username_reset_locator) is True
            assert find_element_and_get_text(input_form_username_placeholder_locator) == \
                   input_form_username_login_placeholder

        def test_input_form_personal_account_visible(self):  # Форма ввода "Лицевой счёт"
            assert is_element_visible(reset_type_menu_tab_personal_account_locator) is True
            find_element_and_click(reset_type_menu_tab_personal_account_locator)

            assert is_element_visible(input_form_username_reset_locator) is True
            assert find_element_and_get_text(input_form_username_placeholder_locator) == \
                   input_form_username_personal_account_placeholder

        def test_captcha_form_visible(self):  # Форма "Капча"
            assert is_element_visible(input_form_captcha_locator) is True
            assert is_element_visible(image_captcha_locator) is True
            assert find_element_and_get_attribute(image_captcha_locator, src_attribute) is not None
            assert is_element_visible(button_reload_captcha_locator) is True

        def test_button_reset_visible(self):  # Кнопка "Продолжить"
            assert is_element_visible(button_reset_locator) is True
            assert find_element_and_get_text(button_reset_locator) == button_reset_text

        def test_button_reset_back_visible(self):  # Кнопка "Вернуться назад"
            assert is_element_visible(button_reset_back_locator) is True
            assert find_element_and_get_text(button_reset_back_locator) == button_reset_back_text

    def test_autochange_reset_type_tabs(self):  # При вводе номера телефона/почты/логина/лицевого счета - таб выбора
        # восстановления пароля меняется автоматически.
        """Если при вводе данных в корректном формате не происходит автоматическое переключение между табами, выводится
        сообщение об ошибке, содержащее вводимое значение данных, название ожидаемого активного таба и название
        фактического активного таба."""
        assertion_error = None

        for locator in reset_tabs_locators_and_input_form_username_placeholders_dict:
            placeholder = reset_tabs_locators_and_input_form_username_placeholders_dict[locator]
            tab_text = reset_tabs_locators_and_auth_type_menu_tab_text_dict[locator]

            for locator_ in reset_tabs_locators_and_data_correct_dict:
                assert is_element_visible(locator) is True
                assert find_element_and_get_text(locator) == tab_text

                find_element_and_click(locator)
                assert find_element(locator) == find_element(auth_type_menu_tab_active_locator)

                assert is_element_visible(input_form_username_reset_locator) is True
                assert find_element_and_get_text(input_form_username_placeholder_locator) == placeholder

                data_ = reset_tabs_locators_and_data_correct_dict[locator_]
                placeholder_ = reset_tabs_locators_and_input_form_username_placeholders_dict[locator_]
                tab_text_ = reset_tabs_locators_and_auth_type_menu_tab_text_dict[locator_]

                find_element_and_send_keys(input_form_username_reset_locator, data_)
                find_element_and_click(input_form_captcha_locator)
                # time.sleep(2)
                try:
                    assert find_element_and_get_attribute(input_form_username_value_locator, value_attribute) == data_
                    assert find_element(locator_) == find_element(auth_type_menu_tab_active_locator)
                    assert find_element_and_get_text(locator_) == tab_text_
                    assert find_element_and_get_text(input_form_username_placeholder_locator) == placeholder_
                except AssertionError:
                    received_data_value = find_element_and_get_attribute(input_form_username_value_locator,
                                                                         value_attribute)
                    active_tab_text = find_element_and_get_text(auth_type_menu_tab_active_locator)
                    assertion_error = f"Input Data: {data_};" \
                                      f" Received Data Value: {received_data_value};" \
                                      f" Expected Tab: {tab_text_};" \
                                      f" Active Tab: {active_tab_text}"
                    print("\n", "\033[31m{}".format(AssertionError), "\033[0m{}".format(assertion_error))
                finally:
                    refresh_page()
        if assertion_error:
            fail_test()


@pytest.mark.usefixtures('open_test_page_reset')
class TestResetFormsScenario:
    def test_reset_page(self):
        assert get_current_url(auth_page_title_locator).startswith(reset_form_url)

    class TestResetFormsScenarioSuccess:
        @pytest.mark.skip(reason="Нет капчи valid_captcha и временного кода valid_otp для теста")
        def test_reset_forms_phone_by_phone_scenario_success(self):  # Восстановление пароля клиента по номеру телефона,
            # кнопка "По номеру телефона"
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
                   valid_phone or find_element_and_get_attribute(input_form_username_value_locator, value_attribute) ==\
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

            find_element_and_click(radio_input_by_phone_locator)  # Пользователь выбирает восстановить по номеру
            # телефона
            assert find_element(radio_input_by_phone_locator) == find_element(radio_input_active_locator)

            find_element_and_click(button_reset_choice_locator)
            assert is_element_visible(reset_confirm_form_locator) is True  # Открывается форма с полем для ввода кода
            # из СМС
            assert find_element_and_get_text(reset_choice_form_title_locator) == reset_choice_form_title
            assert valid_phone in find_element_and_get_text(reset_confirm_form_description_locator)\
                   or valid_phone_form in find_element_and_get_text(reset_confirm_form_description_locator)
            assert is_all_elements_visible(input_reset_code_all_locator) is True  # Шесть отдельных полей для ввода кода
            # подтверждения
            assert len(find_elements(input_reset_code_all_locator)) == count_code_input
            assert is_element_visible(reset_resend_code_timeout_text_locator) is True  # Текст с обратным отсчётом
            # времени
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
            assert find_element_and_get_text(update_password_form_description_locator) ==\
                   update_password_form_description
            assert is_element_visible(input_form_new_password_locator) is True  # Поле ввода нового пароля
            assert find_element_and_get_text(input_form_new_password_placeholder) == input_form_new_password_placeholder
            assert is_element_visible(
                input_form_password_confirm_locator) is True  # Поле ввода для подтверждения нового пароля
            assert find_element_and_get_text(
                input_form_password_confirm_placeholder) == input_form_password_confirm_placeholder
            assert is_element_visible(button_update_locator) is True  # Кнопка "Сохранить" для подтверждения нового
            # пароля
            assert find_element_and_get_text(button_update_locator) == button_update_text
            assert is_element_clickable(button_update_locator) is False

            find_element_and_send_keys(input_form_new_password_locator,
                                       new_valid_password)  # Пользователь вводит новый пароль,
            # подтверждение пароля и нажимает кнопку "Сохранить"
            find_element_and_click(input_form_password_confirm_locator)
            assert is_element_visible(input_form_error_text_locator, 1) is False
            assert find_element_and_get_attribute(input_form_password_confirm_locator, value_attribute) == \
                   new_valid_password

            find_element_and_send_keys(input_form_password_confirm_locator, new_valid_password)  # подтверждение пароля
            find_element_and_click(input_form_new_password_locator)
            assert is_element_visible(input_form_error_text_locator, 1) is False
            assert find_element_and_get_attribute(input_form_password_confirm_locator, value_attribute) == \
                   new_valid_password

            find_element_and_click(button_update_locator)  # нажимает кнопку "Сохранить"
            assert is_element_visible(input_form_error_text_locator, 1) is False

            assert is_element_visible(login_form_locator) is True  # Клиент перенаправляется на страницу авторизации.

            open_page(reset_form_url)

        @pytest.mark.skip(reason="Нет капчи valid_captcha и временного кода valid_otp для теста")
        def test_reset_forms_phone_by_mail_scenario_success(self):  # Восстановление пароля клиента по номеру телефона,
            # кнопка "По e-mail"
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
                   valid_phone or find_element_and_get_attribute(input_form_username_value_locator, value_attribute) ==\
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

            find_element_and_click(radio_input_by_mail_locator)  # Пользователь выбирает восстановить по e-mail
            assert find_element(radio_input_by_mail_locator) == find_element(radio_input_active_locator)

            find_element_and_click(button_reset_choice_locator)
            assert is_element_visible(reset_confirm_form_locator) is True  # Открывается форма с полем для ввода кода из
            # e-mail
            assert find_element_and_get_text(reset_choice_form_title_locator) == reset_choice_form_title
            assert valid_phone in find_element_and_get_text(reset_confirm_form_description_locator)\
                   or valid_phone_form in find_element_and_get_text(reset_confirm_form_description_locator)
            assert is_all_elements_visible(input_reset_code_all_locator) is True  # Шесть отдельных полей для ввода кода
            # подтверждения
            assert len(find_elements(input_reset_code_all_locator)) == count_code_input
            assert is_element_visible(reset_resend_code_timeout_text_locator) is True  # Текст с обратным отсчётом
            # времени
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
            assert find_element_and_get_text(update_password_form_description_locator) ==\
                   update_password_form_description
            assert is_element_visible(input_form_new_password_locator) is True  # Поле ввода нового пароля
            assert find_element_and_get_text(input_form_new_password_placeholder) == input_form_new_password_placeholder
            assert is_element_visible(
                input_form_password_confirm_locator) is True  # Поле ввода для подтверждения нового пароля
            assert find_element_and_get_text(
                input_form_password_confirm_placeholder) == input_form_password_confirm_placeholder
            assert is_element_visible(button_update_locator) is True  # Кнопка "Сохранить" для подтверждения нового
            # пароля
            assert find_element_and_get_text(button_update_locator) == button_update_text
            assert is_element_clickable(button_update_locator) is False

            find_element_and_send_keys(input_form_new_password_locator, new_valid_password)  # Пользователь вводит новый
            # пароль, подтверждение пароля и нажимает кнопку "Сохранить"
            find_element_and_click(input_form_password_confirm_locator)
            assert find_element_and_get_attribute(input_form_new_password_locator, value_attribute) == \
                   new_valid_password
            assert is_element_visible(input_form_error_text_locator, 1) is False

            find_element_and_send_keys(input_form_password_confirm_locator, new_valid_password)  # подтверждение пароля
            find_element_and_click(input_form_new_password_locator)
            assert find_element_and_get_attribute(input_form_password_confirm_locator, value_attribute) == \
                   new_valid_password
            assert is_element_visible(input_form_error_text_locator, 1) is False

            find_element_and_click(button_update_locator)  # нажимает кнопку "Сохранить"
            assert is_element_visible(input_form_error_text_locator, 1) is False

            assert is_element_visible(login_form_locator) is True  # Клиент перенаправляется на страницу авторизации.

            open_page(reset_form_url)

        def test_reset_forms_scenario_success_back_to_login_form(self):  # Возврат на форму авторизации
            assert is_element_visible(button_reset_back_locator) is True
            assert find_element_and_get_text(button_reset_back_locator) == button_reset_back_text

            find_element_and_click(button_reset_back_locator)
            assert is_element_visible(login_form_locator) is True
            assert is_element_visible(login_form_title_locator) is True
            assert find_element_and_get_text(login_form_title_locator) == login_form_title

            open_page(reset_form_url)

    class TestResetFormsScenarioFailure:
        def test_reset_forms_scenario_failure_invalid_captcha(self):  # Введена неверная капча
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
                   valid_phone or find_element_and_get_attribute(input_form_username_value_locator, value_attribute) ==\
                   valid_phone_form

            find_element_and_send_keys(input_form_captcha_locator, invalid_captcha)
            find_element_and_click(input_form_username_reset_locator)
            assert find_element_and_get_attribute(input_form_captcha_locator, value_attribute) == invalid_captcha

            find_element_and_click(button_reset_locator)
            assert is_element_visible(reset_form_error_text_locator) is True
            assert find_element_and_get_text(reset_form_error_text_locator) == reset_form_error_text


@pytest.mark.skip(reason="Нет капчи valid_captcha")
@pytest.mark.usefixtures('go_to_reset_choice_form')
class TestResetChoiceForm:
    class TestResetChoiceFormScenarioSuccess:
        def test_reset_choice_form_scenario_success_back_to_reset_form(self):  # Возврат на форму восстановления пароля
            assert is_element_visible(button_reset_choice_back_locator) is True
            assert find_element_and_get_text(button_reset_choice_back_locator) == button_reset_choice_back_text

            find_element_and_click(button_reset_choice_back_locator)
            assert is_element_visible(reset_form_locator) is True
            assert is_element_visible(reset_form_title_locator) is True
            assert find_element_and_get_text(reset_form_title_locator) == reset_form_title


@pytest.mark.skip(reason="Нет капчи valid_captcha")
@pytest.mark.usefixtures('go_to_reset_form')
class TestResetConfirmForm:
    class TestResetConfirmFormScenarioSuccess:
        def test_reset_confirm_form_scenario_success_back_to_reset_form(self):  # Возврат на форму
            # восстановления пароля
            assert is_element_visible(button_reset_confirm_back_locator) is True
            assert find_element_and_get_text(button_reset_confirm_back_locator) == button_reset_confirm_back_text

            find_element_and_click(button_reset_confirm_back_locator)
            assert is_element_visible(reset_form_locator) is True
            assert is_element_visible(reset_form_title_locator) is True
            assert find_element_and_get_text(reset_form_title_locator) == reset_form_title

    class TestResetConfirmFormScenarioFailure:
        def test_reset_confirm_form_scenario_failure_invalid_otp(self):  # Неверный код
            elements = find_elements(input_reset_code_all_locator)  # Клиент начинает вводить код
            parent_elements = find_elements(input_code_parent_all_locator)

            i = 0
            while i < count_code_input:
                for element in elements:
                    assert parent_elements[i] == find_element(input_code_parent_active_locator)
                    element.send_keys(invalid_otp[i])
                    i += 1

            assert is_element_visible(reset_code_error_locator) is True
            assert find_element_and_get_text(reset_code_error_locator) == code_error_invalid_text

        def test_reset_confirm_form_scenario_failure_expired_code(self):  # Истекший код
            elements = find_elements(input_reset_code_all_locator)  # Клиент начинает вводить код
            parent_elements = find_elements(input_code_parent_all_locator)

            i = 0
            while i < count_code_input:
                for element in elements:
                    assert parent_elements[i] == find_element(input_code_parent_active_locator)
                    element.send_keys(expired_otp[i])
                    i += 1

            assert is_element_visible(reset_code_error_locator) is True
            assert find_element_and_get_text(reset_code_error_locator) == code_error_expired_text


@pytest.mark.skip(reason="Нет капчи valid_captcha и временного кода valid_otp для теста")
@pytest.mark.usefixtures('go_to_update_password_form')
class TestUpdatePasswordForm:
    class TestUpdatePasswordFormElements:
        def test_input_form_new_password_success(self):
            for password in valid_passwords_list:
                find_element_and_send_keys(input_form_new_password_locator, password)
                find_element_and_click(input_form_password_confirm_locator)
                assert find_element_and_get_attribute(input_form_password_confirm_locator, value_attribute) == password
                assert is_element_visible(input_form_new_password_error_text_locator, 1) is False

                refresh_page()

        def test_input_form_password_confirm_success(self):
            for password in valid_passwords_list:
                find_element_and_send_keys(input_form_password_confirm_locator, password)
                find_element_and_click(input_form_new_password_locator)
                assert find_element_and_get_attribute(input_form_password_confirm_locator, value_attribute) == password
                assert is_element_visible(input_form_password_confirm_error_text_locator, 1) is False

                refresh_page()

        class TestInputFormNewPasswordFailure:
            def test_input_form_new_password_failure_valid_chars_invalid_len(self):
                for password in valid_chars_invalid_len_passwords_list:
                    find_element_and_send_keys(input_form_new_password_locator, password)
                    find_element_and_click(input_form_password_confirm_locator)
                    assert find_element_and_get_attribute(input_form_new_password_locator, value_attribute) == password
                    if 0 < len(password) < password_valid_len_interval_list[0]:
                        assert is_element_visible(input_form_new_password_error_text_locator, 1) is True
                        assert find_element_and_get_text(input_form_new_password_error_text_locator) == \
                               input_form_password_error_less_len_text
                    elif len(password) > password_valid_len_interval_list[1]:
                        assert is_element_visible(input_form_new_password_error_text_locator, 1) is True
                        assert find_element_and_get_text(input_form_new_password_error_text_locator) == \
                               input_form_password_error_more_len_text
                    elif len(password) == 0:
                        assert is_element_visible(input_form_new_password_error_text_locator, 1) is False

                    refresh_page()

            def test_input_form_new_password_failure_valid_len_no_uppercase_letters(self):
                for password in no_uppercase_letters_passwords_list:
                    find_element_and_send_keys(input_form_new_password_locator, password)
                    find_element_and_click(input_form_password_confirm_locator)
                    assert find_element_and_get_attribute(input_form_new_password_locator, value_attribute) == password
                    assert is_element_visible(input_form_new_password_error_text_locator, 1) is True
                    assert find_element_and_get_text(input_form_new_password_error_text_locator) == \
                           input_form_password_error_no_uppercase_letters_text

                    refresh_page()

            def test_input_form_new_password_failure_valid_len_no_lowercase_letters(self):
                for password in no_lowercase_letters_passwords_list:
                    find_element_and_send_keys(input_form_new_password_locator, password)
                    find_element_and_click(input_form_password_confirm_locator)
                    assert find_element_and_get_attribute(input_form_new_password_locator, value_attribute) == password
                    assert is_element_visible(input_form_new_password_error_text_locator, 1) is True
                    assert find_element_and_get_text(input_form_new_password_error_text_locator) == \
                           input_form_password_error_no_lowercase_letters_text

                    refresh_page()

            def test_input_form_new_password_failure_valid_len_no_digits_or_special_chars(self):
                for password in no_digits_or_special_chars_passwords_list:
                    find_element_and_send_keys(input_form_new_password_locator, password)
                    find_element_and_click(input_form_password_confirm_locator)
                    assert find_element_and_get_attribute(input_form_new_password_locator, value_attribute) == password
                    assert is_element_visible(input_form_new_password_error_text_locator, 1) is True
                    assert find_element_and_get_text(input_form_new_password_error_text_locator) == \
                           input_form_password_error_no_digits_or_special_chars_text

                    refresh_page()

            def test_input_form_new_password_failure_valid_len_not_only_latin_letters(self):
                for password in not_only_latin_letters_passwords_list:
                    find_element_and_send_keys(input_form_new_password_locator, password)
                    find_element_and_click(input_form_password_confirm_locator)
                    assert find_element_and_get_attribute(input_form_new_password_locator, value_attribute) == password
                    assert is_element_visible(input_form_new_password_error_text_locator, 1) is True
                    assert find_element_and_get_text(input_form_new_password_error_text_locator) == \
                           input_form_password_error_not_only_latin_letters_text

                    refresh_page()

        class TestInputFormPasswordConfirmFailure:
            def test_input_form_password_confirm_failure_valid_chars_invalid_len(self):
                for password in valid_chars_invalid_len_passwords_list:
                    find_element_and_send_keys(input_form_password_confirm_locator, password)
                    find_element_and_click(input_form_new_password_locator)
                    assert find_element_and_get_attribute(input_form_password_confirm_locator, value_attribute) ==\
                           password
                    if 0 < len(password) < password_valid_len_interval_list[0]:
                        assert is_element_visible(input_form_password_confirm_error_text_locator, 1) is True
                        assert find_element_and_get_text(input_form_password_confirm_error_text_locator) == \
                               input_form_password_error_less_len_text
                    elif len(password) > password_valid_len_interval_list[1]:
                        assert is_element_visible(input_form_password_confirm_error_text_locator, 1) is True
                        assert find_element_and_get_text(input_form_password_confirm_error_text_locator) == \
                               input_form_password_error_more_len_text
                    elif len(password) == 0:
                        assert is_element_visible(input_form_password_confirm_error_text_locator, 1) is False

                    refresh_page()

            def test_input_form_password_confirm_failure_valid_len_no_uppercase_letters(self):
                for password in no_uppercase_letters_passwords_list:
                    find_element_and_send_keys(input_form_password_confirm_locator, password)
                    find_element_and_click(input_form_new_password_locator)
                    assert find_element_and_get_attribute(input_form_password_confirm_locator, value_attribute) ==\
                           password
                    assert is_element_visible(input_form_password_confirm_error_text_locator, 1) is True
                    assert find_element_and_get_text(input_form_password_confirm_error_text_locator) == \
                           input_form_password_error_no_uppercase_letters_text

                    refresh_page()

            def test_input_form_password_confirm_failure_valid_len_no_lowercase_letters(self):
                for password in no_lowercase_letters_passwords_list:
                    find_element_and_send_keys(input_form_password_confirm_locator, password)
                    find_element_and_click(input_form_new_password_locator)
                    assert find_element_and_get_attribute(input_form_password_confirm_locator, value_attribute) ==\
                           password
                    assert is_element_visible(input_form_password_confirm_error_text_locator, 1) is True
                    assert find_element_and_get_text(input_form_password_confirm_error_text_locator) == \
                           input_form_password_error_no_lowercase_letters_text

                    refresh_page()

            def test_input_form_password_confirm_failure_valid_len_no_digits_or_special_chars(self):
                for password in no_digits_or_special_chars_passwords_list:
                    find_element_and_send_keys(input_form_password_confirm_locator, password)
                    find_element_and_click(input_form_new_password_locator)
                    assert find_element_and_get_attribute(input_form_password_confirm_locator, value_attribute) ==\
                           password
                    assert is_element_visible(input_form_password_confirm_error_text_locator, 1) is True
                    assert find_element_and_get_text(input_form_password_confirm_error_text_locator) == \
                           input_form_password_error_no_digits_or_special_chars_text

                    refresh_page()

            def test_input_form_password_confirm_failure_valid_len_not_only_latin_letters(self):
                for password in no_digits_or_special_chars_passwords_list:
                    find_element_and_send_keys(input_form_password_confirm_locator, password)
                    find_element_and_click(input_form_new_password_locator)
                    assert find_element_and_get_attribute(input_form_password_confirm_locator, value_attribute) ==\
                           password
                    assert is_element_visible(input_form_password_confirm_error_text_locator, 1) is True
                    assert find_element_and_get_text(input_form_password_confirm_error_text_locator) == \
                           input_form_password_error_not_only_latin_letters_text

                    refresh_page()

    class TestUpdatePasswordFormScenario:
        def test_update_password_scenario_failure_empty_input_forms(self):  # Негативный: пустые поля ввода
            for empty in empty_input_list:
                find_element_and_send_keys(input_form_new_password_locator, empty)  # Оба поля пустые
                find_element_and_click(input_form_password_confirm_locator)
                assert find_element_and_get_attribute(input_form_new_password_locator, value_attribute) == ""
                assert is_element_visible(input_form_new_password_error_text_locator, 1) is False
                find_element_and_send_keys(input_form_password_confirm_locator, empty)
                find_element_and_click(input_form_new_password_locator)
                assert find_element_and_get_attribute(input_form_password_confirm_locator, value_attribute) == ""
                assert is_element_visible(input_form_password_confirm_error_text_locator, 1) is False
                assert is_element_clickable(button_update_locator) is False

                find_element_and_send_keys(input_form_new_password_locator, new_valid_password)  # Пустое поле
                # "Подтверждение пароля"
                find_element_and_click(input_form_password_confirm_locator)
                assert find_element_and_get_attribute(input_form_new_password_locator, value_attribute) == \
                       new_valid_password
                assert is_element_visible(input_form_new_password_error_text_locator, 1) is False
                find_element_and_send_keys(input_form_password_confirm_locator, empty)
                find_element_and_click(input_form_new_password_locator)
                assert find_element_and_get_attribute(input_form_password_confirm_locator, value_attribute) == ""
                assert is_element_visible(input_form_password_confirm_error_text_locator, 1) is False
                assert is_element_clickable(button_update_locator) is False

                find_element_and_send_keys(input_form_new_password_locator, empty)  # Пустое поле "Пароль"
                find_element_and_click(input_form_password_confirm_locator)
                assert find_element_and_get_attribute(input_form_new_password_locator, value_attribute) == ""
                assert is_element_visible(input_form_new_password_error_text_locator, 1) is False
                find_element_and_send_keys(input_form_password_confirm_locator, new_valid_password)
                find_element_and_click(input_form_new_password_locator)
                assert find_element_and_get_attribute(input_form_password_confirm_locator, value_attribute) == \
                       new_valid_password
                assert is_element_visible(input_form_password_confirm_error_text_locator, 1) is False
                assert is_element_clickable(button_update_locator) is False

        def test_update_password_scenario_failure_passwords_mismatch(self):  # Негативный: новый пароль и подтверждение
            # пароля не совпадают
            find_element_and_send_keys(input_form_new_password_locator, new_valid_password)
            find_element_and_click(input_form_password_confirm_locator)
            assert find_element_and_get_attribute(input_form_new_password_locator, value_attribute) == \
                   new_valid_password
            assert is_element_visible(input_form_new_password_error_text_locator, 1) is False

            find_element_and_send_keys(input_form_password_confirm_locator, invalid_password)
            find_element_and_click(input_form_new_password_locator)
            assert find_element_and_get_attribute(input_form_password_confirm_locator, value_attribute) ==\
                   invalid_password
            assert is_element_visible(input_form_password_confirm_error_text_locator, 1) is False

            find_element_and_click(button_update_locator)  # нажимает кнопку "Сохранить"
            assert is_element_visible(input_form_password_confirm_error_text_locator, 1) is True
            assert find_element_and_get_text(input_form_password_confirm_error_text_locator) ==\
                   input_form_password_error_passwords_mismatch_text
