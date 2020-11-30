CREATE OR REPLACE VIEW checkin_com_sintoma AS
    SELECT local_nome, checkin_inicio, checkin_final, sintoma_descricao FROM checkin
        JOIN caso_sintoma ON caso_sintoma_usuario_id_ = checkin_id_usuario
                                  AND checkin_inicio < caso_sintoma_final
                                  AND checkin_final > caso_sintoma_inicio
        JOIN sintoma ON sintoma_id_=caso_sintoma_sintoma_id_
        JOIN local ON local_id_=checkin_local_id_;