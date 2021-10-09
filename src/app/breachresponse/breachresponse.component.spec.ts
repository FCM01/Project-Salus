import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BreachresponseComponent } from './breachresponse.component';

describe('BreachresponseComponent', () => {
  let component: BreachresponseComponent;
  let fixture: ComponentFixture<BreachresponseComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BreachresponseComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(BreachresponseComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
