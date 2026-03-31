/** @type {import('tailwindcss').Config} */

const base = 1;
const scale = 1.23;

module.exports = {
  content: ["./templates/**/*.html"],
  theme: {
    extend: {
      colors: {
        'greninja': '#2ab6ca',
        'grey': '#f4f4f4',
        'orange': '#e2642f'
      },
      spacing: {
        '2xs': `${(1/1.23)/1.23/1.23}rem`,
        'xs': `${(1/1.23)/1.23}rem`,
        'sm': `${base*(scale^-1)}rem`,
        'base': `${base}rem`,
        'lg': `${scale*(scale)}rem`,
        'xl': `${base*(scale^2)}rem`,
        '2xl': `${base*(scale^3)}rem`,
        '3xl': `${base*(scale^4)}rem`,
        '4xl': `${base*(scale^5)}rem`,
        '5xl': `${base*(scale^6)}rem`,
        '6xl': `${base*(scale^7)}rem`,
        '7xl': `${base*(scale^8)}rem`,
        '8xl': `${base*(scale^9)}rem`,
        '9xl': `${base*(scale^10)}rem`,
        '10xl': `${base*(scale^11)}rem`,
        '50vh': '50vh',
      }
    },
  },
  plugins: [],
}

