/** @type {import('tailwindcss').Config} */
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
        'sm': `${1/1.23}rem`,
        'base': '1rem',
        'lg': `1.23rem`,
        'xl': `${1.23*2}rem`,
        '2xl': `${1.23*3}rem`,
        '3xl': `${1.23*4}rem`,
        '4xl': `${1.23*5}rem`,
        '5xl': `${1.23*6}rem`,
        '6xl': `${1.23*7}rem`,
        '7xl': `${1.23*8}rem`,
        '8xl': `${1.23*9}rem`,
        '9xl': `${1.23*10}rem`,
        '10xl': `${1.23*11}rem`,
        '50vh': '50vh',
      }
    },
  },
  plugins: [],
}

