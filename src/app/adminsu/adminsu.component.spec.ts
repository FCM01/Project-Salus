import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdminsuComponent } from './adminsu.component';

describe('AdminsuComponent', () => {
  let component: AdminsuComponent;
  let fixture: ComponentFixture<AdminsuComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AdminsuComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AdminsuComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
