import { Component, Input } from '@angular/core';

@Component({
  selector: 'mywork-square',
  template: `<button nbButton hero status='primary' *ngIf="value == null">{{ value }}</button>
  <button nbButton hero status='success' *ngIf="value =='X'" >{{value}}</button>
  <button nbButton hero status='danger' *ngIf="value =='O'" >{{value}}</button>`,
  styles: ['button { width:100%; height: 100%; font-size:4rem;}'],
})
export class SquareComponent {
  @Input() value: 'X' | 'O';
}
