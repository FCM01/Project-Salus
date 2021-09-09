import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SecuritysuComponent } from './securitysu.component';

describe('SecuritysuComponent', () => {
  let component: SecuritysuComponent;
  let fixture: ComponentFixture<SecuritysuComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SecuritysuComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SecuritysuComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
