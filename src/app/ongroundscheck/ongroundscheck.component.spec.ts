import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OngroundscheckComponent } from './ongroundscheck.component';

describe('OngroundscheckComponent', () => {
  let component: OngroundscheckComponent;
  let fixture: ComponentFixture<OngroundscheckComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OngroundscheckComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(OngroundscheckComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
