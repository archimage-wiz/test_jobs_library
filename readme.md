# Библиотечное приложение

Библиотечное приложение позволяет управлять библиотекой книг, создавать, удалять и изменять их, а также искать их по различным критериям.

## Функциональные возможности

* Создание и удаление книг
* Изменение статуса книг (доступна/недоступна)
* Поиск книг по различным критериям (автор, название, год издания)
* Вывод списка всех книг

## Описание интерфейса

* Меню:
	+ Создать новую книгу
	+ Удалить книгу
	+ Изменить статус книги
	+ Поиск книг
	+ Вывод списка всех книг
* Формы для ввода данных:
	+ Создание новой книги: автор, название, год издания
	+ Изменение статуса книги: идентификатор книги, статус (доступна/недоступна)
* Вывод информации о книгах:
	+ Список всех книг
	+ Информация о конкретной книге (автор, название, год издания, статус)

## Технические требования

* Операционная система: Windows, macOS, Linux
* Версия Python: 3.8+
* Дополнительные библиотеки и модули: uuid, datetime

## Примеры использования

* Создание новой книги:
	+ Выберите пункт "Создать новую книгу" в меню
	+ Введите автор, название и год издания книги
	+ Нажмите кнопку "Создать"
* Изменение статуса книги:
	+ Выберите пункт "Изменить статус книги" в меню
	+ Введите идентификатор книги
	+ Выберите новый статус (доступна/недоступна)
	+ Нажмите кнопку "Изменить"
* Поиск книги по автору:
	+ Выберите пункт "Поиск книг" в меню
	+ Введите автор книги
	+ Нажмите кнопку "Поиск"