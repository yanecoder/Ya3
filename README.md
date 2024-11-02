# Ya3
Базовый интерпретатор языка Ya3, для изучения и показа работы.
Написан на python3.11


# Навигация
### Examples
Примеры кода на языке Ya3.

### Interpreter
Директория с модулями для интерпретации кода.

#### Модули
1. lexer.py - Разбиение на лексемы
2. parser.py - Формирование блоков (синтаксического дерева)
3. executor.py -  Запуск кода
4. tokenizer.py - Токены
5. exceptions.py - Исключения

### Main
main.py - интерпретатор
ya3.exe - билд интерпретатора для языка ya3

# Синтаксис
1. Код разбивается на лексемы, затем формируется синтаксическое дерево, после
   код приводится в исполнение.
2. После каждой строки обязан стоять знак ; (EoS, End of String).
3. Переменная объявляется после знака $, не требует типа ($a = <значение).
   Название переменной может содержать только буквенные символы. Переменная
   может содержать только численное или буквенное значение. Переменная должна
   сохранять знак $ при использовании после объявления.
5. Вывод производится командой print (print <значение>)
6. Значение - любые взаимодействия между переменными ($a+$b, $a-$b), взаимодействие
   переменной с данным ($a = $b - 15), взаимодействие данного ($a = 15 - 10),
   любая переменная, либо данное само по себе.
   Данное - строка, число, не объявленные в переменную.
8. Допускается как использование пробелов, как и их отсутствие ($a=$b+2, $a = $b + 2)
9. Строковые данные должны быть выделены в двойные кавычки (print "Hello, world!")
   

# Примеры
Все примеры вы можете найти в директории ```/examples```

# Примечания
1. При доработке кода интерпретатора при использовании точек остановки для
   дебага, делайте print(1) после кодаи размещайте ее туда, чтобы программа
   сохраняла результат. 
version: v2

