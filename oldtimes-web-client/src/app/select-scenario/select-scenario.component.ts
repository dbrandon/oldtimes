import { Component, OnInit } from '@angular/core';
import { HeroService } from '../hero.service';

@Component({
  selector: 'app-select-scenario',
  templateUrl: './select-scenario.component.html',
  styleUrls: ['./select-scenario.component.css']
})
export class SelectScenarioComponent implements OnInit {

  constructor(private heroService : HeroService) { }

  ngOnInit(): void {
    this.getParty()
  }

  getParty() {
    this.heroService.getParty().subscribe(party => {
      console.log('do something with the party!');
    })
  }

}
