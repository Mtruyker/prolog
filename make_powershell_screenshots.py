# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import os

OUTPUT_DIR = r"C:\Users\Professional\.gemini\antigravity\brain\bafce425-ceac-4ae0-a60b-a2f4a35f17e7"
os.makedirs(OUTPUT_DIR, exist_ok=True)

BG = (1, 36, 86)
FG = (238, 238, 238)
PROMPT = (160, 220, 255)
INPUT = (255, 241, 138)
SUCCESS = (120, 255, 140)
WARN = (255, 220, 120)
BORDER = (35, 78, 135)
TITLE_BG = (0, 83, 156)
TITLE_FG = (255, 255, 255)

FONT_SIZE = 15
LINE_H = 21
TITLE_H = 34
PAD_X = 14
WIN_W = 900


def load_font(size):
    for path in (
        "C:/Windows/Fonts/consola.ttf",
        "C:/Windows/Fonts/cour.ttf",
        "C:/Windows/Fonts/lucon.ttf",
    ):
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def wrap_line(draw, text, font, max_width):
    words = text.split(" ")
    lines = []
    current = ""
    for word in words:
        candidate = word if not current else current + " " + word
        if draw.textlength(candidate, font=font) <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines or [""]


def screenshot(filename, lines, title="Windows PowerShell — SWI-Prolog", width=WIN_W, target_height=None):
    font = load_font(FONT_SIZE)
    tmp = Image.new("RGB", (width, 100), BG)
    tmp_draw = ImageDraw.Draw(tmp)
    rendered = []
    for text, color in lines:
        wrapped = wrap_line(tmp_draw, text, font, width - PAD_X * 2)
        for part in wrapped:
            rendered.append((part, color))

    height = TITLE_H + 12 + len(rendered) * LINE_H + 16
    if target_height:
        height = max(height, target_height)
    img = Image.new("RGB", (width, height), BG)
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, width - 1, height - 1], outline=BORDER, width=2)
    draw.rectangle([0, 0, width, TITLE_H], fill=TITLE_BG)
    draw.text((12, 8), title, font=load_font(FONT_SIZE - 1), fill=TITLE_FG)
    for i, sym in enumerate(["─", "□", "×"]):
        draw.text((width - 54 + i * 17, 8), sym, font=load_font(FONT_SIZE - 1), fill=TITLE_FG)

    y = TITLE_H + 8
    for text, color in rendered:
        draw.text((PAD_X, y), text, font=font, fill=color)
        y += LINE_H

    out = os.path.join(OUTPUT_DIR, filename)
    img.save(out)
    print(out)


ps = "PS C:\\Users\\Professional\\.gemini\\antigravity\\scratch\\prolog_expert_system>"
run = '& "C:\\Program Files\\swipl\\bin\\swipl.exe" -q -g start -t halt run_cli.pl'

screenshot("screenshot_1_start.png", [
    (ps + " " + run, PROMPT),
    ("=================================================================", FG),
    ("   ЭКСПЕРТНАЯ СИСТЕМА ПОДБОРА МЕСТА ПРОИЗВОДСТВЕННОЙ ПРАКТИКИ", SUCCESS),
    ("                   (Колледж / Техникум)", FG),
    ("=================================================================", FG),
    ("Ответьте на 11 вопросов экспертной системы. После каждого ответа ставьте точку.", FG),
    ("", FG),
    ("Доступные специальности для ввода:", FG),
    ("  is  - Информационные системы и программирование", INPUT),
    ("  set - Сетевое и системное администрирование", INPUT),
    ("  tm  - Технология машиностроения", INPUT),
    ("  buh - Экономика и бухгалтерский учет", INPUT),
    ("  tur - Туризм и гостеприимство", INPUT),
    ("", FG),
    ("Вопрос 1. Введите вашу специальность:", PROMPT),
], target_height=494)

screenshot("screenshot_2_input.png", [
    ("Вопрос 1. Введите вашу специальность: is.", PROMPT),
    ("Вопрос 2. Введите ваш средний балл (например, 4.2): 4.2.", PROMPT),
    ("Доступные города для ввода: moscow, spb, ekaterinburg, any", FG),
    ("Вопрос 3. Введите желаемый город: moscow.", PROMPT),
    ("Доступные форматы работы: office, remote, any", FG),
    ("Вопрос 4. Введите предпочтительный формат работы: any.", PROMPT),
    ("Доступные отрасли: it, industry, transport, finance, tourism, any", FG),
    ("Вопрос 5. Введите предпочтительную отрасль: it.", PROMPT),
    ("--- Профессиональные интересы ---", FG),
    ("Вопрос 6. Разработка программ, серверная логика или базы данных? yes.", PROMPT),
    ("Вопрос 7. Сайты, интерфейсы и дизайн экранов? no.", PROMPT),
    ("Вопрос 8. Сети, серверы Linux и администрирование? no.", PROMPT),
    ("Вопрос 9. Чертежи, станки с ЧПУ и техническое проектирование? no.", PROMPT),
    ("Вопрос 10. Бухгалтерские документы, Excel, финансы или право? no.", PROMPT),
    ("Вопрос 11. Общение с клиентами, сервис и английский язык? no.", PROMPT),
], target_height=454)

screenshot("screenshot_3_results_is.png", [
    ("Выполняется поиск подходящих мест практики...", FG),
    ("", FG),
    ("РЕЗУЛЬТАТЫ ПОДБОРА (отсортированы по соответствию):", SUCCESS),
    ("-----------------------------------------------------------------", FG),
    ("100% соответствия | Должность: Разработчик Python", SUCCESS),
    ('               | Компания:  ООО "ИТ-Комплекс" (moscow)', FG),
    ("               | Требования: Полное соответствие!", SUCCESS),
    ("-----------------------------------------------------------------", FG),
    ("62.666666666666664% соответствия | Должность: Frontend-разработчик", WARN),
    ('               | Компания:  ООО "СофтЛайнс" (remote)', FG),
    ("               | Недостающие навыки для изучения: [javascript,html,css,react]", WARN),
    ("-----------------------------------------------------------------", FG),
], target_height=434)

screenshot("screenshot_4_results_buh.png", [
    ("Вопрос 1. Введите вашу специальность: buh.", PROMPT),
    ("Вопрос 2. Введите ваш средний балл: 4.7.", PROMPT),
    ("Вопрос 3. Введите желаемый город: moscow.", PROMPT),
    ("Вопрос 4. Введите предпочтительный формат работы: office.", PROMPT),
    ("Вопрос 5. Введите предпочтительную отрасль: finance.", PROMPT),
    ("Вопрос 10. Бухгалтерские документы, Excel, финансы или право? yes.", PROMPT),
    ("", FG),
    ("РЕЗУЛЬТАТЫ ПОДБОРА (отсортированы по соответствию):", SUCCESS),
    ("-----------------------------------------------------------------", FG),
    ("92% соответствия | Должность: Младший аудитор", SUCCESS),
    ("               | Компания:  Центральный Банк РФ (moscow)", FG),
    ("               | Требования: Полное соответствие!", SUCCESS),
    ("-----------------------------------------------------------------", FG),
], target_height=474)

screenshot("screenshot_5_results_set.png", [
    ("Вопрос 1. Введите вашу специальность: set.", PROMPT),
    ("Вопрос 2. Введите ваш средний балл: 3.8.", PROMPT),
    ("Вопрос 3. Введите желаемый город: any.", PROMPT),
    ("Вопрос 4. Введите предпочтительный формат работы: office.", PROMPT),
    ("Вопрос 5. Введите предпочтительную отрасль: transport.", PROMPT),
    ("Вопрос 8. Сети, серверы Linux и администрирование? yes.", PROMPT),
    ("", FG),
    ("РЕЗУЛЬТАТЫ ПОДБОРА (отсортированы по соответствию):", SUCCESS),
    ("-----------------------------------------------------------------", FG),
    ("100% соответствия | Должность: Помощник системного администратора", SUCCESS),
    ('               | Компания:  АО "РЖД" (ekaterinburg)', FG),
    ("               | Требования: Полное соответствие!", SUCCESS),
    ("-----------------------------------------------------------------", FG),
], target_height=454)

screenshot("screenshot_6_not_found.png", [
    ("Вопрос 1. Введите вашу специальность: is.", PROMPT),
    ("Вопрос 2. Введите ваш средний балл: 3.0.", PROMPT),
    ("Вопрос 3. Введите желаемый город: moscow.", PROMPT),
    ("Вопрос 4. Введите предпочтительный формат работы: office.", PROMPT),
    ("Вопрос 5. Введите предпочтительную отрасль: it.", PROMPT),
    ("Вопрос 6. Разработка программ, серверная логика или базы данных? yes.", PROMPT),
    ("", FG),
    ("Выполняется поиск подходящих мест практики...", FG),
    ("", FG),
    ("К сожалению, подходящих мест практики не найдено.", WARN),
    ("Рекомендации для прохождения практики:", FG),
    ("1. Постарайтесь повысить средний балл успеваемости.", FG),
    ('2. Расширьте географию поиска (введите "any" в поле города).', FG),
    ("3. Изучите дополнительные навыки, востребованные работодателями.", FG),
], target_height=434)
