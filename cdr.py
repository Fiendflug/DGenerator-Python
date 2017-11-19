# -*- coding: utf-8 -*-

""" CDR converting to UTM5 format and parse in UTM5 """

import configparser, subprocess, logging
from os import path, listdir, makedirs
from sys import stdout as cmd_output

class Cdr:
    _app_dir = path.dirname(path.realpath(__file__))
    _config = configparser.ConfigParser()
    _period = None
    _cdr_upload_dir = None
    _cdr_converted_dir = None
    _parser = None
    _parser_config = None

    def __init__(self, period):
        self._config.read(self._app_dir + '/config/dgenerator.conf')
        self._period = '%s_%s' % tuple(period)
        self._cdr_upload_dir = path.join(path.normpath(self._config.get('CDR', 'SourceRootCdrDir')), self._period)
        self._cdr_converted_dir = path.join(path.normpath(self._config.get('CDR', 'ConvertedRootCdrDir')), self._period)
        self._parser = self._config.get('CDR', 'ParserPath')
        self._parser_config = self._config.get('CDR', 'ParserConfigPath')

    def _convert(self):
        # Convert CDR files in UTM5 format

        if path.isdir(self._cdr_upload_dir) and len(listdir(self._cdr_upload_dir)) != 0:
            if not path.isdir(self._cdr_converted_dir):
                makedirs(self._cdr_converted_dir)
            cdr_count = 1
            for cdr in listdir(self._cdr_upload_dir):
                converted_cdr_name = cdr.replace('.log', '.cdr')
                converted_cdr_lines = []
                line_count = 0
                for line in open(path.join(self._cdr_upload_dir, cdr)):
                    temp = line.split()
                    converted_cdr_lines.append(
                        '%s;%s;%s;%s;%s %s;%s;%s;1\n' %
                        (temp[1],temp[3],temp[6],str(line_count),temp[4],temp[5],temp[0][1:],temp[2]))
                    line_count += 1
                converted_cdr_file = open(path.join(self._cdr_converted_dir, converted_cdr_name), 'w+')
                converted_cdr_file.writelines(converted_cdr_lines)
                cmd_output.write('INFO: Файл %s из %s (%s) успешно сконвертирован\n' %
                                 (cdr_count, len(listdir(self._cdr_upload_dir)), cdr))
                cdr_count += 1
            cmd_output.write('COMPLETE: Все CDR файлы успешно сконвертированы.\n')
            return 0
        else:
            cmd_output.write('ERROR: Не обнаружен каталог с CDR файлами, которые необходимо обработать\n')
            return 1


    def run_generate(self):
        # Start parse converted CDR files via utm5_send_cdr
        count = 1
        if self._convert() == 0:
            for cdr in listdir(self._cdr_converted_dir):
                try:
                    subprocess.check_output(['ping','www.google.ru'], shell=True)
                except subprocess.CalledProcessError as exc:
                    cmd_output.write('ERROR: Произошла ошибка парсинга. Опреация прервана.\n')
                    return
                cmd_output.write('INFO:  Файл %s успешно пропарсился\n' % (str(count)))
                count += 1
            cmd_output.write('COMPLETE: Все CDR файлы успешно пропарсились.\n')

