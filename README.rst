====================================================
Интерфейс для редактирования данных в РСУБД на PyQt5
====================================================


Задание
=======

Для разработки интерфейса необходимо использовать библиотеку PyQt5, для работы с БД необходимо использовать библиотеку SQLAlchemy.


Разворачивание
==============


.. code-block:: sh

    $ sudo apt build-dep python3-pyqt5
    $ poetry shell
    $ poetry install


Реализация
==========

Дизайн
------

Текущая обстановка такова, что нужно продемонстрировать навык погружения в неизвестную сферу (косвенно, поверхностно известную).
Главная цель - это состряпать приложение, которое будет утилитарно выполнять свою функцию, без дружественных человеку изысков.
Однако задание превратилось для меня в борьбу с самим собой. У меня есть предубеждения как правильно строить архитектуру приложений. Я перебирал различные материалы по Qt-Qml-Quick в поиске чего-то близкого.
Конечно все эти поиски не увенчались успехом - моя придумка живет только у меня в голове. И вот спустя 2 недели я вернулся в начало - qt doc, что бы собрать самую простую связь. Питон предоставляет значение url соединения с БД, qt-qml обслуживает возможную корректировку человеком и передаёт сигнал обработно в питон с утвержденным url от человека.




Лицензия
========

Код предоставляется по лицензии `GPLv3 <https://www.gnu.org/licenses/gpl-3.0.ru.html>`_.
