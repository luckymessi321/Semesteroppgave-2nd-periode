const grid = document.getElementsByClassName("grid")[0] 
const startButton = document.getElementById("start")
const score = document.getElementById("score")
let squares = []
let currentSnake = [2,1,0]
let direction = 1
let gridWidth = 10
let appleIndex = 0
let count = 0

function updateScore() {
    count++
    if (score) score.textContent = `${count}`;
}

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
    if (
        (currentSnake[0] >= 90 && currentSnake[0] <= 100 && direction === 10) || // om snake head er på bunnen av grid
        (currentSnake[0] >= 0 && currentSnake[0] <= 9 && direction === -10) || // om snake head er på toppen av grid
        (currentSnake[0] % 10 === 0 && direction === -1) || // om snake head er ved venstre vegg av grid
        (currentSnake[0] % 10 === 9 && direction === 1) || // om snake head er ved høyre vegg av grid
        squares[currentSnake[0] + direction].classList.contains('snake') // om snake crasher i seg selv
    ) {
        clearInterval(timerId)
        direction = 0
    }
    //fjerner siste element/firkant i currentSnake tabellen
    const tail = currentSnake.pop()
    //fjerner styling fra siste element/firkant
    squares[tail].classList.remove('snake')
    //legger til firkanter i retningen slangen flytter seg
    currentSnake.unshift(currentSnake[0] + direction)   
    //legger til styling til de nye firkantene
    // bestemmer hva som skjer om snake spiser et eple
    if (squares[currentSnake[0]].classList.contains('apple')) {
        //fjerner klassen til eplet slik at det ser ut som om det ble spist
        squares[currentSnake[0]].classList.remove('apple')
        //øker snake lengde
        squares[tail].classList.add('snake')
        console.log(tail)
        //legger til en ny firkant i currentSnake slik at halen (tail) følger resten av snake
        currentSnake.push(tail)
        console.log(currentSnake)
        //lager et nytt eple
        generateApple()
        //legger til 1 til scoren
        updateScore()
    }

    squares[currentSnake[0]].classList.add('snake')
}
move()
const timerId = setInterval(move, 1000)

function generateApple () {
    do {
        // generer tilfeldig tall
        appleIndex = Math.floor(Math.random() * squares.length)
    } while (squares[appleIndex].classList.contains('snake'))
    squares[appleIndex].classList.add('apple') 
}
generateApple()

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