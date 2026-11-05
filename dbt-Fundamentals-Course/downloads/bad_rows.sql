-- Appendix A2: bad rows (Lab 4)
insert into raw.orders   values (11, 6, '2026-05-10', 'lost');
insert into raw.payments values (11, 99, 'credit_card', 700);  -- order 99 does not exist
