import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PlayScenarioComponent } from './play-scenario.component';

describe('PlayScenarioComponent', () => {
  let component: PlayScenarioComponent;
  let fixture: ComponentFixture<PlayScenarioComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PlayScenarioComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PlayScenarioComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
