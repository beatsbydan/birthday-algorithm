import data from "./data.js"

const today = new Date()
const todaysDay = today.getDate()
const todaysMonth = today.getMonth()

for (let userData of data){
    const birthDay = new Date(userData.birthday)
    const day = birthDay.getDate()
    const month = birthDay.getMonth()
    if(day === todaysDay && month + 1 === todaysMonth + 1){
        console.log(`Wish ${userData.name} a happy birthday!`)
    }
}