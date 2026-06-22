# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1800, 650
BG = (133, 133, 130)
BLACK = (0, 0, 0)
WHITE = (245, 245, 245)
LABEL = (250, 250, 250)
TEXT = (20, 20, 20)


def load_font(size, bold=False):
    paths = [
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/calibrib.ttf" if bold else "C:/Windows/Fonts/calibri.ttf",
    ]
    for path in paths:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

NODE_FONT = load_font(11, True)
LABEL_FONT = load_font(13)
SMALL_FONT = load_font(12)


def edge(a, b):
    draw.line([a[0], a[1], b[0], b[1]], fill=BLACK, width=4)


def label(cx, y, text, font=LABEL_FONT):
    lines = text.split("\n")
    widths = [draw.textlength(line, font=font) for line in lines]
    tw = max(widths)
    th = len(lines) * 15
    x1 = cx - tw / 2 - 7
    y1 = y
    x2 = cx + tw / 2 + 7
    y2 = y + th + 5
    draw.rounded_rectangle([x1, y1, x2, y2], radius=3, fill=LABEL, outline=(220, 220, 220), width=1)
    yy = y + 3
    for line in lines:
        draw.text((cx, yy), line, fill=TEXT, font=font, anchor="ma")
        yy += 15


def node(x, y, code, text, below=16):
    r = 10
    draw.ellipse([x - r, y - r, x + r, y + r], fill=WHITE, outline=BLACK, width=2)
    draw.text((x, y - 1), code, fill=TEXT, font=NODE_FONT, anchor="mm")
    label(x, y + below, text)
    return (x, y)


def connect(parent, children):
    for child in children:
        edge(parent, child)


# Верхний уровень графа
root = node(900, 35, "БЗ", "База\nзнаний", 15)

anketa = node(170, 165, "А", "Анкета\nстудента")
company = node(500, 150, "К", "company/6")
position = node(860, 145, "В", "position/6")
interests = node(1220, 150, "И", "position_\ninterests/2")
rules = node(1580, 165, "П", "Правила\nвывода")
connect(root, [anketa, company, position, interests, rules])

# Анкета студента
a1 = node(40, 310, "1", "Спец.")
a2 = node(120, 355, "2", "GPA")
a3 = node(205, 310, "3", "Город")
a4 = node(285, 380, "4", "Формат")
a5 = node(365, 320, "5", "Отрасль")
a6 = node(225, 505, "6", "Вопросы\n6-11")
connect(anketa, [a1, a2, a3, a4, a5, a6])
s1 = node(115, 610, "S", "StudentSkills", 12)
s2 = node(335, 610, "T", "StudentInterests", 12)
connect(a6, [s1, s2])

# Компании
c1 = node(430, 310, "it", "ИТ-\nКомплекс")
c2 = node(520, 385, "pr", "ПромТех")
c3 = node(610, 310, "rj", "РЖД")
c4 = node(430, 510, "o", "Отрасль")
c5 = node(520, 545, "g", "Город")
c6 = node(610, 510, "m", "Мин.\nGPA")
connect(company, [c1, c2, c3, c4, c5, c6])

# Вакансии
p1 = node(720, 305, "py", "Python")
p2 = node(825, 390, "fr", "Frontend")
p3 = node(950, 305, "sa", "Сис.\nадмин")
p4 = node(735, 525, "sp", "Спец.")
p5 = node(860, 590, "sk", "Навыки")
p6 = node(990, 525, "co", "Компания")
connect(position, [p1, p2, p3, p4, p5, p6])
p7 = node(785, 455, "bu", "Бух.")
p8 = node(910, 455, "au", "Аудитор")
p9 = node(1035, 455, "ht", "Отель")
connect(position, [p7, p8, p9])

# Интересы
i1 = node(1125, 305, "pr", "programming")
i2 = node(1235, 390, "web", "web")
i3 = node(1350, 305, "net", "networks")
i4 = node(1160, 520, "fin", "finance")
i5 = node(1290, 560, "serv", "service")
connect(interests, [i1, i2, i3, i4, i5])

# Правила
r1 = node(1460, 305, "S", "match_\nspec")
r2 = node(1570, 380, "G", "match_gpa")
r3 = node(1690, 305, "L", "match_\nlocation")
r4 = node(1515, 500, "F", "industry/\nformat")
r5 = node(1660, 535, "I", "interest_\nscore")
connect(rules, [r1, r2, r3, r4, r5])
score = node(1580, 610, "%", "Score\n50+30+20", 12)
connect([1580, 165], [score])
for r in [r1, r2, r3, r4, r5]:
    edge(r, score)

out1 = node(1445, 630, "V", "Вакансии", 10)
out2 = node(1730, 630, "M", "Недостающие\nнавыки", 10)
edge(score, out1)
edge(score, out2)

img.save("graph_model_flowchart.png")
print(os.path.abspath("graph_model_flowchart.png"))
