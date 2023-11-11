# Практические задания по курсу "Нейронные сети"
## Тестирование
### 1. Создание ориентированного графа 
```
python3 nntask1.py input1=arcs1.txt output1=digraph1.xml
python3 nntask1.py input1=arcs2.txt output1=digraph2.xml
python3 nntask1.py input1=arcs3.txt output1=digraph3.xml
```
В arcs3.txt представлен граф с циклом, поэтому в заданиях 2 и 3 не будет получен результат.
### 2. Создание функции по графу
```
python3 nntask2.py input1=digraph1.xml output1=prefix_func1.txt
python3 nntask2.py input1=digraph2.xml output1=prefix_func2.txt
python3 nntask2.py input1=digraph3.xml output1=prefix_func3.txt
```

### 3. Вычисление значения функции на графе
```
python3 nntask3.py input1=digraph1.xml input2=operations1.txt output1=func_value1.txt
python3 nntask3.py input1=digraph2.xml input2=operations2.txt output1=func_value2.txt
python3 nntask3.py input1=digraph2.xml input2=operations3.txt output1=func_value3.txt
```
Первый граф ($5 * 5 + e^{3 * 9}$):
![](https://github.com/unins000exe/NI/blob/main/img/test1.png)

Второй граф ($e^{3 * 1 + 2}$):
![](https://github.com/unins000exe/NI/blob/main/img/test2.png)

В последнем тесте у вершины E задана операция $exp$, но она имеет двух родителей (то есть два аргумента), поэтому программа завершает работу с выводом сообщения об ошибке.
