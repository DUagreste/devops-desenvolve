  SELECT aluno.primeiro_nome,
         aluno.ultimo_nome,
		 COUNT(aluno_curso.curso_id) numero_cursos
    FROM aluno
	JOIN aluno_curso ON aluno_curso.aluno_id = aluno.id
GROUP BY 1, 2
ORDER BY numero_cursos DESC
   LIMIT 1;
   
  SELECT curso.nome,
  		 COUNT(aluno_curso.aluno_id) numero_alunos
    FROM curso
	JOIN aluno_curso ON aluno_curso.curso_id = curso.id
GROUP BY 1
ORDER BY numero_alunos DESC
   LIMIT 1;
   
   SELECT categoria
   	 FROM categoria_cursos(
	 		SELECT categoria.nome AS categoria,
	 				COUNT(curso.id) AS numero_cursos
	 			FROM categoria
				JOIN curso ON curso.categoria_id = categoria.id
		 	GROUP BY categoria
		 ) AS categoria_cursos
		 WHERE numero_cursos >=3;
		 
		 
	SELECT categoria.id AS categoria_id, vw_cursos_por_categoria.*
	FROM vw_cursos_por_categoria 
	JOIN categoria ON categoria.nome = vw_cursos_por_categoria.categoria;		 

CREATE VIEW vw_cursos_por_categoria AS SELECT categoria.nome AS categoria,
	 				COUNT(curso.id) AS numero_cursos
	 			FROM categoria
				JOIN curso ON curso.categoria_id = categoria.id
		 	GROUP BY categoria;
			
DROP VIEW vw_cursos_backend;	

SELECT * FROM vw_cursos_backend;

CREATE VIEW vw_cursos_backend AS SELECT nome FROM curso WHERE categoria_id = 2;