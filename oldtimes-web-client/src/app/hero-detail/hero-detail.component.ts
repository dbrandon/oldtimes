import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Location } from '@angular/common';
import { Hero } from '../hero';
import { HeroService } from '../hero.service';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-hero-detail',
  templateUrl: './hero-detail.component.html',
  styleUrls: ['./hero-detail.component.css']
})
export class HeroDetailComponent implements OnInit {

  @Input() hero?: Hero;

  constructor(
    private route: ActivatedRoute,
    private heroService: HeroService,
    private location: Location,
    private http: HttpClient,
    private _router: Router,
  ) { }

  ngOnInit(): void {
    this.getHero();
  }

  getHero(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.heroService.getHero(id).subscribe(hero => this.hero = hero);
  }

  goBack(): void {
    this.location.back();
  }

  save(): void {
    console.log('save');
    this.http.put('/rest/hero', this.hero)
      .subscribe(rr => {
        console.log('rr=' + rr);
      })
  }

  remove(): void {
    console.log('remove');
    this.http.delete('/rest/hero/' + this.hero?.id)
      .subscribe(rr => this._router.navigate(['heroes']));
  }
}
