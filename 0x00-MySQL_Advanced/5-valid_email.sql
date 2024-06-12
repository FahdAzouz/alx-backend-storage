-- valid email or not based on change

DELIMITER // ;
CREATE TRIGGER reset
BEFORE INSERT ON users
FOR EACH ROW
BEGIN
  IF NEW.email != OLD.email THEN
    SET NEW.valid_email = 0;
  END IF;
END;//
delimiter ;
