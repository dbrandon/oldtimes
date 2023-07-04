import { Component, Input, OnInit } from '@angular/core';
import { Monster } from '../obj/monster';

@Component({
  selector: 'app-monster-detail',
  templateUrl: './monster-detail.component.html',
  styleUrls: ['./monster-detail.component.css']
})
export class MonsterDetailComponent implements OnInit {
  @Input() monster ?: Monster;
  
  constructor() { }

  ngOnInit(): void {
  }

}
