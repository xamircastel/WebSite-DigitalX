# Dockerfile para Cloud Run - Digital-X Website
# Multi-stage build optimizado para producción

# Stage 1: Build
FROM node:20-alpine AS builder

WORKDIR /app

# Copiar archivos de dependencias
COPY package*.json ./

# Instalar dependencias
RUN npm ci

# Copiar código fuente
COPY . .

# Build de producción
RUN npm run build

# Stage 2: Production
FROM nginx:alpine AS production

# Copiar configuración de nginx optimizada
COPY nginx.conf /etc/nginx/nginx.conf

# Copiar archivos estáticos del build
COPY --from=builder /app/dist /usr/share/nginx/html

# Exponer puerto (Cloud Run usa 8080 por defecto)
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:8080/ || exit 1

# Iniciar nginx
CMD ["nginx", "-g", "daemon off;"]