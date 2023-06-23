import { HttpClient } from '@angular/common/http';
import { Location } from '@angular/common';

import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-hero-add',
  templateUrl: './hero-add.component.html',
  styleUrls: ['./hero-add.component.css']
})
export class HeroAddComponent implements OnInit {

  heroName = '';

  constructor(
    private http: HttpClient,
    private location: Location,
    private _router: Router) { }

  ngOnInit(): void {
  }

  goBack() {
    this.location.back();
  }

  save() {
    console.log('save hero ' + this.heroName);
    this.http.post('/rest/hero', this.heroName)
        .subscribe(rr => {
          console.log('response=' + rr);
          this._router.navigate(['heroes'])
        });
  }
}
