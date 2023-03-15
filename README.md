# Stonefish

### Сервис определения фишинговых сайтов

### Математическая модель

Есть N анализаторов сайта по различным параметрам, каждый анализатор в результате оценки
дает число 1-100, где 1 - фишинговый сайт 100 - лигитимный сайт. Также анализаторы имеют 
коэффициенты, они умножаются на результат анализатора (число от 1 до 100). Из суммы 
анализаторов складывается общая оценка.

```
result = sum(An * Af)
An - результат анализатора
Af - коэффициент анализатора
```

### TODO:

3) Сделать config через ymal - pyyaml
5) Добавлять анализаторы
