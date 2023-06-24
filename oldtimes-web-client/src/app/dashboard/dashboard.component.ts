import { Component, OnInit } from '@angular/core';
import { Hero } from '../hero';
import { HeroService } from '../hero.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  heroes: Hero[] = [];

  constructor(private heroService: HeroService) { }

  ngOnInit(): void {
    this.getHeroes();
    this.heroService.getUsername().subscribe(resp => {
      console.log('username=' + JSON.stringify(resp));
    })
  }

  getHeroes(): void {
    this.heroService.getHeroes().subscribe(heroes => this.heroes = heroes.slice(1, 5));
  }

}
