--task 10 create function
DELIMITER //;
CREATE FUNCTION SafeDiv (a INTEGER, b INTEGER) RETURNS INT
DETERMINISTIC
BEGIN
  DECLARE result FLOAT;
  IF b == 0 THEN
    RETURN 0;
  END IF;
  SET result = (a * 1.0) / b
  RETURN result;
END;//
delimiter ;
