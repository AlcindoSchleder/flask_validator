Funcionalidade: End Point de insersão de registros dos consulta

    Cenário: Json Inválido
        Dado Um json inválido
        """
        {"score": 1000.0 }
        """
        Quando Enviar o json inválido
        Então Api deve retornar 400 inválido

    Cenário: Json Válido
        Dado Um json Válido
        """
        {"doc_id": "446.367.760-20", "score": 1000.0 }
        """
        Quando Enviar o json válido
        Então Api deve retornar 201 válido
