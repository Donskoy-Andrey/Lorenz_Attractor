# Моделирование аттрактора Лоренца
## Постановка задачи:
Необходимо создать итерируемый класс `LorenzAttractor`, который инициализируется тремя аргументами:
- начальное состояние аттрактора - список из трёх чисел `[x0, y0, z0]: list[float]`
- параметры аттрактора - список из трёх чисел `[sigma, beta, rho]: list[float]`
- шаг интегрирования - число `step : float`


Должен быть создан соответствующий итератор, который при каждом последующием обращении к нему будет возвращать состояние аттрактора через заданный интервал интервал `step`.

## Пример запуска аттрактора:
```python
attractor1 = LorenzAttractor([1,2,3], [10, 8/3, 28], 0.1)
attractor2 = LorenzAttractor([2,8,1], [10, 8/3, 28], 0.1)
for state1, state2 in zip(attractor1, attractor2):
    print(state1, state2)
```
В результате данная программа должна выводить на экран состояния аттракторов в моменты времени `0, 0.1, 0.2, 0.3, ...`.

## Примечания:
* Класс `LorenzAttractor` должен иметь метод `__iter__`, возвращающий объект класса `LorenzAttractorIterator`
* Класс `LorenzAttractorIterator` должен иметь метод `__next__`, возвращающий список из трёх чисел, соответствующих состоянию аттрактора
* Для численного интегрирования используется класс [scipy.integrate.ode](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.ode.html).

## Результаты отрисовки двух заданных аттракторов:
![att1](https://github.com/Donskoy-Andrey/LorenzAttractor/blob/master/images/gif/Attractor-1.gif?raw=true)
![att2](https://github.com/Donskoy-Andrey/LorenzAttractor/blob/master/images/gif/Attractor-2.gif?raw=true)
