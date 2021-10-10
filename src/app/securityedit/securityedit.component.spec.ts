import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SecurityeditComponent } from './securityedit.component';

describe('SecurityeditComponent', () => {
  let component: SecurityeditComponent;
  let fixture: ComponentFixture<SecurityeditComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SecurityeditComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SecurityeditComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
