import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TeacherdashbaoardComponent } from './teacherdashbaoard.component';

describe('TeacherdashbaoardComponent', () => {
  let component: TeacherdashbaoardComponent;
  let fixture: ComponentFixture<TeacherdashbaoardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TeacherdashbaoardComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TeacherdashbaoardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
