import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DomesticsuComponent } from './domesticsu.component';

describe('DomesticsuComponent', () => {
  let component: DomesticsuComponent;
  let fixture: ComponentFixture<DomesticsuComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DomesticsuComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DomesticsuComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
