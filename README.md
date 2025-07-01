# Bot de Búsqueda de Piezas - Miami Star

Este es un prototipo funcional de un bot web que permite ingresar un número de parte y obtener:
- Descripción del producto
- Medidas estimadas
- Link oficial del fabricante
- Estado simulado de inventario

## Ejecutar localmente

1. Instalar dependencias:
```
pip install -r requirements.txt
```

2. Ejecutar la app:
```
python main.py
```

3. Abrir en navegador:
```
http://localhost:7860
```

## Deploy en Render

1. Crear repositorio en GitHub
2. Conectar cuenta en [https://render.com](https://render.com)
3. Crear un nuevo Web Service
4. Comando de arranque: `gunicorn main:app`