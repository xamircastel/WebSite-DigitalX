# Guía de Contribución - Digital-X Website

## 📋 Resumen del Proyecto

Este proyecto es el sitio web de Digital-X, construido con **Astro 4.x** y **Tailwind CSS**.

---

## 👥 División de Trabajo

### Rama `feature/desktop-improvements` (Vista Desktop/Web)
**Responsable:** Desarrollador 1

**Enfoque:** Pantallas ≥ 768px (tablets y desktop)

### Rama `feature/mobile-improvements` (Vista Mobile)
**Responsable:** Desarrollador 2

**Enfoque:** Pantallas < 768px (móviles)

---

## 🎨 Convenciones de CSS/Tailwind

### Para evitar conflictos, seguir estas reglas:

### Vista Desktop (Desarrollador 1)
Usar clases con prefijos responsivos:
- `md:` - Para tablets (≥768px)
- `lg:` - Para desktop (≥1024px)
- `xl:` - Para pantallas grandes (≥1280px)
- `2xl:` - Para pantallas extra grandes (≥1536px)

**Ejemplo:**
```html
<div class="md:flex-row md:gap-8 lg:px-12">
```

### Vista Mobile (Desarrollador 2)
Usar clases **SIN prefijo** (mobile-first):
- Clases base sin prefijo aplican a mobile
- `sm:` - Para móviles grandes (≥640px) - OPCIONAL

**Ejemplo:**
```html
<div class="flex-col gap-4 px-4 sm:px-6">
```

---

## 📁 Estructura de Archivos

```
website/
├── src/
│   ├── components/
│   │   ├── layout/          # Header, Footer
│   │   └── sections/        # Hero, Products, etc.
│   ├── layouts/
│   ├── pages/
│   └── styles/
│       └── global.css       # ⚠️ ARCHIVO COMPARTIDO
└── public/
```

### Reglas por Archivo

| Archivo | Desktop | Mobile | Notas |
|---------|---------|--------|-------|
| `global.css` | ⚠️ Cuidado | ⚠️ Cuidado | Usar media queries separadas |
| Componentes `.astro` | ✅ Clases `md:`, `lg:` | ✅ Clases base | Mismo archivo, diferentes clases |

---

## 🔧 Modificaciones en `global.css`

Si necesitas agregar estilos personalizados:

### Desktop (Desarrollador 1)
```css
/* === DESKTOP STYLES === */
@media (min-width: 768px) {
  .mi-clase-desktop {
    /* estilos */
  }
}
```

### Mobile (Desarrollador 2)
```css
/* === MOBILE STYLES === */
@media (max-width: 767px) {
  .mi-clase-mobile {
    /* estilos */
  }
}
```

---

## 🚀 Flujo de Trabajo Git

### 1. Antes de empezar a trabajar
```bash
git checkout tu-rama
git pull origin tu-rama
```

### 2. Hacer commits frecuentes
```bash
git add .
git commit -m "Descripción clara del cambio"
git push
```

### 3. Mensajes de commit recomendados
- `[Desktop] Ajuste de espaciado en header`
- `[Mobile] Fix menú hamburguesa`
- `[Desktop] Mejora grid de productos`
- `[Mobile] Optimización hero section`

---

## 🔀 Proceso de Merge

### Orden recomendado:
1. **Primero:** Merge de `feature/desktop-improvements` a `main`
2. **Segundo:** Merge de `feature/mobile-improvements` a `main`

### Si hay conflictos:
1. El segundo en hacer merge resuelve los conflictos
2. Para clases Tailwind en el mismo elemento: **combinar ambas clases**
3. Para `global.css`: mantener ambos bloques de media queries

---

## 🛠️ Comandos Útiles

### Iniciar el servidor de desarrollo
```bash
cd website
npm install  # Solo la primera vez
npm run dev
```

### Ver el sitio
- Local: http://localhost:4321

### Verificar cambios responsive
- Usar DevTools del navegador (F12)
- Desktop: Probar en viewport ≥ 768px
- Mobile: Probar en viewport < 768px

---

## ⚠️ Reglas Importantes

1. **NO modificar** clases del otro desarrollador
2. **SIEMPRE** hacer pull antes de empezar a trabajar
3. **Commits pequeños** y frecuentes
4. **Comunicarse** si necesitas modificar algo compartido
5. **Probar** en ambas vistas antes de hacer push

---

## 📞 Resolución de Dudas

Si tienes dudas sobre qué clases usar o cómo evitar conflictos:
1. Revisa este documento
2. Consulta con tu compañero/a
3. En caso de duda, usa clases con prefijo de tu responsabilidad

---

## 📝 Ejemplo Práctico

### Antes (conflicto potencial):
```html
<!-- Desarrollador 1 modifica -->
<div class="flex gap-8 px-12">

<!-- Desarrollador 2 modifica -->
<div class="flex gap-4 px-4">
```

### Después (sin conflicto):
```html
<!-- Ambos en el mismo elemento -->
<div class="flex gap-4 px-4 md:gap-8 md:px-12">
```

- `gap-4 px-4` → Mobile (Desarrollador 2)
- `md:gap-8 md:px-12` → Desktop (Desarrollador 1)

---

¡Éxito en el desarrollo! 🚀
