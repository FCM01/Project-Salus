import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ForgetpasswordverifyComponent } from './forgetpasswordverify.component';

describe('ForgetpasswordverifyComponent', () => {
  let component: ForgetpasswordverifyComponent;
  let fixture: ComponentFixture<ForgetpasswordverifyComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ForgetpasswordverifyComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ForgetpasswordverifyComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
