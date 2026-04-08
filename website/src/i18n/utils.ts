import es from './translations/es.json';
import en from './translations/en.json';
import zh from './translations/zh.json';
import hi from './translations/hi.json';
import fr from './translations/fr.json';

const translations: Record<string, Record<string, string>> = { es, en, zh, hi, fr };

export const languages = {
  es: { name: 'Español', flag: '🇪🇸' },
  en: { name: 'English', flag: '🇺🇸' },
  zh: { name: '中文', flag: '🇨🇳' },
  hi: { name: 'हिन्दी', flag: '🇮🇳' },
  fr: { name: 'Français', flag: '🇫🇷' },
};

export type Lang = keyof typeof languages;

export const defaultLang: Lang = 'es';

export function t(lang: Lang, key: string): string {
  return translations[lang]?.[key] || translations[defaultLang]?.[key] || key;
}

export function getLocalizedPath(lang: Lang, path: string): string {
  const cleanPath = path.replace(/^\/(es|en|zh|hi|fr)(\/|$)/, '/');
  if (lang === defaultLang) return cleanPath;
  return `/${lang}${cleanPath}`;
}

export function getLangFromUrl(url: URL): Lang {
  const [, lang] = url.pathname.split('/');
  if (lang in languages) return lang as Lang;
  return defaultLang;
}

export function getProductSlug(lang: Lang): string {
  if (lang === 'en') return 'products';
  if (lang === 'zh') return 'products';
  if (lang === 'hi') return 'products';
  if (lang === 'fr') return 'produits';
  return 'productos';
}

export function getThanksSlug(lang: Lang): string {
  if (lang === 'en') return 'thanks';
  if (lang === 'zh') return 'thanks';
  if (lang === 'hi') return 'thanks';
  if (lang === 'fr') return 'merci';
  return 'gracias';
}

export function formatText(text: string): string {
  return text
    .replace(/<gradient>(.*?)<\/gradient>/g, '<span class="text-gradient">$1</span>')
    .replace(/<green>(.*?)<\/green>/g, '<span class="text-[var(--color-accent-green)] font-semibold">$1</span>')
    .replace(/<pink>(.*?)<\/pink>/g, '<span class="text-[var(--color-accent-pink)]">$1</span>')
    .replace(/<orange>(.*?)<\/orange>/g, '<span class="text-[var(--color-accent-orange)]">$1</span>')
    .replace(/<accent>(.*?)<\/accent>/g, '<span class="text-[var(--color-secondary)]">$1</span>')
    .replace(/<strong>(.*?)<\/strong>/g, '<span class="text-white font-semibold">$1</span>');
}
