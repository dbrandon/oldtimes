import { Component, OnInit } from '@angular/core';
import { Party } from '../obj/party_member';
import { HeroService } from '../hero.service';
import { Monster } from '../obj/monster';

@Component({
  selector: 'app-play-scenario',
  templateUrl: './play-scenario.component.html',
  styleUrls: ['./play-scenario.component.css']
})
export class PlayScenarioComponent implements OnInit {
  public monsterList: Monster[] = [];
  public party: Party = new Party();
  public messageList: string[] = [];

  constructor(private heroService: HeroService) { }

  ngOnInit(): void {
    this.getScenarioStatus();
    this.getParty();
    this.getMonsters();
  }

  getMonsters() {
    this.heroService.getMonsters().subscribe(list => this.monsterList = list);
  }

  getParty() {
    this.heroService.getParty().subscribe(party => this.party = party);
  }

  getScenarioStatus() {
    this.heroService.getScenarioStatus().subscribe(resp => {
      resp.events.forEach(e => console.log('event text=[' + e.text + ']'))
    })
  }

  attack() {
    this.heroService.simpleAttack().subscribe(list => {
      for(var i = 0; i < list.length; i++) {
        this.messageList.push(list[i]);
      }
      this.getMonsters();
    })
  }
}
