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

% Ввод списка навыков до ввода слова 'done'
read_skills(Skills) :-
    write('Введите ваш навык (в нижнем регистре, например, python, или done для завершения): '),
    read(Skill),
    (Skill == done ->
        Skills = []
    ;
        read_skills(Rest),
        Skills = [Skill|Rest]
    ).

% Точка входа в программу
start :-
    writeln('================================================================='),
    writeln('   ЭКСПЕРТНАЯ СИСТЕМА ПОДБОРА МЕСТА ПРОИЗВОДСТВЕННОЙ ПРАКТИКИ    '),
    writeln('                   (Колледж / Техникум)                          '),
    writeln('================================================================='),
    nl,
    writeln('Доступные специальности для ввода:'),
    writeln('  is  - Информационные системы и программирование'),
    writeln('  set - Сетевое и системное администрирование'),
    writeln('  tm  - Технология машиностроения'),
    writeln('  buh - Экономика и бухгалтерский учет'),
    writeln('  tur - Туризм и гостеприимство'),
    nl,
    write('Введите вашу специальность: '),
    read(Spec),
    (member_of(Spec, [is, set, tm, buh, tur]) -> true ; 
        writeln('Ошибка: Неизвестная специальность. Перезапуск...'), nl, start),
    
    nl,
    write('Введите ваш средний балл (например, 4.2): '),
    read(GPA),
    (number(GPA) -> true ;
        writeln('Ошибка: Средний балл должен быть числом. Перезапуск...'), nl, start),
    
    nl,
    writeln('Доступные города для ввода: moscow, spb, ekaterinburg, any (любой город)'),
    write('Введите желаемый город: '),
    read(Loc),
    
    nl,
    writeln('--- Ввод ваших навыков ---'),
    writeln('Вводите навыки по одному. В конце каждого ввода ставьте точку (.) и нажимайте Enter.'),
    writeln('Примеры: python. sql. git. autocad. one_c. communication. english.'),
    writeln('Когда введете все навыки, напишите done. и нажмите Enter.'),
    nl,
    read_skills(Skills),
    
    nl,
    writeln('Выполняется поиск подходящих мест практики...'),
    nl,
    
    % Поиск всех рекомендаций
    findall(
        Score-rec(Title, CompanyName, CompanyLoc, MissingSkills),
        recommend_position(Spec, Skills, GPA, Loc, _PositionID, Title, CompanyName, CompanyLoc, Score, MissingSkills),
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
