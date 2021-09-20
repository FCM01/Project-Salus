import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DomesticdashboardComponent } from './domesticdashboard.component';

describe('DomesticdashboardComponent', () => {
  let component: DomesticdashboardComponent;
  let fixture: ComponentFixture<DomesticdashboardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DomesticdashboardComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DomesticdashboardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
