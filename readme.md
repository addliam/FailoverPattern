# Failover pattern

Implementacion en Python del patron Failover. Demostracion con modulos que generan valores aleatorios en el rango de 1 a 3.

## Recursos

https://aws.amazon.com/es/blogs/networking-and-content-delivery/
three-advanced-design-patterns-for-high-available-applications-using-amazon-cloudfront/

## Prueba de ejecucion

```bash
[A] - El valor es 1
[-] Value: 1
------------------------------
[A] - El valor es 2
[B] - El valor es 3
**** ERROR ****  El valor aleatorio es 2
[-] Value: 1
------------------------------
[B] - El valor es 3
[-] Value: 3
------------------------------
[B] - El valor es 3
[-] Value: 3
------------------------------
[B] - El valor es 2
[-] Value: 2
------------------------------
```

Empieza ejecutandose el modulo A, durante la segunda ejecucion ocurre un error (en el contexto error es que el valor sea 2) y se cambia la ejecucion al modulo B. En las solicitudes posteriores se mantiene en uso el modulo B.
