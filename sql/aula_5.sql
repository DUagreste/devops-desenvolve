SELECT *
    FROM vw_cursos_por_categoria
    JOIN categoria ON categoria.nome = vw_cursos_por_categoria.categoria;

    SELECT categoria.id AS categoria_id, vw_cursos_por_categoria
    FROM vw_cursos_por_categoria
    JOIN categoria ON categoria.nome = vw_cursos_por_categoria.categoria;