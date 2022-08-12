const numberGrade = number(prompt("Enter your grade: "))

const gradeTable = {
    "10" : "A",
    "9" : "B",
    "8" : "C",
    "7" : "D",
}
// no floor division in JS
const key = Math.floor(numberGrade / 10)

let letterGrade = gradeTable[String(key)]

if(letterGrade == undefined) {
    letterGrade = "F"
}


// string literal, serves same functionality as f-string in python
console.log(`You got a(n) ${letterGrade}`)
