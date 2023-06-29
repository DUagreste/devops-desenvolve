select * from curso;
select * from categoria;

select id from categoria where nome not like '% %';

select curso.nome from curso where categoria_id in (
	select id from categoria where nome like '% de %'
);

  SELECT curso.nome,
         COUNT(aluno_curso.aluno_id) numero_alunos
    FROM curso
    JOIN aluno_curso ON aluno_curso.curso_id = curso.id
GROUP BY 1
     HAVING COUNT(aluno_curso.aluno_id) > 2
ORDER BY numero_alunos DESC;
