CREATE OR REPLACE FUNCTION atualizaRisco() RETURNS TRIGGER AS $$
DECLARE reg checkin%rowtype;
BEGIN
    raise notice 'Trigger set %', new.diagnostico_usuario_id_;
    FOR reg IN SELECT *
    FROM checkin WHERE checkin_id_usuario = new.diagnostico_usuario_id_
                       AND DATE(checkin_inicio) < new.diagnostico_data_fim_sintomas
                       AND DATE(checkin_final) > new.diagnostico_data_inicio_sintomas LOOP
        raise notice 'UPDATING RISKS for symptoms';
        UPDATE checkin SET checkin_risco = checkin_risco + 4
        WHERE checkin_local_id_=reg.checkin_local_id_
              AND checkin_inicio < reg.checkin_final
              AND checkin_final > reg.checkin_inicio
              AND checkin_id_usuario <> new.diagnostico_usuario_id_;
    END LOOP;
    FOR reg IN SELECT *
    FROM checkin WHERE checkin_id_usuario = new.diagnostico_usuario_id_
                       AND DATE(checkin_inicio) < new.diagnostico_data_recuperacao
                       AND DATE(checkin_final) > new.diagnostico_data_exame LOOP
        raise notice 'UPDATING RISKS for exam';
        UPDATE checkin SET checkin_risco = checkin_risco + 1
        WHERE checkin_local_id_=reg.checkin_local_id_
              AND checkin_inicio < reg.checkin_final
              AND checkin_final > reg.checkin_inicio
              AND checkin_id_usuario <> new.diagnostico_usuario_id_;
    END LOOP;
RETURN NEW;
END;
$$
LANGUAGE 'plpgsql';

CREATE TRIGGER risco_trigger
AFTER INSERT OR UPDATE ON diagnostico
FOR EACH ROW
EXECUTE PROCEDURE atualizaRisco();