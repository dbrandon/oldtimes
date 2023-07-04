import { Component, Input, OnInit } from '@angular/core';
import { PartyMember } from '../obj/party_member';

@Component({
  selector: 'app-party-member-detail',
  templateUrl: './party-member-detail.component.html',
  styleUrls: ['./party-member-detail.component.css']
})
export class PartyMemberDetailComponent implements OnInit {
  @Input() member ?: PartyMember;

  constructor() { }

  ngOnInit(): void {
  }

}
