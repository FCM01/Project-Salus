import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DomesticeditComponent } from './domesticedit.component';

describe('DomesticeditComponent', () => {
  let component: DomesticeditComponent;
  let fixture: ComponentFixture<DomesticeditComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DomesticeditComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DomesticeditComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
