import { Injectable } from '@angular/core';
import { Hero } from './hero';

import { Observable, map, of, tap, share, Subject } from 'rxjs';
import { MessageService } from './message.service';
import { HttpClient } from '@angular/common/http';

interface HResp {
  heroes: Hero[];
}

@Injectable({
  providedIn: 'root'
})
export class HeroService {

  constructor(
    private http: HttpClient,
    private messageService: MessageService) { }

  getHeroes(): Observable<Hero[]> {
    return this.http.get<HResp>('/rest/heroes').pipe(
      map(resp => resp.heroes),
      tap(list => this.log('recieved list (' + list.length + ') of heroes')),
    );
  }

  createHero(heroName: string) {
    return this.http.post('/rest/hero', heroName).pipe(
      tap(x => this.log('Created hero "' + heroName + '"')),
    );
  }

  deleteHero(id: number) {
    return this.http.delete('/rest/hero/' + id).pipe(
      tap(x => this.log('Deleted hero ID=' + id))
    );
  }

  getHero(id: number): Observable<Hero> {
    return this.http.get<Hero>('/rest/hero/' + id).pipe(
      tap(x => this.log('Retrieved hero for ID=' + id)),
    );
  }

  updateHero(hero: Hero) {
    return this.http.put('/rest/hero', hero).pipe(
      tap(x => this.log('Updated hero ID=' + hero.id)),
    );
  }

  private log(message: string) {
    this.messageService.add('[HeroService]: ' + message);
  }
}
