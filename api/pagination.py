from flask import request, url_for

'''
    este é o modulo de paginação, para evitar de exibir todos os registros de uma vez.
    - é preciso criar o link next, que ira verificar se existe uma proxima pagina e ira exibi-la,
    caso não haja ele traz a ultima pagina com registros.
    - tambem o link prev para verificar se ha registros em paginas anteriores e conseguir voltar
    de pagina.
    - por fim o metodo return que ira retornar os links serializados
    Seguindo, é só aplicar a paginação
'''

def pagination(model, schema):
    page = int(request.args.get('page', 1))

    # configura quantidade de objetos na pagina
    per_page = int(request.args.get('per_page', 3))
    page_obj = model.query.paginate(page=page, per_page=per_page)

    # proxima pagina
    next = url_for(
        request.endpoint,
        page=page_obj.next_num if page_obj.has_next else page_obj.page,
        per_page=per_page,
        **request.view_args
    )

    # pagina anterior
    prev = url_for(
        request.endpoint,
        page=page_obj.prev_num if page_obj.has_prev else page_obj.page,
        per_page=per_page,
        **request.view_args
    )

    return {
        'total': page_obj.total,
        'pages': page_obj.pages,
        'next': next,
        'prev': prev,
        'results': schema.dump(page_obj.items) #schema.dump para serializar os dados em json
    }