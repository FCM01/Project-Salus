import { TestBed } from '@angular/core/testing';

import { SalusloginService } from './saluslogin.service';

describe('SalusloginService', () => {
  let service: SalusloginService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SalusloginService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
