:- encoding(utf8).
% =================================================================
% КОНСОЛЬНЫЙ ЗАПУСК ЭКСПЕРТНОЙ СИСТЕМЫ (run_cli.pl)
% Интерактивный терминальный интерфейс для SWI-Prolog
% =================================================================

% Установка кодировки UTF-8 для корректного отображения русских символов
:- set_stream(user_output, encoding(utf8)).
:- set_stream(user_error, encoding(utf8)).
:- set_stream(user_input, encoding(utf8)).

:- consult('expert_system.pl').

positive_answer(yes).
positive_answer(y).

negative_answer(no).
negative_answer(n).

ask_profile_question(Number, Text, YesSkills, YesInterests, Skills, Interests) :-
    format('Вопрос ~w. ~w (yes/no): ', [Number, Text]),
    read(Answer),
    nl,
    (positive_answer(Answer) ->
        Skills = YesSkills,
        Interests = YesInterests
    ; negative_answer(Answer) ->
        Skills = [],
        Interests = []
    ;
        writeln('Ошибка: введите yes. или no.'),
        ask_profile_question(Number, Text, YesSkills, YesInterests, Skills, Interests)
    ).

append_all([], []).
append_all([H|T], Result) :-
    append_all(T, Rest),
    append(H, Rest, Result).

ask_diagnostics(Skills, Interests) :-
    ask_profile_question(6, 'Вам интересна разработка программ, серверная логика или базы данных?', [python, sql, git], [programming, backend, databases], S6, I6),
    ask_profile_question(7, 'Вам интересны сайты, интерфейсы и дизайн экранов?', [javascript, html, css, react, git], [programming, web, design], S7, I7),
    ask_profile_question(8, 'Вам интересны сети, серверы Linux и администрирование?', [linux, tcp_ip, bash], [networks, administration, linux], S8, I8),
    ask_profile_question(9, 'Вам интересны чертежи, станки с ЧПУ и техническое проектирование?', [autocad, cnc, solidworks], [engineering, drawings, machines], S9, I9),
    ask_profile_question(10, 'Вам интересны бухгалтерские документы, Excel, финансы или право?', [one_c, excel, fin_analysis, law], [documents, accounting, finance, analysis, law_docs], S10, I10),
    ask_profile_question(11, 'Вам интересны общение с клиентами, сервис и английский язык?', [english, communication], [communication, service, english], S11, I11),
    append_all([S6, S7, S8, S9, S10, S11], AllSkills),
    append_all([I6, I7, I8, I9, I10, I11], AllInterests),
    list_to_set(AllSkills, Skills),
    list_to_set(AllInterests, Interests).

% Точка входа в программу
start :-
    writeln('================================================================='),
    writeln('   ЭКСПЕРТНАЯ СИСТЕМА ПОДБОРА МЕСТА ПРОИЗВОДСТВЕННОЙ ПРАКТИКИ    '),
    writeln('                   (Колледж / Техникум)                          '),
    writeln('================================================================='),
    writeln('Ответьте на 11 вопросов экспертной системы. После каждого ответа ставьте точку.'),
    nl,
    writeln('Доступные специальности для ввода:'),
    writeln('  is  - Информационные системы и программирование'),
    writeln('  set - Сетевое и системное администрирование'),
    writeln('  tm  - Технология машиностроения'),
    writeln('  buh - Экономика и бухгалтерский учет'),
    writeln('  tur - Туризм и гостеприимство'),
    nl,
    write('Вопрос 1. Введите вашу специальность: '),
    read(Spec),
    (member_of(Spec, [is, set, tm, buh, tur]) -> true ; 
        writeln('Ошибка: Неизвестная специальность. Перезапуск...'), nl, start),
    
    nl,
    write('Вопрос 2. Введите ваш средний балл (например, 4.2): '),
    read(GPA),
    (number(GPA) -> true ;
        writeln('Ошибка: Средний балл должен быть числом. Перезапуск...'), nl, start),
    
    nl,
    writeln('Доступные города для ввода: moscow, spb, ekaterinburg, any (любой город)'),
    write('Вопрос 3. Введите желаемый город: '),
    read(Loc),
    (member_of(Loc, [moscow, spb, ekaterinburg, any]) -> true ;
        writeln('Ошибка: Неизвестный город. Перезапуск...'), nl, start),
    
    nl,
    writeln('Доступные форматы работы: office, remote, any'),
    write('Вопрос 4. Введите предпочтительный формат работы: '),
    read(WorkFormat),
    (member_of(WorkFormat, [office, remote, any]) -> true ;
        writeln('Ошибка: Неизвестный формат работы. Перезапуск...'), nl, start),
    
    nl,
    writeln('Доступные отрасли: it, industry, transport, finance, tourism, any'),
    write('Вопрос 5. Введите предпочтительную отрасль: '),
    read(IndustryPref),
    (member_of(IndustryPref, [it, industry, transport, finance, tourism, any]) -> true ;
        writeln('Ошибка: Неизвестная отрасль. Перезапуск...'), nl, start),
    
    nl,
    writeln('--- Профессиональные интересы ---'),
    writeln('Отвечайте yes. или no.'),
    ask_diagnostics(Skills, Interests),
    
    nl,
    writeln('Выполняется поиск подходящих мест практики...'),
    nl,
    
    % Поиск всех рекомендаций
    findall(
        Score-rec(Title, CompanyName, CompanyLoc, MissingSkills),
        recommend_position(Spec, Skills, GPA, Loc, IndustryPref, WorkFormat, Interests, _PositionID, Title, CompanyName, CompanyLoc, Score, MissingSkills),
        Pairs
    ),
    
    % Сортировка пар Score-rec по возрастанию ключа (Score)
    keysort(Pairs, SortedPairs),
    % Разворот для сортировки по убыванию (от лучшего к худшему)
    reverse(SortedPairs, DescSortedPairs),
    
    % Вывод результатов
    print_results(DescSortedPairs),
    
    nl,
    writeln('================================================================='),
    writeln('Спасибо за использование экспертной системы!'),
    writeln('================================================================='),
    nl.

% Вывод списка результатов
print_results([]) :-
    writeln('К сожалению, подходящих мест практики не найдено.'),
    writeln('Рекомендации для прохождения практики:'),
    writeln('1. Постарайтесь повысить средний балл успеваемости.'),
    writeln('2. Расширьте географию поиска (введите "any" в поле города).'),
    writeln('3. Изучите дополнительные навыки, востребованные работодателями.').
    
print_results(Results) :-
    writeln('РЕЗУЛЬТАТЫ ПОДБОРА (отсортированы по соответствию):'),
    writeln('-----------------------------------------------------------------'),
    print_items(Results).

% Вспомогательный вывод элементов списка
print_items([]).
print_items([Score-rec(Title, CompanyName, CompanyLoc, Missing)|T]) :-
    format('~w% соответствия | Должность: ~w~n', [Score, Title]),
    format('               | Компания:  ~w (~w)~n', [CompanyName, CompanyLoc]),
    (Missing == [] ->
        writeln('               | Требования: Полное соответствие!')
    ;
        format('               | Недостающие навыки для изучения: ~w~n', [Missing])
    ),
    writeln('-----------------------------------------------------------------'),
    print_items(T).
