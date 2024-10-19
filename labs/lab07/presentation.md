---
## Front matter
lang: ru-RU
title: Презентация к лабораторной работе №7
author: Старков Н.А
group: НПМбд-02-21

## Formatting
toc: false
slide_level: 2
theme: metropolis
header-includes: 
 - \metroset{progressbar=frametitle,sectionpage=progressbar,numbering=fraction}
 - '\makeatletter'
 - '\beamer@ignorenonframefalse'
 - '\makeatother'
aspectratio: 43
section-titles: true
---

# Презентация к лабораторной работе №7

# Цель работы

Освоить на практике применение режима однократного гаммирования.

# Выполнение работы

## Применение команд gcc -v И sudo setenforce 0

![Команды gcc -v И sudo setenforce 0](image/1.png)

## Проверили успешное выполнение команд “whereis gcc” и “whereis g++”

![Комнады whereis gcc и whereis g++ ](image/2.png)

## Вход и создание файла

![Вход и создание файла](image/3.png)

## Код 1

![Код 1](image/4.png)

## Скомпилировали программу и запустили ее 

![Команды gcc simpleid.c -o simpleid и ./simpleid](image/5.png)

## Создаем новый файл, там пишем более сложный код, компилируем и запускаем программу.

![Создание файла](image/6.png)

![Код 2](image/7.png)

![Компиляция и запуск](image/8.png)

## Сменили права и запустили программу

![Сменили права](image/9.png)

![Запуск программы](image/10.png)

## Проделал тоже самое относительно SetGID-бита. Также можем заметить различия с предыдущим пунктом.

![Сменили права](image/11.png)

![Запуск программы](image/12.png)

## Код 3

![Код 3](image/13.png)

![Сменили права](image/14.png)

![Запуск программы](image/15.png)

## Снова сменили права и попробовали прочитать

![Сменили права](image/16.png)

![Тщетная попытка прочтения](image/17.png)

## Работа с Sticky-битом

![Команда ls -l / | grep tmp](image/18.png)

![Команда “echo”test” > /tmp/file01.txt](image/19.png)

## Работа от пользователя guest2

![Вход от имени guest2 и попытка чтения](image/20.png)

![Работа с файлом от имени guest](image/21.png)

![Работа с файлом от имени guest](image/22.png)

## Убрали атрибут t

![Команда su - и очередной chmod](image/23.png)

![Проверка от имени guest2](image/24.png)

## Вернули атрибут t
![Возвращение легенды](image/25.png)

![Возвращение легенды](image/25.png)

# Вывод 

В ходе выполнения лабораторной работы №7 я развил навыки применения режима однократного гаммирования.