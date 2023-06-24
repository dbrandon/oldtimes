import { HttpClient } from '@angular/common/http';
import { Location } from '@angular/common';

import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HeroService } from '../hero.service';

@Component({
  selector: 'app-hero-add',
  templateUrl: './hero-add.component.html',
  styleUrls: ['./hero-add.component.css']
})
export class HeroAddComponent implements OnInit {

  heroName = '';

  constructor(
    private service: HeroService,
    private location: Location,
    private _router: Router) { }

  ngOnInit(): void {
  }

  goBack() {
    this.location.back();
  }

  save() {
    this.service.createHero(this.heroName)
        .subscribe(rr => this._router.navigate(['heroes']));
  }
}
