CREATE OR REPLACE FUNCTION insereRisco() RETURNS TRIGGER AS $$
DECLARE sintomaticos INT;
DECLARE diagnosticados INT;
BEGIN
    raise notice 'Trigger set %', new.checkin_id_usuario;
    SELECT INTO sintomaticos COUNT(checkin_id_)
    FROM checkin_com_sintomas
    WHERE checkin_id_ <> new.checkin_id_
          AND new.checkin_inicio < checkin_final
          AND new.checkin_final > checkin_inicio;
    SELECT INTO diagnosticados COUNT(checkin_id_)
    FROM checkin_com_diagnostico
    WHERE checkin_id_ <> new.checkin_id_
          AND new.checkin_inicio < checkin_final
          AND new.checkin_final > checkin_inicio;
    new.checkin_risco := new.checkin_risco + (4*sintomaticos);
    new.checkin_risco := new.checkin_risco + (1*diagnosticados);

    SELECT INTO sintomaticos COUNT(checkin_id_)
    FROM checkin_com_sintomas
    WHERE checkin_id_ == new.checkin_id_;
    IF (sintomaticos <> 0) THEN
        UPDATE checkin SET checkin_risco = checkin_risco+4
        WHERE checkin_id_ <> new.checkin_id_
              AND checkin_inicio < new.checkin_final
              AND checkin_final > new.checkin_inicio;
    END IF;

    SELECT INTO diagnosticados COUNT(checkin_id_)
    FROM checkin_com_diagnostico
    WHERE checkin_id_ == new.checkin_id_;
    IF (diagnosticados <> 0) THEN
        UPDATE checkin SET checkin_risco = checkin_risco+1
        WHERE checkin_id_ <> new.checkin_id_
              AND checkin_inicio < new.checkin_final
              AND checkin_final > new.checkin_inicio;
    END IF;
RETURN NEW;
END;
$$
LANGUAGE 'plpgsql';

CREATE TRIGGER risco_checkin_insert_trigger
BEFORE INSERT ON checkin
FOR EACH ROW
EXECUTE PROCEDURE insereRisco();