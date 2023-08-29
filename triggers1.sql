-- a trigger to check if a customer with the same email address already exists in the database
DELIMITER $$
CREATE TRIGGER `check_customer_email_exists` 
BEFORE INSERT ON `user1` 
FOR EACH ROW 
BEGIN
    IF (SELECT COUNT(*) FROM `user1` WHERE `email` = NEW.email) > 0 
    THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'A customer with this email already exists.';
    END IF;
END$$
DELIMITER ;

-- a trigger to prevent the deletion of a customer record if the customer has pending orders
DELIMITER $$
CREATE TRIGGER `prevent_customer_deletion1` 
BEFORE DELETE ON `user1` 
FOR EACH ROW 
BEGIN
    IF (SELECT COUNT(*) FROM `order_1` WHERE `uder_id` = OLD.uder_id AND `Order_Status` = 0) > 0 
    THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'This customer has pending orders and cannot be deleted.';
    END IF;
END$$
DELIMITER ;


