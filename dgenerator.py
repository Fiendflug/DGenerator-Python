#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" DGenerator cli process """

import cmd, cdr, period, sys

class Cli(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = 'DGenerator(%s %s)>>> ' % tuple(per.get_period())
        self.intro = 'Вас приветствует DGenerator. Для получения справки введите ? или воспользуйтесь командой help'
        self.doc_header = 'Доступные команды (для справки по конкретной команде наберите "help <Команда>")'

    def default(self, line):
        print('Некорректная команда. Воспользутесь командой help или ? для получения помощи.')

    def emptyline(self):
        pass

    def change_promt(self, new_promt):
        self.prompt = new_promt

    # Show command methods section

    def do_show_list_clients(self, args):
        """Отображает список активных клиентов. Данная команда не предусматривает использования параметров."""

        if not args:
            for i in range(1, 2500):
                print('Пользователь с ID - {0}'.format(i))
        else:
            print('Некорректные параметры. Воспользутесь командой help show_list_clients для получения помощи.')

    def do_show_all_clients_stat(self, args):
        """Отображает сводную статистику по клиентам за отчетный период. Данная команда не предусматривает
        использования параметров."""

        if not args:
            print('Статистика по всем клиентам')
        else:
            print('Некорректные параметры. Воспользутесь командой help show_all_clients_stat для получения помощи.')

    def do_show_client_stat(self, args):
        """Отображает сводную статистику о конкретном клиенте. В качестве параметра допускается передавать
        ID Аккаунта, Абонентский номер (номер телефона) или фамилию имя отчество в формате <ID Аккаунта> или 
        <Номер телефона> или <Фамилия Имя Отчество>. Комбинирование и отсутсвие параметров не допускается. 
        Например, команда show_client_stat 3354 отобразит статистику для клиента с ID аккаунта 3354, 
        команда show_client_stat 58104 отобразит статистику для клиента с абонентским номером 496-455-81-04, а команда 
        show_client_stat Иванов Петр Сидорович отобразит статистику для клиента с указанным ФИО."""

        arguments = [a if not a.isdigit() else int(a) for a in args.split()]

        if len(arguments) == 1 and arguments[0] in range(1, 9999):
            print('Параметр ID аккаунта - {0}'.format(arguments))
        elif len(arguments) == 1 and arguments[0] in range(58000, 92999):
            print('Параметр Номер телефона - {0}'.format(arguments))
        elif len(arguments) == 3 and arguments[0].isalpha() and arguments[1].isalpha() and arguments[2].isalpha():
            print('Параметр ФИО, где Ф - {0} И - {1} О - {2}'.format(arguments[0], arguments[1], arguments[2]))
        else:
            print('Некорректные параметры. Воспользутесь командой help show_client_stat для получения помощи.')

    def do_show_trunks_stat(self, args):
        """Отображает сводную статистику по транкам присоединяющих операторов. Данная команда не предусматривает
        использования параметров."""

        if not args:
            print('Статистика по тарнкам')
        else:
            print('Некорректные параметры. Воспользутесь командой help show_trunks_stat для получения помощи.')

    def do_show_period(self, args):
        """Отображает выбранный расчетный период в формате <Месяц Год>. Данная команда не предусматривает
        использования параметров."""

        if not args:
            print('Текущий отчетный период - %s %s' % tuple(per.get_period()))
        else:
            print('Некорректные параметры. Воспользутесь командой help show_period для получения помощи.')

    def do_show_config(self, args):
        """Отображает текущую конфигурацию сеанса. Данная команда не предусматривает использования параметров."""

        if not args:
            print('Текущая конфигурация')
        else:
            print('Некорректные параметры. Воспользутесь командой help show_config для получения помощи.')

    def do_show_log(self, args):
        """Отображает последние записи журнала. Данная команда не предусматривает использования параметров."""

        if not args:
            print('Записи лог-файла')
        else:
            print('Некорректные параметры. Воспользутесь командой help show_log для получения помощи.')

    # Generate docs command methods section

    def do_generate_all_bills(self, args):
        """Позволяет запустить процесс генерирования телефонных счетов для всех клиентов физических лиц. 
        Обязательно обращайте внимание на отчетный период (команда show_period). Директорию, в которой хранятся файлы
        счетов можно узнать в соотвествующей секции конфигурации (которую можно просмотреть командой show_config).
        Данная команда не предусматривает использования параметров."""

        if not args:
            print('Генерируем квитанции клиентам физическим лицам')
        else:
            print('Некорректные параметры. Воспользутесь командой help generate_all_bills для получения помощи.')

    def do_generate_all_details(self, args):

        """Позволяет запустить процесс генерирования детализаций для всех клиентов (физических и юридических лиц)
        Обязательно обращайте внимание на отчетный период (команда show_period). Директорию, в которой хранятся файлы
        счетов можно узнать в соотвествующей секции конфигурации (которую можно просмотреть командой show_config).
        Данная команда не предусматривает использования параметров."""

        if not args:
            print('Генерируем детализации всем клиентам')
        else:
            print('Некорректные параметры. Воспользутесь командой help generate_all_details для получения помощи.')

    def do_generate_client_bill(self, args):
        """Позволяет запустить процесс генерирования телефонного счета указанному в качестве параметра клиенту.
        В качестве параметра допускается передавать ID Аккаунта, Абонентский номер (номер телефона) 
        или фамилию имя отчество в формате <ID Аккаунта> или <Номер телефона> или <Фамилия Имя Отчество>. 
        Комбинирование и отсутсвие параметров не допускается. Например, команда generate_client_bill 3354 запустит 
        процесс генерирования счета для клиента с ID аккаунта 3354, команда generate_client_bill 58104 сгенерирует
        счет для клиента с абонентским номером 496-455-81-04, а команда generate_client_bill Иванов Петр Сидорович 
        счет для клиента с указанным ФИО. Обязательно обращайте внимание на отчетный период (команда show_period). 
        Директорию, в которой хранятся файлы счетов можно узнать в соотвествующей секции конфигурации
        (которую можно просмотреть командой show_config)."""

        arguments = [a if not a.isdigit() else int(a) for a in args.split()]

        if len(arguments) == 1 and arguments[0] in range(1, 9999):
            print('Параметр ID аккаунта - {0}'.format(arguments))
        elif len(arguments) == 1 and arguments[0] in range(58000, 92999):
            print('Параметр Номер телефона - {0}'.format(arguments))
        elif len(arguments) == 3 and arguments[0].isalpha() and arguments[1].isalpha() and arguments[2].isalpha():
            print('Параметр ФИО, где Ф - {0} И - {1} О - {2}'.format(arguments[0], arguments[1], arguments[2]))
        else:
            print('Некорректные параметры. Воспользутесь командой help generate_client_bill для получения помощи.')

    def do_generate_client_detail(self, args):
        """Позволяет запустить процесс генерирования детализации телефонных соединений указанному в качестве параметра
        клиенту. В качестве параметра допускается передавать ID Аккаунта, Абонентский номер (номер телефона) 
        или фамилию имя отчество в формате <ID Аккаунта> или <Номер телефона> или <Фамилия Имя Отчество>. 
        Комбинирование и отсутсвие параметров не допускается. Например, команда generate_client_detail 3354 запустит 
        процесс генерирования счета для клиента с ID аккаунта 3354, команда generate_client_detail 58104 сгенерирует
        счет для клиента с абонентским номером 496-455-81-04, а команда generate_client_detail Иванов Петр Сидорович 
        счет для клиента с указанным ФИО. Обязательно обращайте внимание на отчетный период (команда show_period). 
        Директорию, в которой хранятся файлы счетов можно узнать в соотвествующей секции конфигурации
        (которую можно просмотреть командой show_config)."""

        arguments = [a if not a.isdigit() else int(a) for a in args.split()]

        if len(arguments) == 1 and arguments[0] in range(1, 9999):
            print('Параметр ID аккаунта - {0}'.format(arguments))
        elif len(arguments) == 1 and arguments[0] in range(58000, 92999):
            print('Параметр Номер телефона - {0}'.format(arguments))
        elif len(arguments) == 3 and arguments[0].isalpha() and arguments[1].isalpha() and arguments[2].isalpha():
            print('Параметр ФИО, где Ф - {0} И - {1} О - {2}'.format(arguments[0], arguments[1], arguments[2]))
        else:
            print('Некорректные параметры. Воспользутесь командой help generate_client_detail для получения помощи.')

    def do_generate_reports(self, args):
        """Позвлояет запустить процесс генерирования отчетных документов для финансового отдела. Данная команда
        не предусматривает использования параметров. Директорию, в которой хранятся файлы отчетов можно узнать в
        соотвествующей секции конфигурации (которую можно просмотреть командой show_config)."""

        if not args:
            print('Генерируем финансовую отчетность')
        else:
            print('Некорректные параметры. Воспользутесь командой help generate_reports для получения помощи.')

    def do_generate_cdr(self, args):
        """Позволяет запустить процесс преобразования CDR записей о вызовах в формат UTM5 и следом запустить процесс
        передачи конвертированных файлов парсеру UTM5. Данная команда не предусматривает использования параметров."""

        if not args:
            c = cdr.Cdr(per.get_period())
            c.run_generate()
        else:
            print('Некорректные параметры. Воспользутесь командой help generate_cdr для получения помощи.')

    # Set command methods section

    def do_set_period(self, args):
        """Позволяет установить отчетный период. В качестве параметра допускается передавать месяц и год 
        в формате <Месяц Год>. Отсуствие параметров не допускается Например, команда set_period 7 2017 установит в
        качестве отчетного периода текущего сеанса отрезок времени от 
        01.07.2017 0:00 до 30.07.2017 23:59 включительно."""

        arguments = [int(a) for a in args.split() if a.isdigit()]

        if len(arguments) == 2 and arguments[0] in range(1, 13) and arguments[1] in range(2010, 2100):
            per.set_period(arguments)
            cli.change_promt('DGenerator (%s %s)>>> ' % tuple(per.get_period()))
        else:
            print('Некорректные параметры. Воспользутесь командой help set_period для получения помощи.')

    def do_test(self, args):
        print(per.get_period())

    # Common command methods section

    def do_exit(self, arg):
        """Обеспечивает выход из приложения."""
        print('Завершение сеанса. До скорой встречи.')
        return True


# Dgenerator's CLI loop

if __name__ == "__main__":
    per = period.Period()
    cli = Cli()
    try:
        cli.cmdloop()
    except KeyboardInterrupt:
        print('Завершение сеанса. До скорой встречи.')
