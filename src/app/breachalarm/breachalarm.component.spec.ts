import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BreachalarmComponent } from './breachalarm.component';

describe('BreachalarmComponent', () => {
  let component: BreachalarmComponent;
  let fixture: ComponentFixture<BreachalarmComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BreachalarmComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(BreachalarmComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
