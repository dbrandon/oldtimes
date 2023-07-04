import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { HeroesComponent } from './heroes/heroes.component';
import { HeroDetailComponent } from './hero-detail/hero-detail.component';
import { MessagesComponent } from './messages/messages.component';
import { AppRoutingModule } from './app-routing.module';
import { DashboardComponent } from './dashboard/dashboard.component';
import { HeroAddComponent } from './hero-add/hero-add.component';
import { SelectScenarioComponent } from './select-scenario/select-scenario.component';
import { PlayScenarioComponent } from './play-scenario/play-scenario.component';
import { PartyInfoComponent } from './party-info/party-info.component';
import { CreatureStatDetailComponent } from './creature-stat-detail/creature-stat-detail.component';
import { PartyMemberDetailComponent } from './party-member-detail/party-member-detail.component';
import { MonsterDetailComponent } from './monster-detail/monster-detail.component';

@NgModule({
  declarations: [
    AppComponent,
    HeroesComponent,
    HeroDetailComponent,
    MessagesComponent,
    DashboardComponent,
    HeroAddComponent,
    SelectScenarioComponent,
    PlayScenarioComponent,
    PartyInfoComponent,
    CreatureStatDetailComponent,
    PartyMemberDetailComponent,
    MonsterDetailComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule,
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
