function bottleSong() {
  // code goes here
  numberOfBeer = 99
  while (numberOfBeer >= 1){
    if(numberOfBeer === 1){
      console.log(`${numberOfBeer} bottles of beer on the wall, ${numberOfBeer} bottles of beer.`)
      console.log(`Take one down and pass it around, no more bottles of beer on the wall.`)
      break;
    }
    console.log(`${numberOfBeer} bottles of beer on the wall, ${numberOfBeer} bottles of beer.`)
    numberOfBeer = numberOfBeer -1
    console.log(`Take one down and pass it around, ${numberOfBeer} bottles of beer on the wall.`)
  }
    console.log("No more bottles of beer on the wall, no more bottles of beer.")
    console.log("Go to the store and buy some more, 99 bottles of beer on the wall.")
};

bottleSong();
