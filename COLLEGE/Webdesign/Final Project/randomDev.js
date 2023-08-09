let randomChoice = [
  "Game Developer",
  "Low-Level System Developer",
  "Data Science Engineer",
  "Web Developer",
  "Mobile Developer",
  "Internet of Things Developer",
];

function getRandom(button) {
  let randomInt = Math.floor(Math.random() * 6);
  let randomDev = randomChoice[randomInt];

  button.innerHTML = randomDev;
}
