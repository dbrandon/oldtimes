import { Component, OnInit } from '@angular/core';
import { HeroService } from '../hero.service';
import { Party } from '../obj/party_member';

@Component({
  selector: 'app-select-scenario',
  templateUrl: './select-scenario.component.html',
  styleUrls: ['./select-scenario.component.css']
})
export class SelectScenarioComponent implements OnInit {
  public party: Party = new Party();

  constructor(private heroService : HeroService) { }

  ngOnInit(): void {
    this.getParty()
  }

  getParty() {
    this.heroService.getParty().subscribe(party => this.party = party);
  }

}
