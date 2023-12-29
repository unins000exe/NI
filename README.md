# Практические задания по курсу "Нейронные сети"
## Тестирование
### 1. Создание ориентированного графа 
```
python3 nntask1.py input1=tests/arcs1.txt output1=tests/digraph1.xml
python3 nntask1.py input1=tests/arcs2.txt output1=tests/digraph2.xml
python3 nntask1.py input1=tests/arcs3.txt output1=tests/digraph3.xml
```
В arcs3.txt представлен граф с циклом, поэтому в заданиях 2 и 3 не будет получен результат.
### 2. Создание функции по графу
```
python3 nntask2.py input1=tests/digraph1.xml output1=tests/prefix_func1.txt
python3 nntask2.py input1=tests/digraph2.xml output1=tests/prefix_func2.txt
python3 nntask2.py input1=tests/digraph3.xml output1=tests/prefix_func3.txt
```

### 3. Вычисление значения функции на графе
```
python3 nntask3.py input1=tests/digraph1.xml input2=tests/operations1.txt output1=tests/func_value1.txt
python3 nntask3.py input1=tests/digraph2.xml input2=tests/operations2.txt output1=tests/func_value2.txt
python3 nntask3.py input1=tests/digraph2.xml input2=tests/operations3.txt output1=tests/func_value3.txt
```
Первый граф ($5 * 5 + e^{3 * 9}$):

![](https://github.com/unins000exe/NI/blob/main/img/wtest1.png)

Второй граф ($e^{3 * 1 + 2}$):

![](https://github.com/unins000exe/NI/blob/main/img/wtest2.png)

В последнем тесте у вершины E задана операция $exp$, но она имеет двух родителей (то есть два аргумента), поэтому программа завершает работу с выводом сообщения об ошибке.

### 4. Построение многослойной нейронной сети
```
python3 nntask4.py input1='W.json' input2='X.json' output1='Y.json'
```

### 5. Реализация метода обратного распространения ошибки для многослойной НС
```
# python3 nntask5.py input1='W_xor.json' input2='XY_xor.json' input3='params_xor.json' output1='E_xor.txt'
# python3 nntask5.py input1='W_num.json' input2='XY_num.json' input3='params_num.json' output1='E_num.txt'
```
