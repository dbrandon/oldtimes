import { Injectable } from '@angular/core';
import { Hero } from './hero';

import { Observable, map, of, tap, share, Subject, Subscriber, mergeMap } from 'rxjs';
import { MessageService } from './message.service';
import { HttpClient } from '@angular/common/http';
import { Party } from './obj/party_member';

interface HResp {
  heroes: Hero[];
}

interface UsernameResp {
  username: string;
}

interface SimpleResponse {
  ok: boolean,
}
interface PartyResponse extends SimpleResponse {
  party: Party,
}

@Injectable({
  providedIn: 'root'
})
export class HeroService {

  private username?: string;
  private usernameQuery?: Observable<string>;
  private subList : Subscriber<string>[] = [];

  constructor(
    private http: HttpClient,
    private messageService: MessageService) { }

  getUsername() {
    if(this.username != null) {
      return of(this.username);
    }

    if(this.usernameQuery == null) {
      this.usernameQuery = this.http.get<UsernameResp>('/rest/get_authorized').pipe(
        map(resp => resp.username)
      );

      this.usernameQuery.subscribe(resp => {
        this.username = resp;
        this.usernameQuery = undefined;

        for(var sub of this.subList) {
          this.publishUsername(sub);
        }
      });
    }

    return new Observable<string>((subscriber) => {
      if(this.username) {
        this.publishUsername(subscriber);
        return;
      }
      this.subList.push(subscriber);
    });
  }

  private publishUsername(sub: Subscriber<string>) {
    sub.next(this.username);
    sub.complete();
  }

  private afterUsername<RC>(fn: (name:string)=>Observable<RC>): Observable<RC> {
    return this.getUsername().pipe(mergeMap(fn));
  }

  getParty(): Observable<Party> {
    return this.afterUsername(result => this.http.get<PartyResponse>('/rest/party').pipe(
      map(resp => resp.party),
      tap(party => this.log('received party: ' + party.members.length + ' members'))
    ));
  }

  getHeroes(): Observable<Hero[]> {
    return this.afterUsername(result => this.http.get<HResp>('/rest/heroes').pipe(
      map(resp => resp.heroes),
      tap(list => this.log('received list (' + list.length + ') of heroes.'))
    ));
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
