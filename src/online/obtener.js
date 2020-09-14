// Packages
const rutify = require('rutificador')

// Search by name
rutify({ name: 'Juán Perez' }).then(juanitos => {
  console.log(juanitos)
})