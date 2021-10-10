import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VisitoreditComponent } from './visitoredit.component';

describe('VisitoreditComponent', () => {
  let component: VisitoreditComponent;
  let fixture: ComponentFixture<VisitoreditComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ VisitoreditComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(VisitoreditComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
