import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreatureStatDetailComponent } from './creature-stat-detail.component';

describe('CreatureStatDetailComponent', () => {
  let component: CreatureStatDetailComponent;
  let fixture: ComponentFixture<CreatureStatDetailComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CreatureStatDetailComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CreatureStatDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
