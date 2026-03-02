const grid = document.getElementsByClassName("grid")[0] 
const startButton = document.getElementById("start")
const score = document.getElementById("score")
let squares = []
let currentSnake = [2,1,0]
let direction = 1
let gridWidth = 10

function createGrid() {
    //lager 100 av firkantene med en for-løkke
    for (let i = 0; i < 100; i++) {
        //lager element 'square'
        const square = document.createElement('div')
        //legger til styling for firkantene
        square.classList.add('square')
        //legger til firkant i grid-en
        grid.appendChild(square)
        //lagrer firkantene til en ny tabell
        squares.push(square)
    }
}
createGrid()

currentSnake.forEach(index => squares[index].classList.add('snake'))

function move() {
    //fjerner siste element/firkant i currentSnake tabellen
    const tail = currentSnake.pop()
    //fjerner styling fra siste element/firkant
    squares[tail].classList.remove('snake')
    //legger til firkanter i retningen slangen flytter seg
    currentSnake.unshift(currentSnake[0] + direction)   
    //legger til styling til de nye firkantene
    squares[currentSnake[0]].classList.add('snake')
}
move()
const timerId = setInterval(move, 1000)

function control(e) {
  // Use string values for the 'e.key' property for modern compatibility
  if (e.key === 'ArrowRight') {
    console.log('right pressed');
    direction = 1
  } else if (e.key === 'ArrowUp') {
    console.log('up pressed');
    direction = -gridWidth
  } else if (e.key === 'ArrowLeft') {
    console.log('left pressed');
    direction = -1
  } else if (e.key === 'ArrowDown') {
    console.log('down pressed');
    direction = +gridWidth
  }
}

// Pass a reference to the function 'control', do not call it with '()'
document.addEventListener('keyup', control);