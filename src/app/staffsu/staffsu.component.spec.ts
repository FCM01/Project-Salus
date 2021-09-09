import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StaffsuComponent } from './staffsu.component';

describe('StaffsuComponent', () => {
  let component: StaffsuComponent;
  let fixture: ComponentFixture<StaffsuComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ StaffsuComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(StaffsuComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
