/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}", "./index.html"],
  theme: {
    extend: {
      screens: {
        'xs': '475px',
      },
    }
  },
  plugins: [],
  corePlugins: {
    preflight: true, 
  }
}
