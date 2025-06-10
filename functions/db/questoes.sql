CREATE TABLE IF NOT EXISTS tb_questoes (
	id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
	zotero_collection_key nvarchar(50) NOT NULL,
	zotero_item_key nvarchar(50) NOT NULL,
	curso nvarchar(500) NOT NULL,
	assunto nvarchar(500) NOT NULL,  
	texto_base nvarchar(5000) NOT NULL,  
	referencia nvarchar(500) NOT NULL, 
	tipo_questao nvarchar(10) NOT NULL,
	nivel_questao nvarchar(10) NOT NULL,
	enunciado nvarchar(5000) NOT NULL,  
	alternativa_1 nvarchar(1000) NOT NULL,  
	alternativa_2 nvarchar(1000) NOT NULL,  
	alternativa_3 nvarchar(1000) NOT NULL,  
	alternativa_4 nvarchar(1000) NOT NULL,  
	alternativa_5 nvarchar(1000) NOT NULL,  
	correta nvarchar(10) NOT NULL,  
	justificativa_1 nvarchar(1000) NOT NULL,  
	justificativa_2 nvarchar(1000) NOT NULL,  
	justificativa_3 nvarchar(1000) NOT NULL,  
	justificativa_4 nvarchar(1000) NOT NULL,  
	justificativa_5 nvarchar(1000) NOT NULL,  
	data_insert date(128) DEFAULT(CURRENT_TIMESTAMP)
);


