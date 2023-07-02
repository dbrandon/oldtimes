import { Component, Input, OnInit } from '@angular/core';
import { Party } from '../obj/party_member';

@Component({
  selector: 'app-party-info',
  templateUrl: './party-info.component.html',
  styleUrls: ['./party-info.component.css']
})
export class PartyInfoComponent implements OnInit {

  @Input() party?: Party;

  ngOnInit(): void {
  }

}
