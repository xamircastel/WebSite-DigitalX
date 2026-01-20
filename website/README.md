# Digital-X Website

Sitio web corporativo de **Digital-X** construido con Astro + Tailwind CSS y desplegado en Google Cloud Run.

🌐 **URL de Producción:** https://digital-x.com.co/

## 🚀 Stack Tecnológico

- **Framework:** [Astro](https://astro.build/) v5.16.11
- **Estilos:** [Tailwind CSS](https://tailwindcss.com/) v4.1.18
- **Servidor:** Nginx Alpine (contenedor Docker)
- **Hosting:** Google Cloud Run
- **CI/CD:** Google Cloud Build

## 📁 Estructura del Proyecto

```text
website/
├── public/              # Assets estáticos (imágenes, iconos, etc.)
├── src/
│   ├── components/      # Componentes reutilizables
│   │   ├── layout/      # Header, Footer, MainLayout
│   │   └── sections/    # Secciones de la página (Hero, About, Products, etc.)
│   ├── pages/           # Páginas del sitio
│   │   ├── index.astro  # Página principal
│   │   └── productos/   # Páginas de productos (LALA AI, VClub, etc.)
│   └── styles/          # Estilos globales
├── Dockerfile           # Configuración de Docker para producción
├── nginx.conf           # Configuración de Nginx optimizada
├── cloudrun.yaml        # Configuración de Cloud Run
└── package.json
```

## 🛠️ Comandos de Desarrollo

| Comando           | Descripción                                      |
| :---------------- | :----------------------------------------------- |
| `npm install`     | Instalar dependencias                            |
| `npm run dev`     | Servidor de desarrollo en `localhost:4321`       |
| `npm run build`   | Construir para producción en `./dist/`           |
| `npm run preview` | Preview del build de producción                  |

## ☁️ Despliegue en Google Cloud Run

### Requisitos Previos

1. [Google Cloud SDK](https://cloud.google.com/sdk) instalado
2. Proyecto GCP configurado: `digital-x-info-web`
3. Docker Desktop (opcional para builds locales)

### Configurar Proyecto GCP

```bash
gcloud config set project digital-x-info-web
```

### Desplegar

```bash
# Construir imagen y subir a Container Registry
gcloud builds submit --tag gcr.io/digital-x-info-web/digitalx-website:latest

# Desplegar a Cloud Run (configuración económica)
gcloud run deploy digitalx-website \
  --image gcr.io/digital-x-info-web/digitalx-website:latest \
  --region us-central1 \
  --platform managed \
  --allow-unauthenticated \
  --min-instances 0 \
  --max-instances 10 \
  --memory 256Mi \
  --cpu 1 \
  --cpu-throttling \
  --timeout 60s \
  --concurrency 80
```

### Configuración de Infraestructura

La configuración está optimizada para **mínimo costo**:

- ✅ **Escala a cero** (`min-instances: 0`) - Sin costo cuando no hay tráfico
- ✅ **CPU Throttling** - CPU se reduce cuando no procesa requests
- ✅ **Memoria mínima** (256Mi) - Suficiente para servir contenido estático
- ✅ **Rate Limiting** en Nginx - Protección básica contra ataques (10 req/s burst 20)
- ✅ **Compresión Gzip** - Reduce ancho de banda

### Dominio Personalizado

El dominio `digital-x.com.co` está mapeado al servicio Cloud Run.

## 🔒 Seguridad

El servidor Nginx incluye:

- Headers de seguridad (X-Frame-Options, X-Content-Type-Options, X-XSS-Protection)
- Rate limiting para prevenir ataques DDoS básicos
- Denegación de acceso a archivos ocultos
- Cache optimizado para assets estáticos

## 📊 Productos

- **LALA AI** - Asistente de IA multi-modelo
- **VClub** - Plataforma de streaming
- **XafraChat** - Chat empresarial
- **HotSimp** - Red social
- **Videntes del Fútbol** - Predicciones deportivas

## 🧹 Mantenimiento

### Limpiar revisiones antiguas

```bash
# Listar revisiones
gcloud run revisions list --service digitalx-website --region us-central1

# Eliminar revisión específica
gcloud run revisions delete [REVISION_NAME] --region us-central1 --quiet
```

### Limpiar imágenes antiguas

Desde la [Consola de GCP](https://console.cloud.google.com/gcr/images/digital-x-info-web), eliminar imágenes no utilizadas en Container Registry.

## 📝 Licencia

© 2026 Digital-X. Todos los derechos reservados.
