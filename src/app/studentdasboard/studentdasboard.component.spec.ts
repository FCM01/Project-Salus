import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StudentdasboardComponent } from './studentdasboard.component';

describe('StudentdasboardComponent', () => {
  let component: StudentdasboardComponent;
  let fixture: ComponentFixture<StudentdasboardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ StudentdasboardComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(StudentdasboardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
