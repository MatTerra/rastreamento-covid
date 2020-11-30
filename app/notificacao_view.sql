CREATE OR REPLACE VIEW notificacao_view AS
    SELECT checkin_id_, checkin_id_usuario,
           checkin_risco, checkin_inicio, checkin_final
           local_id_, local_nome, notificacao_recebida
    FROM notificacao
        LEFT JOIN checkin ON notificacao_checkin_id_=checkin_id_
        LEFT JOIN local ON local_id_=checkin_local_id_;