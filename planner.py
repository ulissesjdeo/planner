from os import system as command, name as OS 
from datetime import datetime
from math import ceil, floor
from config import *


def linify(content):
	start_middle = SEPARATOR_START + content
	spaces_to_add = 0
	len_separator = len(SEPARATOR)
	len_start_middle = len(start_middle)
	if len_start_middle < len_separator:
		spaces_to_add = len_separator - len_start_middle
	for space in range(spaces_to_add - 2): start_middle += ' '
	print(start_middle + SEPARATOR_END)


def days_between(initial_date, final_date): return abs((final_date - initial_date).days)


NOW = datetime.now()
ITA_EXAM = datetime(ITA_EXAM_YEAR, ITA_EXAM_MONTH, ITA_EXAM_DAY)
ITA_EXAM_DAYS_REMAINING = days_between(NOW, ITA_EXAM) - 1

PAGES_PER_DAY_MARTHA_REIS = ceil((PAGINAS_MARTHA_REIS - PAGINAS_FEITAS_MARTHA_REIS) / ITA_EXAM_DAYS_REMAINING)
PAGES_PER_DAY_TOPICOS_DE_FISICA = ceil((PAGINAS_TOPICOS_DE_FISICA - PAGINAS_FEITAS_TOPICOS_DE_FISICA) / ITA_EXAM_DAYS_REMAINING)
CLASSES_PER_DAY_LICOES_DE_MATEMATICA = ceil((AULAS_LICOES_DE_MATEMATICA - AULAS_FEITAS_LICOES_DE_MATEMATICA) / ITA_EXAM_DAYS_REMAINING)

DAYS_REMAINING_TO_EARLY_END = ITA_EXAM_DAYS_REMAINING - DAYS_BEFORE_EXAM_FOR_EARLY_STUDY_END
PAGES_PER_DAY_TO_EARLY_END_MARTHA_REIS = ceil((PAGINAS_MARTHA_REIS - PAGINAS_FEITAS_MARTHA_REIS) / DAYS_REMAINING_TO_EARLY_END)
PAGES_PER_DAY_TO_EARLY_END_TOPICOS_DE_FISICA = ceil((PAGINAS_TOPICOS_DE_FISICA - PAGINAS_FEITAS_TOPICOS_DE_FISICA) / DAYS_REMAINING_TO_EARLY_END)
CLASSES_PER_DAY_TO_EARLY_END_LICOES_DE_MATEMATICA = ceil((AULAS_LICOES_DE_MATEMATICA - AULAS_FEITAS_LICOES_DE_MATEMATICA) / DAYS_REMAINING_TO_EARLY_END)

command('cls' if OS == 'nt' else 'clear')

print(SEPARATOR)
linify(f'')
linify(f'{ITA_EXAM_DAYS_REMAINING} days to ITA exam ({floor(ITA_EXAM_DAYS_REMAINING / 7)} weeks or {floor(ITA_EXAM_DAYS_REMAINING / 30)} months)')
linify(f'')
print(SEPARATOR)
linify(f'')
linify(f'Lições de Matemática')
linify(f'')
linify(f'{AULAS_FEITAS_LICOES_DE_MATEMATICA} of {AULAS_LICOES_DE_MATEMATICA}, means {CLASSES_PER_DAY_LICOES_DE_MATEMATICA} classes per day')
linify(f'{CLASSES_PER_DAY_TO_EARLY_END_LICOES_DE_MATEMATICA} classes per day to end {DAYS_BEFORE_EXAM_FOR_EARLY_STUDY_END} days before exam')
linify(f'')
print(SEPARATOR)
linify(f'')
linify(f'Tópicos de Física')
linify(f'')
linify(f'{PAGINAS_FEITAS_TOPICOS_DE_FISICA} of {PAGINAS_TOPICOS_DE_FISICA}, means {PAGES_PER_DAY_TOPICOS_DE_FISICA} pages per day')
linify(f'{PAGES_PER_DAY_TO_EARLY_END_TOPICOS_DE_FISICA} pages per day to end {DAYS_BEFORE_EXAM_FOR_EARLY_STUDY_END} days before exam')
linify(f'')
print(SEPARATOR)
linify(f'')
linify(f'Martha Reis')
linify(f'')
linify(f'{PAGINAS_FEITAS_MARTHA_REIS} of {PAGINAS_MARTHA_REIS}, means {PAGES_PER_DAY_MARTHA_REIS} pages per day')
linify(f'{PAGES_PER_DAY_TO_EARLY_END_MARTHA_REIS} pages per day to end {DAYS_BEFORE_EXAM_FOR_EARLY_STUDY_END} days before exam')
linify(f'')
print(SEPARATOR)
print()
