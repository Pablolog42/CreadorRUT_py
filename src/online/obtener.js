const infoRut = require('info-rut')

const rut = '9.695.669-k'
infoRut.getPersonByRut(rut).then(console.log).catch(console.error)



//const name = 'pablo leonardo gonzalez aguilera'
//infoRut.getPersonByName(name).then(console.log).catch(console.error)
