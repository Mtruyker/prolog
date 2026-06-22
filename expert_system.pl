:- encoding(utf8).
% =================================================================
% БАЗА ЗНАНИЙ И ПРАВИЛА ЛОГИЧЕСКОГО ВЫВОДА ДЛЯ ЭКСПЕРТНОЙ СИСТЕМЫ
% Выбор места производственной практики студентов техникума
% =================================================================

% -----------------------------------------------------------------
% ФАКТЫ: КОМПАНИИ (company/6)
% Формат: company(ID, Название, Отрасль, Город, МинСреднийБалл, Описание)
% -----------------------------------------------------------------
company(it_complex, 'ООО "ИТ-Комплекс"', it, moscow, 4.0, 'Ведущая ИТ-компания по разработке веб-приложений и корпоративного ПО для финансового сектора.').
company(prom_tech, 'ООО "ПромТех"', industry, spb, 3.5, 'Современный машиностроительный завод, специализирующийся на высокоточном проектировании деталей и ЧПУ-производстве.').
company(rjd, 'АО "РЖД"', transport, ekaterinburg, 3.0, 'Крупнейший транспортно-логистический оператор РФ с возможностями стажировок во многих регионах.').
company(cbr, 'Центральный Банк РФ', finance, moscow, 4.5, 'Главный финансовый регулятор страны с высокими требованиями к академической успеваемости студентов.').
company(cosmos, 'Гостиница "Космос"', tourism, moscow, 3.0, 'Один из крупнейших гостиничных комплексов Москвы, активно работающий со студентами профилей сервиса.').
company(soft_lines, 'ООО "СофтЛайнс"', it, remote, 3.8, 'Прогрессивная ИТ-компания, работающая исключительно в распределенном (удаленном) формате над SaaS-продуктами.').

% -----------------------------------------------------------------
% ФАКТЫ: ВАКАНСИИ / МЕСТА ПРАКТИКИ (position/6)
% Формат: position(ID, Должность, ID_Компании, ПодходящиеСпециальности, ТребуемыеНавыки, ОписаниеОбязанностей)
% Специальности: 
%   is  - Информационные системы и программирование
%   set - Сетевое и системное адрегистрация
%   tm  - Технология машиностроения
%   buh - Экономика и бухгалтерский учет
%   tur - Туризм и гостеприимство
% Навыки:
%   python, sql, git, javascript, html, css, react, linux, tcp_ip, bash,
%   autocad, cnc, solidworks, one_c, excel, fin_analysis, law, english, communication
% -----------------------------------------------------------------
position(py_dev, 'Разработчик Python', it_complex, [is], [python, sql, git], 'Участие в разработке серверной части веб-приложений на FastAPI/Django, проектирование баз данных SQL и написание юнит-тестов.').
position(front_dev, 'Frontend-разработчик', soft_lines, [is], [javascript, html, css, react, git], 'Разработка отзывчивых веб-интерфейсов по макетам Figma на базе React, оптимизация скорости загрузки страниц.').
position(sys_admin, 'Помощник системного администратора', rjd, [set], [linux, tcp_ip, bash], 'Мониторинг сетевой инфраструктуры, настройка Linux-серверов, написание скриптов автоматизации на Bash.').
position(cad_designer, 'Техник-конструктор', prom_tech, [tm], [autocad, cnc, solidworks], 'Разработка чертежей деталей в AutoCAD и SolidWorks, подготовка управляющих программ для металлообрабатывающих станков с ЧПУ.').
position(buh_assistant, 'Помощник бухгалтера', rjd, [buh], [one_c, excel], 'Первичная обработка бухгалтерских документов, проведение сверок с контрагентами, ввод данных в систему 1С:Предприятие.').
position(jr_auditor, 'Младший аудитор', cbr, [buh], [excel, fin_analysis, law], 'Анализ финансовых показателей кредитных организаций, подготовка сводных аналитических таблиц в Excel, изучение нормативно-правовых актов.').
position(hotel_admin, 'Администратор приема и размещения', cosmos, [tur], [english, communication], 'Прием, регистрация и расселение гостей отеля, работа в специализированной СУО, консультации на английском языке, разрешение конфликтных ситуаций.').

% -----------------------------------------------------------------
% ФАКТЫ: ПРОФЕССИОНАЛЬНЫЕ ИНТЕРЕСЫ ДЛЯ ВАКАНСИЙ
% -----------------------------------------------------------------
position_interests(py_dev, [programming, backend, databases]).
position_interests(front_dev, [programming, web, design]).
position_interests(sys_admin, [networks, administration, linux]).
position_interests(cad_designer, [engineering, drawings, machines]).
position_interests(buh_assistant, [documents, accounting, data_entry]).
position_interests(jr_auditor, [finance, analysis, law_docs]).
position_interests(hotel_admin, [communication, service, english]).

% -----------------------------------------------------------------
% ПРАВИЛА ЛОГИЧЕСКОГО ВЫВОДА (Rules)
% -----------------------------------------------------------------

% Вспомогательное правило: проверка вхождения элемента в список
member_of(X, [X|_]).
member_of(X, [_|T]) :- member_of(X, T).

% Вспомогательное правило: длина списка
list_len([], 0).
list_len([_|T], N) :- list_len(T, N1), N is N1 + 1.

% 1. Проверка специальности: специальность студента должна входить в список подходящих для вакансии
match_specialization(StudentSpec, AllowedSpecs) :- 
    member_of(StudentSpec, AllowedSpecs).

% 2. Проверка среднего балла (GPA): средний балл студента должен быть не ниже минимального для компании
match_gpa(StudentGPA, MinGPA) :- 
    StudentGPA >= MinGPA.

% 3. Проверка расположения:
%    - Если студент выбрал "any", подходит любой город.
%    - Если компания предлагает "remote" (удаленно), она подходит при любом выборе студента.
%    - В остальных случаях город студента должен совпадать с городом компании.
match_location(any, _) :- !.
match_location(_, remote) :- !.
match_location(StudentLoc, CompanyLoc) :- 
    StudentLoc = CompanyLoc.

% 4. Проверка предпочтительной отрасли
match_industry(any, _).
match_industry(Industry, Industry).

% 5. Проверка предпочтительного формата работы
match_work_format(any, _).
match_work_format(remote, remote).
match_work_format(office, CompanyLoc) :-
    CompanyLoc \= remote.

% 6. Подсчет совпадений профессиональных интересов
interest_score([], _, 0).
interest_score(StudentInterests, PositionID, Score) :-
    position_interests(PositionID, PositionInterests),
    intersect_count(PositionInterests, StudentInterests, MatchCount),
    list_len(StudentInterests, TotalCount),
    (TotalCount > 0 ->
        Score is (MatchCount * 20) / TotalCount
    ;
        Score is 0
    ).

% 4. Подсчет количества совпадающих навыков студента и требований вакансии
intersect_count([], _, 0).
intersect_count([H|T], StudentSkills, Count) :-
    member_of(H, StudentSkills),
    !,
    intersect_count(T, StudentSkills, SubCount),
    Count is SubCount + 1.
intersect_count([_|T], StudentSkills, Count) :-
    intersect_count(T, StudentSkills, Count).

% 5. Определение недостающих навыков (требуются вакансией, но отсутствуют у студента)
missing_skills([], _, []).
missing_skills([H|T], StudentSkills, Missing) :-
    member_of(H, StudentSkills),
    !,
    missing_skills(T, StudentSkills, Missing).
missing_skills([H|T], StudentSkills, [H|Missing]) :-
    missing_skills(T, StudentSkills, Missing).

% 6. ГЛАВНОЕ ПРАВИЛО РЕКОМЕНДАЦИИ
% Аргументы:
%   Входные:  StudentSpec, StudentSkills, StudentGPA, StudentLoc
%   Выходные: PositionID, Title, CompanyName, CompanyLoc, Score, MissingSkills
recommend_position(StudentSpec, StudentSkills, StudentGPA, StudentLoc, PositionID, Title, CompanyName, CompanyLoc, Score, MissingSkills) :-
    recommend_position(StudentSpec, StudentSkills, StudentGPA, StudentLoc, any, any, [], PositionID, Title, CompanyName, CompanyLoc, Score, MissingSkills).

recommend_position(StudentSpec, StudentSkills, StudentGPA, StudentLoc, IndustryPref, WorkFormatPref, StudentInterests, PositionID, Title, CompanyName, CompanyLoc, Score, MissingSkills) :-
    % Находим вакансию и соответствующую ей компанию
    position(PositionID, Title, CompanyID, AllowedSpecs, ReqSkills, _Duties),
    company(CompanyID, CompanyName, Industry, CompanyLoc, MinGPA, _Description),
    
    % Проверяем жесткие критерии отбора (фильтры)
    match_specialization(StudentSpec, AllowedSpecs),
    match_gpa(StudentGPA, MinGPA),
    match_location(StudentLoc, CompanyLoc),
    match_industry(IndustryPref, Industry),
    match_work_format(WorkFormatPref, CompanyLoc),
    
    % Считаем количество совпадений по навыкам
    intersect_count(ReqSkills, StudentSkills, MatchCount),
    list_len(ReqSkills, TotalCount),
    
    % Вычисляем процент соответствия (Score):
    % Жесткие критерии дают базовые 50%. Навыки дают до 30%, интересы - до 20%.
    (TotalCount > 0 -> 
        SkillsScore is (MatchCount * 30) / TotalCount 
    ; 
        SkillsScore is 30
    ),
    interest_score(StudentInterests, PositionID, InterestScore),
    Score is 50 + SkillsScore + InterestScore,
    
    % Находим, каких навыков не хватает
    missing_skills(ReqSkills, StudentSkills, MissingSkills).
