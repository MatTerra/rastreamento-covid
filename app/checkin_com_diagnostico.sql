CREATE OR REPLACE VIEW checkin_com_sintomas AS
    SELECT checkin_id_, checkin_local_id_, checkin_inicio, checkin_final FROM diagnostico
        LEFT JOIN checkin ON checkin_id_usuario = diagnostico_usuario_id_
                             AND DATE(checkin_inicio) < diagnostico_data_fim_sintomas
                             AND DATE(checkin_final) > diagnostico_data_inicio_sintomas;

CREATE OR REPLACE VIEW checkin_com_diagnostico AS
    SELECT checkin_id_, checkin_local_id_, checkin_inicio, checkin_final FROM diagnostico
        LEFT JOIN checkin ON checkin_id_usuario = diagnostico_usuario_id_
                             AND DATE(checkin_inicio) < diagnostico_data_recuperacao
                             AND DATE(checkin_final) > diagnostico_data_exame;