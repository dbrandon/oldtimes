import { Injectable } from '@angular/core';
import { Hero } from './hero';
import { HEROES } from './mock-heroes';

import { Observable, map, of } from 'rxjs';
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
//    const heroes = of(HEROES);
    this.messageService.add('HeroService: fetched heroes');
    return this.http.get<HResp>('/rest/heroes').pipe(map(resp => {
      console.log('Raw response = ' + JSON.stringify(resp));
      return resp.heroes;
    }));
//return of(HEROES);
//    return heroes;
  }

  getHero(id: number): Observable<Hero> {
    return this.http.get<Hero>('/rest/hero/' + id).pipe(
      map(resp => {
        this.log('Got hero for ID=' + id);
        return resp;
      })
    );
    // const hero = HEROES.find(h => h.id === id)!;
    // this.log(`HeroService: fetched hero id=${id}`);
    // return of(hero);
  }

  private log(message: string) {
    this.messageService.add(message)
  }
}
