﻿**Красивый выход**

1. документация
   1. research basis
      1. [ссылка](https://docs.google.com/document/d/10N9ROdMv72XtvcX_o4qjufSAxJqiUbW63ein7rRt5hE/edit#heading=h.hh0gpzkd0gsk) на текст
      1. abstract / актуальная аннотация (если отличается от финальной версии, представленной в абстракте)
   1. указание как цитировать  К.А. Маслинский, А. Арбузова, А. Митюкова, С. Рябова. В. Сидненко,  **Библиографический указатель советской детской литературы Старцева**
   1. [лонгрид ](https://github.com/AMitiukova/project/blob/main/frontend/texts/%D0%A3%D0%BA%D0%B0%D0%B7%D0%B0%D1%82%D0%B5%D0%BB%D1%8C_%D0%A1%D1%82%D0%B0%D1%80%D1%86%D0%B5%D0%B2%D0%B0_%D1%81%D0%B0%D0%B9%D1%82.txt)на гитхаб пайджес, если нужен
   1. ссылка на сайт - если есть (пока только [макет](https://github.com/AMitiukova/project/blob/main/%D1%81%D0%B0%D0%B8%CC%86%D1%82.zip))

1. формально: кто мы? (в рамках чего создан проект, кто руководители и т.д.), лицензия

**Руководитель**: Кирилл Александрович Маслинский, руководитель Лаборатории цифровых исследований литературы и фольклора, кандидат исторических наук, старший научный сотрудник

- Александра Митюкова: база данных с фильтрацией
- Аня Арбузова: страницы html сайта
- Валерия Сидненко: tabulator с фильтрацией
- Светлана Рябова, к.и.н.наук: тексты

1. данные как скачать
   1. описание
      1. что за данные, их объем, какие источники, минимальный пример: 


|1|row\_id|**порядковый номер записи в общей объединенной таблице**|71584 записи|
| :- | :- | :- | :- |
|2|vol|**период, библиографические данные которого включает том указателя** (указан на каждом из 18 томов библиографического указателя Старцева)|<p>18 томов:</p><p>1918-1931 - *11098 записей*</p><p>1932-1939 - *4217 записей*</p><p>1940-1945 - *2794 записи*</p><p>1946-1948 - *1950 записей*</p><p>1949-1950 - *1715 записей*</p><p>1951-1952 - *1926 записей*</p><p>1953-1954 - *2076 записей*</p><p>1955-1957 - *3574 записи*</p><p>1958-1960 - *4537 записей*</p><p>1961-1963 - *4496 записей*</p><p>1964-1966 - *4411 записей*</p><p>1967-1969 - *4450 записей*</p><p>1970-1971 - *2672 записи*</p><p>1972-1973 - *3150 записей*</p><p>1974-1975 - *3214 записи*</p><p>1976-1978 - *4968 записей*</p><p>1979-1981 - *5017 записей*</p><p>1982-1984 - *5319 записей*</p>|
|3|num|**порядковый номер издания в указателе определенного периода** (совместно с колонкой vol может считаться уникальным идентификатором каждого издания); некоторые номера приведены с литерой “а” в случае с перевыпущенными или повторяющимися изданиями, например: *1184а*|<p>71584 значения; </p><p>11308 уникальных; </p><p>321 значение с литерой “а”; из них 313 уникальных</p>|
|4|author|**фамилия (фамилии), инициалы (если имеются) автора, приведенные в Указателе;** один и тот же автор может быть указан дважды, например *Пушкин А.* и *Пушкин А.С.*; в случае, когда авторов несколько, данные приведены через “;”, например: *Боголепов, П.; Верховская, А.; Сосницкая, М.*|<p>61422 заполненных значений; 10162 - “NOAUTHOR” </p><p>18698 уникальных</p><p></p>|
|5|author\_gender|**пол автора (авторов) в порядке и в соответствии с колонкой “author”**: “m” - мужской; “f” - женский; “-” - не определен; вновь созданная колонка; в случае, когда авторов несколько, данные приведены через “;” например: *m; f; f*|<p>61422 заполненных значений;</p><p>60 уникальных;</p><p>10162 NA</p>|
|6|title|**наименование издания**|<p>71535 заполненных значений; </p><p>40199 уникальных;</p><p>49 NA</p>|
|7|subtitle|**подзаголовок, содержащий зачастую информацию о жанре и/или формате издания, приведенном в Указателе,** например:** *Пособие для учащихся*|<p>51252 заполненных значений;</p><p>13340 уникальных;</p><p>20332 NA</p>|
|8|genre|<p>**унифицированное значение жанра издания, в соответствии с разработанным группой перечнем основных жанров детской литературы из 23 значений;**  вновь созданная колонка значений: </p><p>1. Рассказ</p><p>2. Повесть</p><p>3. Сказка</p><p>4. Роман</p><p>5. Новелла</p><p>6. Миф</p><p>7. Быль</p><p>8. Былина</p><p>9. Легенда (в том числе сказания)</p><p>10. Баллада</p><p>11. Притча</p><p>12. Пословицы</p><p>13. Поговорки</p><p>14. Загадки</p><p>15. Потешки</p><p>16. Поэма</p><p>17. Басня</p><p>18. Очерк</p><p>19. Стихи (в том числе песни)</p><p>20. Пьеса (в том числе сценки, инсценировки, сцены и сценарии)</p><p>21. Драма</p><p>22. Трагедия</p><p>23. Комедия</p><p>каждое издание может иметь более одного значения, например: *Загадки; Рассказ; Сказка; Стихи*</p>|<p>50337 заполненных значений;</p><p>236 уникальных;</p><p>21247 NA</p>|
|9|editorial|**дополнительная библиографическая информация о редакторах, художниках или переводчиках,** например: *Пер. с датск. А. Ганзен. Рис. В. Алфеевского.*|<p>59915 заполненных значений;</p><p>41364 уникальных;</p><p>11669 NA</p>|
|10|city|**город издания, в формате, приведенном в Указателе,** например:** *М.; Л.* или  *Куйбышев*|<p>71535 заполненных значений;</p><p>309 уникальных; </p><p>49 NA;</p><p>44 ошибки (REF\*\*\*\*)</p>|
|11|actual\_city\_name|**нормализованное значение города в соответствии с современным наименованием на русском языке,** например: *Самара*; вновь созданная колонка|<p>71535 заполненных значений;</p><p>276 уникальных; </p><p>49 пустых;</p><p>44 ошибки (REF\*\*\*\*)</p>|
|12|publisher|**наименование издательства в соответствии с приведенными в Указателе,** например:** *Огиз—Молодая гвардия*|<p>71582 заполненных значений;</p><p>1860 уникальных;</p><p>1 пустое</p><p>1 NA</p>|
|13|year|**год издания**, например: *1975*|<p>71479 заполненных значений;</p><p>70 уникальных (с 1917 по 1985 гг.);</p><p>105 NA</p>|
|14|series|**наименование серии,** например: *Библиотека для семьи и школы***  или** *Пионер — значит первый*|<p>48161 заполненных значений;</p><p>2419 уникальных;</p><p>23423 NA</p><p></p>|
|15|volume|**номер выпуска, в случае когда серия выпускалась многократно или периодически** (значение выделено из колонки series), например: *Вып. 32*|<p>609 заполненных значений; </p><p>277 уникальных;</p><p>70975 NA</p>|
|16|pages|**количество страниц,** например:**  *594*|<p>69470 заполненных значений; </p><p>720 уникальных;</p><p>2114 NA</p>|
|17|printrun|**тираж,** например:** *100000*|<p>70375 заполненных значений; </p><p>875 уникальных;</p><p>1209 NA</p>|
|18|price|**цена издания** в формате 0.1 = 1 коп., например: *0.22 (=22 коп.)* или *1.37 (=1 руб. 37 коп.)*|<p>67742 заполненных значений; </p><p>532 уникальных;</p><p>3842 NA</p>|
|19|addressee|**адресация** издания в соответствии с Указателем; включает как биологическую адресацию, например: *для малышей*, так и институциональную, например:  *для дошкольников*|<p>49933 заполненных значений;</p><p>335 уникальных;</p><p>21651 NA</p>|
|20|contents|**содержание издания**, в случае, если оно приведено в Указателе, например: *Кот Васька; Общество чистых тарелок; На елке в школе*|<p>16247 заполненных значений;</p><p>15554 уникальных;</p><p>55337 NA</p>|
|21|section|**раздел;** внутри каждого раздела материал систематизирован по жанрам и периодам, например: *# Художественная литература ## Литература народов СССР ### Русская литература #### Советская литература*|<p>71584 заполненных значений;</p><p>55 уникальных</p>|


1. все метаданные: кто собирал, кто и чем размечал

Машиночитаемая библиографическая база данных по русской детской литературе 1918 – 1984 гг., составленная на основе «Указателя И. И. Старцева», оцифрованная и распознанная рабочей группой во главе с К. А. Маслинским. База данных представляет собой библиографические данные 71 583 книг из всех томов «Указателя Старцева». В сводной таблице содержатся такие колонки, как номер тома, фамилия, имя и отчество автора, название книги, подзаголовок, данные о редакторах, иллюстраторах и переводчиках, место издания, название издательства, год издания, серия, количество страниц, тираж, цена, адресация (категория и возраст детей, которым адресована книга). Внутри каждого раздела материал систематизирован по жанрам и периодам. 

1. формат: CSV - таблица

1. поиск по данным, фильтрация → веб-интерфейс

1. ЧТО МЫ ПИШЕМ НА САЙТЕ ПРОГРАММЫ
   1. короткое и рекламное описания для широкого круга


Во всех книжных магазинах разделы детской литературы, пожалуй, самые обширные. Огромным спросом пользуются переизданные советские книжки. Все больше ценятся старые иллюстрации: И. Билибина, В. Лебедева, П. Митурича, В. Конашевича, и даже Н. Альтмана и В. Татлина. Многие детские издательства буквально ищут, какие книжки переиздать, а ностальгирующие покупатели переполняются счастьем, когда находят давно забытые книжки из детства. Но кроме библиофильского, ностальгического и коммерческого интересов, все больше исследователей занимаются детской литературой. Все больше появляется публикаций и выставкой, посвященных советской детской литературе.

Наша рабочая группа во главе с исследователем детской литературы К. А. Маслинским создала сайт с указателем практически всех детских книг, когда-либо выходивших в Советском союзе. В основе нашего проекта — оцифрованный и распознанный библиографический указатель детской литературы И.И. Старцева. В указателе содержатся полные библиографические данные о книгах, выходивших в СССР с 1918 по 1984 годы. С помощью фильтров в нашем указателе можно найти нужных авторов, названия книг, годы и места изданий, переводчиков, иллюстраторов и многое другое. Кому-то интересно будет почитать исследовательский раздел сайта, узнать, кто был самым издаваемым автором, кто такие детские авторы, кому были адресованы книги, кто был самым популярным иллюстратором, когда издавалось больше всего книг и какими тиражами, а еще можно сопоставить исторические события с процессами книгоиздательстве. Будем рады видеть вас на нашем сайте! Обещаем, что обязательно будет интересно!

1. [картинка](https://arch.rgdb.ru/xmlui/bitstream/id/2991803/?sequence=-1)
1. и [ссылка](https://github.com/AMitiukova/project) на проект (на репозиторий и если сайт, то на сайт)
