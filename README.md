Расчеты, необходимые для статьи про отжиг. Содержание:

* binary — содержит сырые несжатые исходные и отожженные картинки 500x500 или
  1000x1000 пикселей.
* images — картинки в png, полученные из binary
* scripts — скрипты для построения графиков
* target-plots — графики целевых функций
* corrfns — разницы в корреляционных функциях. Формат пути таков:
  `corrfns/имя-образца/минимизируемые-функции`
* corrfns-plot — графики разницы в корреляционных функциях.

Образцы:

* checkboard — шахматная доска 500x500 и отжиг из шума
* disks — мелкие случайные круги 500x500 и отжиг из шума
* noise — value noise 1000x1000 и отжиг из кругов
* sandstone — песчанник 1000x1000 и отжиг из кругов
