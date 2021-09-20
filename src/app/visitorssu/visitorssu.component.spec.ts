import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VisitorssuComponent } from './visitorssu.component';

describe('VisitorssuComponent', () => {
  let component: VisitorssuComponent;
  let fixture: ComponentFixture<VisitorssuComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ VisitorssuComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(VisitorssuComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
