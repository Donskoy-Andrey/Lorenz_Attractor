# Задание 6: Моделирование аттрактора Лоренца

Необходимо создать итерируемый класс `LorenzAttractor`, который инициализируется тремя аргументами:
- начальное состояние аттрактора -- список из трёх чисел `[x0, xy, z0] : list[float]`
- параметры аттрактора -- список из трёх чисел `[sigma, beta, rho]: list[float]`
- шаг интегрирования -- число `step : float`


Предполагается, что будет создан соответствующий итератор, который при каждом последующием обращении к нему будет возвращать состояние аттрактора через заданный интервал интервал `step`.

## Пример запуска аттрактора:
```python
attractor1 = LorenzAttractor([1,2,3], [10, 8/3, 28], 0.1)
attractor2 = LorenzAttractor([2,8,1], [10, 8/3, 28], 0.1)
for state1, state2 in zip(attractor1, attractor2):
  print(state1, state2)
```
В результате данная программа должна выводить на экран состояния аттракторов в моменты времени `0, 0.1, 0.2, 0.3, ...`.

Замечания:
* Класс `LorenzAttractor` должен иметь метод `__iter__`, возвращающий объект класса `LorenzAttractorIterator`
* Класс `LorenzAttractorIterator` должен иметь метод `__next__`, возвращающий список из трёх чисел, соответствующих состоянию аттрактора
* Для численного интегрирования предлагается использовать класс [scipy.integrate.ode](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.ode.html).

## Результаты отрисовки двух заданных аттракторов:
![att1](https://gitlab.sirius-web.org/students/2022/donskoy.ae/hometasks/task6/-/blob/master/images/Lorenz-Attractor-0.png)
![att2](https://gitlab.sirius-web.org/students/2022/donskoy.ae/hometasks/task6/-/blob/master/images/Lorenz-Attractor-1.png)
