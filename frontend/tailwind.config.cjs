/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./index.html', './src/**/*.{js,jsx}'],
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#eff6ff',
          100: '#dbeafe',
          500: '#3b82f6',
          600: '#2563eb',
          700: '#1d4ed8',
        },
        accent: {
          100: '#f5f3ff',
          500: '#8b5cf6',
          600: '#7c3aed',
        },
        surface: '#0f172a',
      },
      boxShadow: {
        soft: '0 18px 40px rgba(15, 23, 42, 0.12)',
      },
      backgroundImage: {
        'hero-grid': 'radial-gradient(circle at top left, rgba(59,130,246,0.15), transparent 35%), radial-gradient(circle at bottom right, rgba(139,92,246,0.18), transparent 35%)',
      },
    },
  },
  plugins: [],
};
