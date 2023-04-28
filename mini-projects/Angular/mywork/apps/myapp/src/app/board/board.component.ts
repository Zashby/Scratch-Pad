import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'mywork-board',
  templateUrl: './board.component.html',
  styleUrls: ['./board.component.scss']
})
export class BoardComponent implements OnInit {

  squares!: any[];
  xIsNext!: boolean;
  winner!: string;

  constructor() { }

  ngOnInit() {
    this.newGame();
  }

  newGame() {
    this.squares = Array(9).fill(null);
    this.winner = null;
    this.xIsNext = true;
  }

  get player() {
    return this.xIsNext ? 'X' : 'O';
  }

  makeMove(idx: number) {
    if (!this.squares[idx]) {
      this.squares.splice(idx, 1, this.player);
      this.xIsNext = !this.xIsNext;
    }

    this.winner = this.calculateWinner();
  }

  compMinMiax(dataArray: [], player: boolean){
    // I may employ a recursive minmax algorithm to determine the best move for a computer player, but I may also be lazy about it and work in Java for a bit.
    return 'nothing'
  }

  calculateWinner() {
    const winningConditions = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [0, 4, 8],
      [2, 4, 6]
    ];

    for (let i = 0; i < winningConditions.length; i++) {
      const [a, b, c] = winningConditions[i];
      if (
        this.squares[a] != null &&
        this.squares[a] === this.squares[b] &&
        this.squares[b] === this.squares[c]
      ) {
        return this.squares[a];
      }


    }
    if (!this.squares.includes(null)){
      return 'Nobody!' ;
    }
     return null;

  }



}