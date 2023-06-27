import { Component, OnInit } from '@angular/core';
import { HeroService } from './hero.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'Old Times Web Client';
  username?: string;

  constructor(private heroService : HeroService) {}

  ngOnInit(): void {
    
    this.getUsername()
  }

  getUsername() {
    this.heroService.getUsername().subscribe(name => this.username = name);
  }

}
