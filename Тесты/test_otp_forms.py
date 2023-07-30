import pytest

from calculated_variables import *
from locators import *


@pytest.mark.usefixtures('open_test_page_otp')
class TestOtpForms:
    """1. Система отображает форму «Авторизация по коду», содержащую:
        a) Подсказку по работе с формой “Укажите контактный номер телефона или почту, на которые необходимо отправить
           код подтверждения”;
        b) Поле ввода номера телефона или почты;
        c) Кнопку "Получить код".
       2. Клиент вводит номер телефона/почту и нажимает кнопку "Получить код";
       3. Система:
        a) Проверяет корректность введенного номера/почты;
        b) Отправляет код на введенный номер телефон/почту;
       4. Отображает форму ввода кода подтверждения, содержащую:
        a) Номер телефона/Почту на который был отправлен код;
        b) Ссылку "Изменить номер", если пользователь ввел телефон на 2 шаге или ссылку "Изменить почту", если
           пользователь ввел почту на шаге 2 (ссылка ведет на форму ввода номера телефона/почты);
        c) Шесть отдельных полей для ввода кода подтверждения;
        d) Текст с обратным отсчётом времени до повторной попытки отправки код, по завершении отсчёта отображается
           ссылка "Получить новый код";
       5. Клиент начинает вводить полученный код;
       6. Система:
        a) После ввода каждой цифры переводит фокус ввода в следующее поле;
        b) При событии заполнения всех 6 полей производит верификацию кода;
        c) При успешной верификации кода система переходит к следующему шагу, иначе клиенту отображается ошибка,
           сценарий останавливается.
       7. Система:
        a) Выполняет поиск УЗ по введенному номеру телефона/почте:
         i. Если УЗ с таким телефоном/почтой не найдена, то создает новую без пароля, ФИО, Региона после чего переход на
            шаг 8;
         ii. Если УЗ найдена – переход на шаг 8;
       8. Аутентифицирует клиента;
       9. Выполняет перенаправление клиента на страницу из redirect_uri;"""

    def test_auth_page(self):
        assert get_current_url(auth_page_title_locator).startswith(auth_url)

    class TestOtpFormsScenario:
        @pytest.mark.skip(reason="Нет временного кода valid_otp для теста")
        def test_otp_forms_phone_scenario_success(self):  # Телефон, верный код
            assert is_element_visible(otp_form_locator) is True  # Форма «Авторизация по коду»
            assert is_element_visible(otp_form_title_locator) is True
            assert find_element_and_get_text(otp_form_title_locator) == otp_form_title

            assert is_element_visible(otp_form_description_locator) is True  # Подсказка по работе с формой “Укажите
            # контактный номер телефона или почту, на которые необходимо отправить код подтверждения”
            assert find_element_and_get_text(otp_form_description_locator) == otp_form_description

            assert is_element_visible(input_form_email_or_phone_locator) is True  # Поле ввода номера телефона или почты
            assert find_element_and_get_text(input_form_email_or_phone_placeholder_locator) == \
                   input_form_email_or_phone_placeholder

            assert is_element_visible(button_get_code_locator) is True  # Кнопка "Получить код"
            assert find_element_and_get_text(button_get_code_locator) == button_get_code_text

            find_element_and_send_keys(input_form_email_or_phone_locator, valid_phone)  # Клиент вводит номер телефона
            find_element_and_click(otp_form_locator)
            assert is_element_visible(input_form_email_or_phone_error_text_locator, 1) is False
            assert find_element_and_get_attribute(input_form_email_or_phone_value_locator, value_attribute) ==\
                   valid_phone or find_element_and_get_attribute(input_form_email_or_phone_value_locator,
                                                                 value_attribute) == valid_phone_form
            try:
                assert is_element_visible(otp_form_timeout_text_locator, timeout=1) is False
            except Exception:
                assert is_element_visible(otp_form_timeout_text_locator, timeout=1, sleep=resend_code_timeout) is \
                       False

            find_element_and_click(button_get_code_locator)  # Клиент нажимает кнопку "Получить код"
            assert is_element_visible(otp_code_form_locator) is True  # Отображает форму ввода кода подтверждения
            assert is_element_visible(otp_code_form_title_locator) is True
            assert find_element_and_get_text(otp_code_form_title_locator) == otp_code_form_title

            assert valid_phone in find_element_and_get_text(otp_code_form_description_locator)\
                   or valid_phone_form in find_element_and_get_text(otp_code_form_description_locator)  # Номер
            # телефона на который был отправлен код

            assert is_element_visible(button_otp_back_phone_locator)  # Ссылка "Изменить номер"
            assert find_element_and_get_text(button_otp_back_phone_locator) == button_otp_back_phone_text

            assert is_all_elements_visible(input_code_all_locator)  # Шесть отдельных полей для ввода кода подтверждения
            assert len(find_elements(input_code_all_locator)) == count_code_input

            assert is_element_visible(otp_resend_code_timeout_text_locator)  # Текст с обратным отсчётом времени до
            # повторной попытки отправки код, по завершении отсчёта отображается ссылка "Получить новый код"
            assert is_element_visible(button_otp_resend_code_locator, sleep=resend_code_timeout) is True

            elements = find_elements(input_code_all_locator)  # Клиент начинает вводить полученный код
            parent_elements = find_elements(input_code_parent_all_locator)

            i = 0
            while i < count_code_input:
                for element in elements:
                    assert parent_elements[i] == find_element(input_code_parent_active_locator)
                    element.send_keys(valid_otp[i])
                    i += 1

            assert get_current_url(start_page_title_locator).startswith(start_url)  # Выполняет перенаправление клиента
            # на страницу из redirect_uri

            find_element_and_click(menu_start_page_account_locator)  # Возврат на страницу авторизации по коду
            find_element_and_click(button_start_page_logout_locator)
            assert get_current_url(auth_page_title_locator).startswith(auth_url)

        @pytest.mark.skip(reason="Нет временного кода valid_otp для теста")
        def test_otp_forms_mail_scenario_success(self):  # Почта, верный код
            assert is_element_visible(otp_form_locator) is True  # Форма «Авторизация по коду»
            assert is_element_visible(otp_form_title_locator) is True
            assert find_element_and_get_text(otp_form_title_locator) == otp_form_title

            assert is_element_visible(otp_form_description_locator) is True  # Подсказка по работе с формой “Укажите
            # контактный номер телефона или почту, на которые необходимо отправить код подтверждения”
            assert find_element_and_get_text(otp_form_description_locator) == otp_form_description

            assert is_element_visible(input_form_email_or_phone_locator) is True  # Поле ввода номера телефона или почты
            assert find_element_and_get_text(input_form_email_or_phone_placeholder_locator) == \
                   input_form_email_or_phone_placeholder

            assert is_element_visible(button_get_code_locator) is True  # Кнопка "Получить код"
            assert find_element_and_get_text(button_get_code_locator) == button_get_code_text

            find_element_and_send_keys(input_form_email_or_phone_locator, valid_mail)  # Клиент вводит адрес почты
            find_element_and_click(otp_form_locator)
            assert is_element_visible(input_form_email_or_phone_error_text_locator, 1) is False
            assert find_element_and_get_attribute(input_form_email_or_phone_value_locator, value_attribute) ==\
                   valid_mail
            try:
                assert is_element_visible(otp_form_timeout_text_locator, timeout=1) is False
            except Exception:
                assert is_element_visible(otp_form_timeout_text_locator, timeout=1, sleep=resend_code_timeout) is\
                       False

            find_element_and_click(button_get_code_locator)  # Клиент нажимает кнопку "Получить код"
            assert is_element_visible(otp_code_form_locator) is True  # Отображает форму ввода кода подтверждения
            assert is_element_visible(otp_code_form_title_locator) is True
            assert find_element_and_get_text(otp_code_form_title_locator) == otp_code_form_title

            assert valid_mail in find_element_and_get_text(otp_code_form_description_locator)  # Адрес почты на
            # который был отправлен код

            assert is_element_visible(button_otp_back_phone_locator)  # Ссылка "Изменить номер"
            assert find_element_and_get_text(button_otp_back_phone_locator) == button_otp_back_mail_text

            assert is_all_elements_visible(input_code_all_locator)  # Шесть отдельных полей для ввода кода подтверждения
            assert len(find_elements(input_code_all_locator)) == count_code_input

            assert is_element_visible(otp_resend_code_timeout_text_locator) is True  # Текст с обратным отсчётом времени
            # до повторной попытки отправки код, по завершении отсчёта отображается ссылка "Получить новый код"
            assert resend_code_timeout_text in find_element_and_get_text(otp_resend_code_timeout_text_locator)
            assert is_element_visible(button_otp_resend_code_locator, sleep=resend_code_timeout) is True

            elements = find_elements(input_code_all_locator)  # Клиент начинает вводить полученный код
            parent_elements = find_elements(input_code_parent_all_locator)

            i = 0
            while i < count_code_input:
                for element in elements:
                    assert parent_elements[i] == find_element(input_code_parent_active_locator)
                    element.send_keys(valid_otp[i])
                    i += 1

            assert get_current_url(start_page_title_locator).startswith(start_url)  # Выполняет перенаправление клиента
            # на страницу из redirect_uri

            find_element_and_click(menu_start_page_account_locator)  # Возврат на страницу авторизации по коду
            find_element_and_click(button_start_page_logout_locator)
            assert get_current_url(auth_page_title_locator).startswith(auth_url)

        def test_otp_forms_phone_scenario_failure_invalid_otp(self):  # Телефон, неверный код
            assert is_element_visible(otp_form_locator) is True  # Форма «Авторизация по коду»
            assert is_element_visible(otp_form_title_locator) is True
            assert find_element_and_get_text(otp_form_title_locator) == otp_form_title

            assert is_element_visible(otp_form_description_locator) is True  # Подсказка по работе с формой “Укажите
            # контактный номер телефона или почту, на которые необходимо отправить код подтверждения”
            assert find_element_and_get_text(otp_form_description_locator) == otp_form_description

            assert is_element_visible(input_form_email_or_phone_locator) is True  # Поле ввода номера телефона или почты
            assert find_element_and_get_text(input_form_email_or_phone_placeholder_locator) == \
                   input_form_email_or_phone_placeholder

            assert is_element_visible(button_get_code_locator) is True  # Кнопка "Получить код"
            assert find_element_and_get_text(button_get_code_locator) == button_get_code_text

            find_element_and_send_keys(input_form_email_or_phone_locator, valid_phone)  # Клиент вводит номер телефона
            find_element_and_click(otp_form_locator)
            assert is_element_visible(input_form_email_or_phone_error_text_locator, 1) is False
            assert find_element_and_get_attribute(input_form_email_or_phone_value_locator, value_attribute) ==\
                   valid_phone or find_element_and_get_attribute(input_form_email_or_phone_value_locator,
                                                                 value_attribute) == valid_phone_form
            try:
                assert is_element_visible(otp_form_timeout_text_locator, timeout=1) is False
            except Exception:
                assert is_element_visible(otp_form_timeout_text_locator, timeout=1, sleep=resend_code_timeout) is \
                       False

            find_element_and_click(button_get_code_locator)  # Клиент нажимает кнопку "Получить код"
            assert is_element_visible(otp_code_form_locator) is True  # Отображает форму ввода кода подтверждения
            assert is_element_visible(otp_code_form_title_locator) is True
            assert find_element_and_get_text(otp_code_form_title_locator) == otp_code_form_title

            assert valid_phone in find_element_and_get_text(otp_code_form_description_locator)\
                   or valid_phone_form in find_element_and_get_text(otp_code_form_description_locator)  # Номер
            # телефона на который был отправлен код

            assert is_element_visible(button_otp_back_phone_locator)  # Ссылка "Изменить номер"
            assert find_element_and_get_text(button_otp_back_phone_locator) == button_otp_back_phone_text

            assert is_all_elements_visible(input_code_all_locator)  # Шесть отдельных полей для ввода кода подтверждения
            assert len(find_elements(input_code_all_locator)) == count_code_input

            assert is_element_visible(otp_resend_code_timeout_text_locator)  # Текст с обратным отсчётом времени до
            # повторной попытки отправки код, по завершении отсчёта отображается ссылка "Получить новый код"
            assert is_element_visible(button_otp_resend_code_locator, sleep=resend_code_timeout) is True

            elements = find_elements(input_code_all_locator)  # Клиент начинает вводить полученный код
            parent_elements = find_elements(input_code_parent_all_locator)

            i = 0
            while i < count_code_input:
                for element in elements:
                    assert parent_elements[i] == find_element(input_code_parent_active_locator)
                    element.send_keys(invalid_otp[i])
                    i += 1

            assert is_element_visible(otp_code_error_locator) is True  # Клиенту отображается ошибка, сценарий
            # останавливается
            assert find_element_and_get_text(otp_code_error_locator) == code_error_invalid_text

            find_element_and_click(button_otp_back_phone_locator)  # Возврат на страницу авторизации по коду
            assert is_element_visible(otp_form_locator) is True

        def test_otp_forms_mail_scenario_failure_invalid_otp(self):  # Почта, неверный код
            assert is_element_visible(otp_form_locator) is True  # Форма «Авторизация по коду»
            assert is_element_visible(otp_form_title_locator) is True
            assert find_element_and_get_text(otp_form_title_locator) == otp_form_title

            assert is_element_visible(otp_form_description_locator) is True  # Подсказка по работе с формой “Укажите
            # контактный номер телефона или почту, на которые необходимо отправить код подтверждения”
            assert find_element_and_get_text(otp_form_description_locator) == otp_form_description

            assert is_element_visible(input_form_email_or_phone_locator) is True  # Поле ввода номера телефона или почты
            assert find_element_and_get_text(input_form_email_or_phone_placeholder_locator) == \
                   input_form_email_or_phone_placeholder

            assert is_element_visible(button_get_code_locator) is True  # Кнопка "Получить код"
            assert find_element_and_get_text(button_get_code_locator) == button_get_code_text

            find_element_and_send_keys(input_form_email_or_phone_locator, valid_mail)  # Клиент вводит адрес почты
            find_element_and_click(otp_form_locator)
            assert is_element_visible(input_form_email_or_phone_error_text_locator, 1) is False
            assert find_element_and_get_attribute(input_form_email_or_phone_value_locator, value_attribute) ==\
                   valid_mail
            try:
                assert is_element_visible(otp_form_timeout_text_locator, timeout=1) is False
            except Exception:
                assert is_element_visible(otp_form_timeout_text_locator, timeout=1, sleep=resend_code_timeout) is \
                       False

            find_element_and_click(button_get_code_locator)  # Клиент нажимает кнопку "Получить код"
            assert is_element_visible(otp_code_form_locator) is True  # Отображает форму ввода кода подтверждения
            assert is_element_visible(otp_code_form_title_locator) is True
            assert find_element_and_get_text(otp_code_form_title_locator) == otp_code_form_title

            assert valid_mail in find_element_and_get_text(otp_code_form_description_locator)  # Адрес почты на
            # который был отправлен код

            assert is_element_visible(button_otp_back_phone_locator)  # Ссылка "Изменить номер"
            assert find_element_and_get_text(button_otp_back_phone_locator) == button_otp_back_mail_text

            assert is_all_elements_visible(input_code_all_locator)  # Шесть отдельных полей для ввода кода подтверждения
            assert len(find_elements(input_code_all_locator)) == count_code_input

            assert is_element_visible(otp_resend_code_timeout_text_locator)  # Текст с обратным отсчётом времени до
            # повторной попытки отправки код, по завершении отсчёта отображается ссылка "Получить новый код"
            assert is_element_visible(button_otp_resend_code_locator, sleep=resend_code_timeout) is True

            elements = find_elements(input_code_all_locator)  # Клиент начинает вводить полученный код
            parent_elements = find_elements(input_code_parent_all_locator)

            i = 0
            while i < count_code_input:
                for element in elements:
                    assert parent_elements[i] == find_element(input_code_parent_active_locator)
                    element.send_keys(invalid_otp[i])
                    i += 1

            assert is_element_visible(otp_code_error_locator) is True  # Клиенту отображается ошибка, сценарий
            # останавливается
            assert find_element_and_get_text(otp_code_error_locator) == code_error_invalid_text

            find_element_and_click(button_otp_back_phone_locator)  # Возврат на страницу авторизации по коду
            assert is_element_visible(otp_form_locator) is True
