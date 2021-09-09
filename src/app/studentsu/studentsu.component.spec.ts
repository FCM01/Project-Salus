import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StudentsuComponent } from './studentsu.component';

describe('StudentsuComponent', () => {
  let component: StudentsuComponent;
  let fixture: ComponentFixture<StudentsuComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ StudentsuComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(StudentsuComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
