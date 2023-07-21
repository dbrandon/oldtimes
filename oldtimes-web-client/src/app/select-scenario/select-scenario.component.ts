import { Component, OnInit } from '@angular/core';
import { HeroService } from '../hero.service';
import { Party } from '../obj/party_member';
import { ScenarioInfo } from '../obj/scenario';
import { Router } from '@angular/router';

@Component({
  selector: 'app-select-scenario',
  templateUrl: './select-scenario.component.html',
  styleUrls: ['./select-scenario.component.css']
})
export class SelectScenarioComponent implements OnInit {
  public party: Party = new Party();

  public scenarioList: ScenarioInfo[] = [];

  constructor(private heroService : HeroService,
    private _router: Router) { }

  ngOnInit(): void {
    this.getParty();
    this.getScenarioList();
  }

  getParty() {
    this.heroService.getParty().subscribe(party => this.party = party);
  }

  getScenarioList() {
    this.heroService.getScenarioList().subscribe(list => this.scenarioList = list);
  }

  startScenario(scenario: ScenarioInfo) {
    this.heroService.startScenario(scenario).subscribe(r => {
      this._router.navigateByUrl('/play-scenario');
    })
  }
}
