var fiba
var fibb
var temp
function myfib2(thresh) {
  fiba = 1;
  fibb = 1;
  console.log (fiba + ", " + fibb + ", ");
  while(fibb <= 150) {
    temp = fiba + fibb;
    fiba = fibb;
    fibb = temp;
    console.log (fibb + ", ");
  }
  console.log("Break now...\n");
}
myfib2(150)