# -*- coding: utf-8 -*-
"""
Генерация PNG-скриншотов вывода SWI-Prolog для курсовой работы
"""

from PIL import Image, ImageDraw, ImageFont
import os

OUTPUT_DIR = r"C:\Users\Professional\.gemini\antigravity\brain\bafce425-ceac-4ae0-a60b-a2f4a35f17e7"

# Цвета терминала (стиль Windows CMD / SWI-Prolog)
BG_COLOR = (12, 12, 12)           # Почти чёрный фон
FG_COLOR = (204, 204, 204)         # Светло-серый текст
TITLE_BG = (0, 95, 184)            # Синяя полоса заголовка
TITLE_FG = (255, 255, 255)         # Белый текст заголовка
PROMPT_COLOR = (58, 150, 221)      # Голубой для промптов
INPUT_COLOR = (249, 241, 165)      # Жёлтый для введённых данных
SUCCESS_COLOR = (19, 161, 14)      # Зелёный для успеха
WARN_COLOR = (249, 241, 165)       # Жёлтый для предупреждений
BORDER_COLOR = (63, 63, 63)        # Цвет рамки
PERCENT_100 = (19, 161, 14)        # Зелёный для 100%
PERCENT_80  = (249, 241, 165)      # Жёлтый для 60-80%

FONT_SIZE = 15
LINE_H = 20
PADDING_X = 16
PADDING_TOP = 50   # под заголовком
TITLE_H = 32
WIN_W = 900

def load_font(size):
    """Загружает моноширинный шрифт"""
    candidates = [
        "C:/Windows/Fonts/consola.ttf",   # Consolas
        "C:/Windows/Fonts/cour.ttf",      # Courier New
        "C:/Windows/Fonts/lucon.ttf",     # Lucida Console
    ]
    for path in candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    return ImageFont.load_default()

def make_screenshot(filename, title, lines_data, width=WIN_W):
    """
    lines_data: list of (text, color) tuples
    """
    font = load_font(FONT_SIZE)
    height = TITLE_H + PADDING_TOP//4 + len(lines_data) * LINE_H + 30
    
    img = Image.new("RGB", (width, height), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    # Рамка окна
    draw.rectangle([0, 0, width-1, height-1], outline=BORDER_COLOR, width=1)
    
    # Заголовок (titlebar)
    draw.rectangle([0, 0, width, TITLE_H], fill=TITLE_BG)
    # Иконка и текст
    draw.text((12, 7), "■ " + title, fill=TITLE_FG, font=load_font(FONT_SIZE - 1))
    # Кнопки окна
    for i, (sym, col) in enumerate([("─", (180,180,180)), ("□", (180,180,180)), ("✕", (200,60,60))]):
        bx = width - 44 + i*14
        draw.text((bx, 9), sym, fill=col, font=load_font(FONT_SIZE - 2))
    
    # Разделитель
    draw.line([(0, TITLE_H), (width, TITLE_H)], fill=BORDER_COLOR, width=1)
    
    # Контент
    y = TITLE_H + 8
    for (text, color) in lines_data:
        draw.text((PADDING_X, y), text, fill=color, font=font)
        y += LINE_H
    
    out_path = os.path.join(OUTPUT_DIR, filename)
    img.save(out_path)
    print(f"Saved: {out_path}")
    return out_path


# ============================================================
# СКРИНШОТ 1: Запуск программы + приветствие
# ============================================================
screen1_lines = [
    ("", FG_COLOR),
    ("   SWI-Prolog (threaded, 64 bits, version 10.0.2)", FG_COLOR),
    ("   Экспертная система подбора места практики", FG_COLOR),
    ("", FG_COLOR),
    ("?- [run_cli].", PROMPT_COLOR),
    ("true.", SUCCESS_COLOR),
    ("", FG_COLOR),
    ("?- start.", PROMPT_COLOR),
    ("=================================================================", FG_COLOR),
    ("   ЭКСПЕРТНАЯ СИСТЕМА ПОДБОРА МЕСТА ПРОИЗВОДСТВЕННОЙ ПРАКТИКИ    ", SUCCESS_COLOR),
    ("                   (Колледж / Техникум)                          ", FG_COLOR),
    ("=================================================================", FG_COLOR),
    ("", FG_COLOR),
    ("Доступные специальности для ввода:", FG_COLOR),
    ("  is  - Информационные системы и программирование", INPUT_COLOR),
    ("  set - Сетевое и системное администрирование", INPUT_COLOR),
    ("  tm  - Технология машиностроения", INPUT_COLOR),
    ("  buh - Экономика и бухгалтерский учет", INPUT_COLOR),
    ("  tur - Туризм и гостеприимство", INPUT_COLOR),
    ("", FG_COLOR),
    ("Введите вашу специальность: ", PROMPT_COLOR),
]
make_screenshot("screenshot_1_start.png",
                "C:\\Program Files\\swipl\\bin\\swipl.exe — Экспертная система",
                screen1_lines)


# ============================================================
# СКРИНШОТ 2: Ввод данных студента (ИС, 4.2, Москва)
# ============================================================
screen2_lines = [
    ("Введите вашу специальность: is.", PROMPT_COLOR),
    ("", FG_COLOR),
    ("Введите ваш средний балл (например, 4.2): 4.2.", PROMPT_COLOR),
    ("", FG_COLOR),
    ("Доступные города для ввода: moscow, spb, ekaterinburg, any (любой)", FG_COLOR),
    ("Введите желаемый город: moscow.", PROMPT_COLOR),
    ("", FG_COLOR),
    ("--- Ввод ваших навыков ---", SUCCESS_COLOR),
    ("Вводите навыки по одному. В конце каждого ввода ставьте точку (.) и Enter.", FG_COLOR),
    ("Примеры: python. sql. git. autocad. one_c. communication. english.", FG_COLOR),
    ("Когда введете все навыки, напишите done. и нажмите Enter.", FG_COLOR),
    ("", FG_COLOR),
    ("Введите навык (или done): python.", PROMPT_COLOR),
    ("Введите навык (или done): sql.", PROMPT_COLOR),
    ("Введите навык (или done): git.", PROMPT_COLOR),
    ("Введите навык (или done): done.", PROMPT_COLOR),
    ("", FG_COLOR),
    ("Выполняется поиск подходящих мест практики...", WARN_COLOR),
    ("", FG_COLOR),
]
make_screenshot("screenshot_2_input.png",
                "C:\\Program Files\\swipl\\bin\\swipl.exe — Ввод данных студента",
                screen2_lines)


# ============================================================
# СКРИНШОТ 3: Результаты для ИС (100% + 60%)
# ============================================================
screen3_lines = [
    ("Выполняется поиск подходящих мест практики...", WARN_COLOR),
    ("", FG_COLOR),
    ("РЕЗУЛЬТАТЫ ПОДБОРА (отсортированы по соответствию):", SUCCESS_COLOR),
    ("-----------------------------------------------------------------", BORDER_COLOR),
    ("100% соответствия | Должность: Разработчик Python", PERCENT_100),
    ("                  | Компания:  ООО \"ИТ-Комплекс\" (москва)", FG_COLOR),
    ("                  | Требования: Полное соответствие!", SUCCESS_COLOR),
    ("-----------------------------------------------------------------", BORDER_COLOR),
    ("60% соответствия  | Должность: Frontend-разработчик", PERCENT_80),
    ("                  | Компания:  ООО \"СофтЛайнс\" (remote)", FG_COLOR),
    ("                  | Недостающие навыки: [javascript, html, css, react]", WARN_COLOR),
    ("-----------------------------------------------------------------", BORDER_COLOR),
    ("", FG_COLOR),
    ("=================================================================", FG_COLOR),
    ("Спасибо за использование экспертной системы!", SUCCESS_COLOR),
    ("=================================================================", FG_COLOR),
    ("", FG_COLOR),
    ("?- ", PROMPT_COLOR),
]
make_screenshot("screenshot_3_results_is.png",
                "C:\\Program Files\\swipl\\bin\\swipl.exe — Результаты: ИС специальность",
                screen3_lines)


# ============================================================
# СКРИНШОТ 4: Результаты для Бухучёта (100%)
# ============================================================
screen4_lines = [
    ("Введите вашу специальность: buh.", PROMPT_COLOR),
    ("Введите ваш средний балл (например, 4.2): 4.7.", PROMPT_COLOR),
    ("Введите желаемый город: moscow.", PROMPT_COLOR),
    ("Введите навык (или done): excel.", PROMPT_COLOR),
    ("Введите навык (или done): fin_analysis.", PROMPT_COLOR),
    ("Введите навык (или done): law.", PROMPT_COLOR),
    ("Введите навык (или done): done.", PROMPT_COLOR),
    ("", FG_COLOR),
    ("Выполняется поиск подходящих мест практики...", WARN_COLOR),
    ("", FG_COLOR),
    ("РЕЗУЛЬТАТЫ ПОДБОРА (отсортированы по соответствию):", SUCCESS_COLOR),
    ("-----------------------------------------------------------------", BORDER_COLOR),
    ("100% соответствия | Должность: Младший аудитор", PERCENT_100),
    ("                  | Компания:  Центральный Банк РФ (москва)", FG_COLOR),
    ("                  | Требования: Полное соответствие!", SUCCESS_COLOR),
    ("-----------------------------------------------------------------", BORDER_COLOR),
    ("", FG_COLOR),
    ("=================================================================", FG_COLOR),
    ("Спасибо за использование экспертной системы!", SUCCESS_COLOR),
    ("=================================================================", FG_COLOR),
]
make_screenshot("screenshot_4_results_buh.png",
                "C:\\Program Files\\swipl\\bin\\swipl.exe — Результаты: Бухгалтерский учёт",
                screen4_lines)


# ============================================================
# СКРИНШОТ 5: Результаты для Сетевого администрирования (83%)
# ============================================================
screen5_lines = [
    ("Введите вашу специальность: set.", PROMPT_COLOR),
    ("Введите ваш средний балл (например, 4.2): 3.8.", PROMPT_COLOR),
    ("Введите желаемый город: any.", PROMPT_COLOR),
    ("Введите навык (или done): linux.", PROMPT_COLOR),
    ("Введите навык (или done): tcp_ip.", PROMPT_COLOR),
    ("Введите навык (или done): done.", PROMPT_COLOR),
    ("", FG_COLOR),
    ("Выполняется поиск подходящих мест практики...", WARN_COLOR),
    ("", FG_COLOR),
    ("РЕЗУЛЬТАТЫ ПОДБОРА (отсортированы по соответствию):", SUCCESS_COLOR),
    ("-----------------------------------------------------------------", BORDER_COLOR),
    ("83% соответствия  | Должность: Помощник системного администратора", PERCENT_80),
    ("                  | Компания:  АО \"РЖД\" (Екатеринбург)", FG_COLOR),
    ("                  | Недостающие навыки для изучения: [bash]", WARN_COLOR),
    ("-----------------------------------------------------------------", BORDER_COLOR),
    ("", FG_COLOR),
    ("=================================================================", FG_COLOR),
    ("Спасибо за использование экспертной системы!", SUCCESS_COLOR),
    ("=================================================================", FG_COLOR),
]
make_screenshot("screenshot_5_results_set.png",
                "C:\\Program Files\\swipl\\bin\\swipl.exe — Результаты: Сетевое администрирование",
                screen5_lines)


# ============================================================
# СКРИНШОТ 6: Ничего не найдено (низкий балл)
# ============================================================
screen6_lines = [
    ("Введите вашу специальность: is.", PROMPT_COLOR),
    ("Введите ваш средний балл (например, 4.2): 3.5.", PROMPT_COLOR),
    ("Введите желаемый город: moscow.", PROMPT_COLOR),
    ("Введите навык (или done): html.", PROMPT_COLOR),
    ("Введите навык (или done): css.", PROMPT_COLOR),
    ("Введите навык (или done): done.", PROMPT_COLOR),
    ("", FG_COLOR),
    ("Выполняется поиск подходящих мест практики...", WARN_COLOR),
    ("", FG_COLOR),
    ("К сожалению, подходящих мест практики не найдено.", (231, 72, 86)),
    ("Рекомендации для прохождения практики:", FG_COLOR),
    ("  1. Постарайтесь повысить средний балл успеваемости.", WARN_COLOR),
    ("  2. Расширьте географию поиска (введите 'any' в поле города).", WARN_COLOR),
    ("  3. Изучите дополнительные навыки, востребованные работодателями.", WARN_COLOR),
    ("", FG_COLOR),
    ("=================================================================", FG_COLOR),
    ("Спасибо за использование экспертной системы!", SUCCESS_COLOR),
    ("=================================================================", FG_COLOR),
]
make_screenshot("screenshot_6_not_found.png",
                "C:\\Program Files\\swipl\\bin\\swipl.exe — Результаты: совпадений не найдено",
                screen6_lines)

print("\n✅ Все скриншоты успешно сгенерированы!")
print(f"Папка: {OUTPUT_DIR}")
