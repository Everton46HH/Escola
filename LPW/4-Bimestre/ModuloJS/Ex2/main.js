// import { func} from './func.js' 
// import { constante } from './const.js'

(async() => {
    const {func} = await import('./func.js')

    const { constante } = await import ("./const.js")

    console.log(func("Everton"));
    console.log(constante);     
})();