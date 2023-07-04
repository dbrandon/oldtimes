import { Component, Input, OnInit } from '@angular/core';
import { CreatureStats } from '../obj/creature';

@Component({
  selector: 'app-creature-stat-detail',
  templateUrl: './creature-stat-detail.component.html',
  styleUrls: ['./creature-stat-detail.component.css']
})
export class CreatureStatDetailComponent implements OnInit {
  @Input() stats ?: CreatureStats;

  constructor() { }

  ngOnInit(): void {
  }
}
