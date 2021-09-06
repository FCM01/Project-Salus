import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RegistercheckComponent } from './registercheck.component';

describe('RegistercheckComponent', () => {
  let component: RegistercheckComponent;
  let fixture: ComponentFixture<RegistercheckComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RegistercheckComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RegistercheckComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
