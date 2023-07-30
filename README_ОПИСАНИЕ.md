# 28.1.-Rostelecom

SkillFactory. 

Задание 28.1. 

Требования: https://lms.skillfactory.ru/assets/courseware/v1/010c9924044551b87b76b5c3c624bd2a/asset-v1:Skillfactory+QAP+18JUNE2020+type@asset+block/%D0%A2%D1%80%D0%B5%D0%B1%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F_SSO_%D0%B4%D0%BB%D1%8F_%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F_last.doc

Список файлов проекта:
- директория docs:
- - test_cases.txt - тест-кейсы
- - bug_reports - баг-репорты
- директория tests:
- - test_login_form.py - автотесты для авторизации по логину и паролю
- - test_otp_forms.py - автотесты для авторизации по временному коду
- - test_reset_forms.py - автотесты для восстановления пароля
- - test_register_form.py - автотесты для регистрации
- locators.py - локаторы элементов
- variables.py - переменные
- calculated_variables.py - вычисляемые переменные
- functions.py - функции
- conftest.py - фикстуры
- requirements.txt - список используемых библиотек



Для запуска тестов (в зависимости от тестируемой формы) используются команды:
pytest tests/test_login_form.py
pytest tests/test_otp_forms.py
pytest tests/test_reset_forms.py
pytest tests/test_register_form.py

Для запуска конкретного теста используется команда: pytest -k "{имя теста}"

Тесты:
- class TestLoginForm - Стандартная авторизация по логину и паролю:
- - class TestLoginFormElementsVisibility - Видимость элементов формы авторизации по логину и паролю
- - test_autochange_auth_type_tabs - Таб выбора аутентификации меняется автоматически при вводе номера телефона/почты/логина/лицевого счета    
- - class TestLoginFormElements - Тесты для элементов формы авторизации по логину и паролю:
  - - test_input_form_username_mail_failure - Негативный тест для поля ввода e-mail
- - class TestLoginFormPhonePasswordScenario - Сценарии:
  - - class TestLoginFormPhonePasswordScenario - Позитивный и негативный сценарии авторизации клиента по номеру телефона, кнопка "Телефон"
  - - class TestLoginFormMailPasswordScenario - Позитивный и негативный сценарии авторизации клиента по номеру телефона, кнопка "Почта"
  - - class TestLoginFormLoginPasswordScenario - Позитивный и негативный сценарии авторизации клиента по номеру телефона, кнопка "Логин"
  - - class TestLoginFormPersonalAccountPasswordScenario - Позитивный и негативный сценарии авторизации клиента по номеру телефона, кнопка "Лицевой счет"
- 
- class TestOtpForms - Авторизация по временному коду:
- - class TestOtpFormsScenario - Сценарии:
  - - test_otp_forms_phone_scenario_success - Позитивный, телефон, верный код (skip "Нет временного кода для теста")
  - - test_otp_forms_mail_scenario_success - Позитивный, почта, верный код (skip "Нет временного кода для теста")
  - - test_otp_forms_phone_scenario_failure_invalid_otp - Негативный, телефон, неверный код
  - - test_otp_forms_mail_scenario_failure_invalid_otp - Негативный, почта, неверный код
- 
- class TestResetForm - Восстановление пароля:
- - class TestResetFormElementsVisibility - Видимость элементов формы восстановления пароля
- - test_autochange_reset_type_tabs - Таб выбора восстановления пароля меняется автоматически при вводе номера телефона/почты/логина/лицевого счета
- - class TestResetFormsScenario - Сценарии:
  - - class TestResetFormsScenarioSuccess - Позитивные:
    - - test_reset_forms_phone_by_phone_scenario_success - Восстановление пароля клиента по номеру телефона, кнопка "По номеру телефона" (skip "Нет капчи valid_captcha и временного кода valid_otp для теста")
    - - test_reset_forms_phone_by_mail_scenario_success - Восстановление пароля клиента по номеру телефона, кнопка "По e-mail" (skip "Нет капчи valid_captcha и временного кода valid_otp для теста")
    - - test_reset_forms_scenario_success_back_to_login_form - Возврат на форму авторизации
  - - TestResetFormsScenarioFailure - Негативные:
    - - test_reset_forms_scenario_failure_invalid_captcha - Введена неверная капча
- 
- class TestResetChoiceForm - Форма выбора восстановления пароля (skip "Нет капчи valid_captcha"):
- - class TestResetChoiceFormScenarioSuccess - Позитивные сценарии:
  - - test_reset_choice_form_scenario_success_back_to_reset_form - Возврат на форму восстановления пароля
- class TestResetConfirmForm - Форма с полем для ввода кода (skip "Нет капчи valid_captcha"):
- - class TestResetConfirmFormScenarioSuccess - Позитивные сценарии:
  - - test_reset_confirm_form_scenario_success_back_to_reset_form - Возврат на форму восстановления пароля
- - class TestResetConfirmFormScenarioFailure - Негативные сценарии:
  - - test_reset_confirm_form_scenario_failure_invalid_code - Неверный код
  - - test_reset_confirm_form_scenario_failure_expired_code - Истекший код
- 
- class TestUpdatePasswordForm - Форма для ввода нового пароля (skip "Нет капчи valid_captcha и временного кода valid_otp для теста"):
- - class TestUpdatePasswordFormElements - Тесты для элементов формы для ввода нового пароля:
  - - test_input_form_new_password_success - Позитивный тест для поля вода нового пароля (используется техника граничных значений)
  - - test_input_form_password_confirm_success - Позитивный тест для поля вода подтверждения пароля (используется техника граничных значений)
  - - class TestInputFormNewPasswordFailure - Негативные тесты для поля вода нового пароля (используется техника граничных значений):
    - - test_input_form_new_password_failure_valid_chars_invalid_len - Допустимые символы, недопустимая длина
    - - test_input_form_new_password_failure_valid_len_no_uppercase_letters - Допустимая длина, без заглавных букв
    - - test_input_form_new_password_failure_valid_len_no_lowercase_letters - Допустимая длина, без строчных букв
    - - test_input_form_new_password_failure_valid_len_no_digits_or_special_chars - Допустимая длина, без цифр или спецсимволов
    - - test_input_form_new_password_failure_valid_len_not_only_latin_letters - Допустимая длина, не только латинские буквы
  - - class TestInputFormPasswordConfirmFailure - Негативные тесты для поля вода подтверждения пароля (используется техника граничных значений):
    - - test_input_form_password_confirm_failure_valid_chars_invalid_len - Допустимые символы, недопустимая длина
    - - test_input_form_password_confirm_failure_valid_len_no_uppercase_letters - Допустимая длина, без заглавных букв
    - - test_input_form_password_confirm_failure_valid_len_no_lowercase_letters - Допустимая длина, без строчных букв
    - - test_input_form_password_confirm_failure_valid_len_no_digits_or_special_chars - Допустимая длина, без цифр или спецсимволов
    - - test_input_form_password_confirm_failure_valid_len_not_only_latin_letters - Допустимая длина, не только латинские буквы
- - class TestUpdatePasswordFormScenario - Сценарии:
  - - test_update_password_scenario_failure_empty_input_forms - Негативный: пустые поля ввода
  - - test_update_password_scenario_failure_passwords_mismatch - Негативный: новый пароль и подтверждение пароля не совпадают
- 
- class TestRegisterForm - Форма регистрации:
- - class TestRegisterFormElements - Тесты для элементов формы регистрации:
  - - test_input_form_first_name_success - Позитивный тест для поля ввода имени (используется техника граничных значений) 
  - - test_input_form_last_name_success - Позитивный тест для поля ввода фамилии (используется техника граничных значений)
  - - class TestInputFormFirstNameFailure - Негативные тесты для поля ввода имени (используется техника граничных значений):
    - - test_input_form_first_name_failure_valid_chars_invalid_len - Допустимые символы, недопустимая длина
    - - test_input_form_first_name_failure_not_only_cyrillic_letters - Допустимая длина, не только буквы кириллицы
    - - test_input_form_first_name_failure_with_digits - Допустимая длина, c цифрами
    - - test_input_form_first_name_failure_with_other_special_chars - Допустимая длина, с недопустимыми спецсимволами
  - - class TestInputFormLastNameFailure - Негативные тесты для поля ввода фамилии (используется техника граничных значений):
    - - test_input_form_last_name_failure_valid_chars_invalid_len - Допустимые символы, недопустимая длина
    - - test_input_form_last_name_failure_not_only_cyrillic_letters - Допустимая длина, не только буквы кириллицы
    - - test_input_form_last_name_failure_with_digits - Допустимая длина, c цифрами
    - - test_input_form_last_name_failure_with_other_special_chars - Допустимая длина, с недопустимыми спецсимволами
- - class TestRegisterFormScenario - Сценарии:
  - - class TestRegisterFormScenarioSuccess - Позитивные:
    - - test_register_form_by_phone_scenario_success - По номеру телефона
    - - test_register_form_by_mail_scenario_success - По e-mail
