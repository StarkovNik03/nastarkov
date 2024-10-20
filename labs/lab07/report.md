# **Отчет к лабораторной работе №7**
## **Common information**
discipline: Основы информационной безопасности  
group: НПМбд-02-21  
author: Старков Н.А.
---
---
## **Цель работы**

Освоить на практике применение режима однократного гаммирования.

## **Выполнение работы**

1) Для начала я убедился, что компилятор gcc установлен, используя команду “gcc -v”. Затем отключила систему запретов до очередной перезагрузки системы
командой “sudo setenforce 0”, после чего команда “getenforce” вывела “Permissive”

![Команды gcc -v И sudo setenforce 0](image/1.png)

2) Проверили успешное выполнение команд “whereis gcc” и “whereis g++”

![Комнады whereis gcc и whereis g++ ](image/2.png)

3) Вошли в систему от имени пользователя guest командой “su - guest”. Создали программу simpleid.c командой “touch simpleid.c” и открыла её в редакторе командой “gedit /home/guest/simpleid.c”

![Вход и создание файла](image/3.png)

4) Написали код в созданном файле

![Код 1](image/4.png)

5) Скомпилировали программу и запустили ее 

![Команды gcc simpleid.c -o simpleid и ./simpleid](image/5.png)

6) Создаем новый файл, там пишем более сложный код, компилируем и запускаем программу.

![Создание файла](image/6.png)

![Код 2](image/7.png)

![Компиляция и запуск](image/8.png)

7) От имени суперпользователя выполнили команды “sudo chown root:guest/home/guest/simpleid2” и “sudo chmod u+s /home/guest/simpleid2”, затем выполнили проверку правильности установки новых атрибутов и смены владельца файла simpleid2 командой “sudo ls -l /home/guest/simpleid2”. Этими командами была произведена смена пользователя файла на root и установлен SetUID-бит.

![Сменили права](image/9.png)

![Запуск программы](image/10.png)

Запустил программы simpleid2 и id. Теперь появились различия в uid

8) Проделал тоже самое относительно SetGID-бита. Также можем заметить различия с предыдущим пунктом.

![Сменили права](image/11.png)

![Запуск программы](image/12.png)

9) Создаем новый файл readfile. Скомпилировали созданную программу командой “gcc readfile.c -o readfile”. Сменили владельца у файла readfile.c командой “sudo chown root:guest/home/guest/readfile.c” и поменяли права так, чтобы только суперпользовательмог прочитать его, а guest не мог, с помощью команды “sudo chmod 700/home/guest/readfile.c”. Теперь убедились, что пользователь guest не может
прочитать файл readfile.c командой “cat readfile.c”, получив отказ в доступе.

![Код 3](image/13.png)

![Сменили права](image/14.png)

![Запуск программы](image/15.png)

10) Поменяли владельца у программы readfile и устанавила SetUID. Проверили, может ли программа readfile прочитать файл readfile.c командой “./readfile readfile.c”. Прочитать удалось. Аналогично проверили, можно ли прочитать файл /etc/shadow. Прочитать удалось

![Сменили права](image/16.png)

![Тщетная попытка прочтения](image/17.png)

11) Командой “ls -l / | grep tmp” убеждились, что атрибут Sticky на директории /tmp установлен. От имени пользователя guest создали файл file01.txt в директории /tmp со словом test командой “echo”test” > /tmp/file01.txt”. Просмотрели атрибуты у только что созданного файла и разрешаем чтение и запись для категории пользователей “все остальные” командами “ls -l /tmp/file01.txt” и “chmod o+rw
/tmp/file01.txt”

![Команда ls -l / | grep tmp](image/18.png)

![Команда “echo”test” > /tmp/file01.txt](image/19.png)

12) От имени пользователя guest2 попробовали прочитать файл командой “cat/tmp/file01.txt” - это удалось. Далее попытались дозаписать в файл слово test2, проверить содержимое файла и записать в файл слово test3, стерев при этом всю имеющуюся в файле информацию - эти операции удалось выполнить только в случае, если еще дополнительно разрешить чтение и запись для группы пользователей командой “chmod g+rw /tmp/file01.txt”. От имени пользователя guest2 попробовала удалить файл - это не удается ни в каком из случаев, возникает ошибка

![Вход от имени guest2 и попытка чтения](image/20.png)

![Работа с файлом от имени guest](image/21.png)

![Работа с файлом от имени guest](image/22.png)

13) Повысили права до суперпользователя командой “su -” и выполнили команду, снимающую атрибут t с директории /tmp “chmod -t /tmp”. После чего покинули режим суперпользователя командой “exit”. Повторили предыдущие шаги. Теперь мне удалось удалить файл file01.txt от имени пользователя, не являющегося его владельцем

![Команда su - и очередной chmod](image/23.png)

![Проверка от имени guest2](image/24.png)

14) Вернули атрибут t+

![Возвращение легенды](image/25.png)

![Возвращение легенды](image/26.png)


## **Вывод**
В ходе выполнения лабораторной работы №7 я развил навыки применения режима однократного гаммирования.


