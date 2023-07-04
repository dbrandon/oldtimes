import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PartyMemberDetailComponent } from './party-member-detail.component';

describe('PartyMemberDetailComponent', () => {
  let component: PartyMemberDetailComponent;
  let fixture: ComponentFixture<PartyMemberDetailComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PartyMemberDetailComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PartyMemberDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
