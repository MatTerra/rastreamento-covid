CREATE OR REPLACE FUNCTION notifica() RETURNS TRIGGER AS $$
DECLARE checkins INT;
BEGIN
    SELECT INTO checkins count(notificacao_checkin_id_) FROM notificacao
    WHERE notificacao_checkin_id_=new.checkin_id_;
    IF (new.checkin_risco > 5 AND checkins = 0) THEN
        INSERT INTO notificacao (notificacao_checkin_id_)
        VALUES (new.checkin_id_);
    END IF;
RETURN NEW;
END;
$$
LANGUAGE 'plpgsql';


CREATE TRIGGER risco_trigger
AFTER INSERT OR UPDATE ON checkin
FOR EACH ROW
EXECUTE PROCEDURE notifica();