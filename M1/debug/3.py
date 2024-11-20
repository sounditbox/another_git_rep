import logging
import traceback
import sys

# Все сообщения об ошибках будут записываться в файл error.log.
logging.basicConfig(filename='error.log', encoding='utf-8', level=logging.ERROR)


def function_c():
    return 1 / 0  # Это вызовет ZeroDivisionError


def function_b():
    function_c()


def function_a():
    try:
        function_b()
    # Ловим исключение и формируем сообщение
    except ZeroDivisionError:
        exc_type, exc_value, exc_tb = sys.exc_info()
        full_tb = traceback.format_exception(exc_type, exc_value, exc_tb)
        logging.error("Произошло исключение:\n%s", ''.join(full_tb))


function_a()
