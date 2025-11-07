# Документация к geometric_lib

## Math formulas
### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ab/2

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

## Описание функций

### Функция `area` в circle.py

*   **Назначение:** Вычисляет площадь круга
*   **Параметры:**
    *   `r` (int, float): значение радиуса
*   **Возвращаемое значение:** (int, float) Площадь круга.
*   **Пример вызова:**
    ```python
    result = result(5)
    print(result)  # Вывод: 78.53981633974483
    ```

### Функция `area` в square.py

*   **Назначение:** Вычисляет площадь квадрата (по сути ищет квадрат числа)
*   **Параметры:**
    *   `a` (int, float): длина стороны квадрата
*   **Возвращаемое значение:** (int, float) Возвращает квадрат числа
*   **Пример вызова:**
    ```python
    result = area(5)
    print(result)  # Вывод: 25
    ```

### Функция `perimeter` в circle.py

*   **Назначение:** Вычисляет длину дуги окружности
*   **Параметры:**
    *   `r` (int, float): значение радиуса
*   **Возвращаемое значение:** (int, float) Длина дуги окружности.
*   **Пример вызова:**
    ```python
    result = result(5)
    print(result)  # Вывод: 31.41592653589793
    ```


### Функция `perimeter` в square.py

*   **Назначение:** Вычисляет периметр квадрата
*   **Параметры:**
    *   `a` (int, float): длина стороны квадрата
*   **Возвращаемое значение:** (int, float) Периметр квадрата
*   **Пример вызова:**
    ```python
    result = result(5)
    print(result)  # Вывод: 20
    ```


## Общее описание решения
* Каждый файл содержит две функции: для нахождения площади и периметра
* Для нахождения используются формулы, перечисленные в #Math formulas


## Project change history
Хеш коммита | Описание изменения
------------|--------------------
`9964540`   | comments added
`0832dfe`   | comments added
`f21f05e`   | comments added
`776b738`   | was fixed
`09bbd26`   | new file triangle was added
`1051f5f`   | new file rectangle.py was added
