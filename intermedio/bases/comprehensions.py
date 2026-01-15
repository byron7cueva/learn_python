sample_articles = [
    {
        "title": "Python logra nuevo éxito",
        "source": {"name": "TechNews"},
        "description": "Gran noticia",
        "category": "Tecnología",
    },
    {
        "title": "Mercado en crisis",
        "source": {"name": "Finance"},
        "description": "Análisis completo",
        "category": "Economía",
    },
    {
        "title": "Nueva tecnología",
        "source": {"name": "TechNews"},
        "description": "Innovación",
        "category": "Tecnología",
    },
    {
        "title": "Deportes hoy",
        "source": {"name": "Sports"},
        "description": "Resultados",
        "category": "Deportes",
    },
    {
        "title": "Política actual",
        "source": {"name": "News"},
        "description": "Actualidad",
        "category": "Política",
    },
    {
        "title": "Ciencia avanza",
        "source": {"name": "Science"},
        "description": "Descubrimientos",
        "category": "Ciencia",
    },
]


def extract_titles_traditional(articles):
    """Extrae solo los tipos usando solo un for"""
    titles = []
    for article in articles:
        titles.append(article["title"])
    return titles


# List comprehension
# De la manera Pythonica
def extract_files(articles):
    """Extrae solo los titulos usando un comprehension"""
    return [article["title"] for article in articles]


def extract_titles_traditional2(articles):
    """Extrae solo los tipos usando solo un for"""
    titles = []
    for article in articles:
        if len(article["title"]) > 10:
            titles.append(article["title"])
    return titles


def extract_files2(articles):
    """Extrae solo los titulos usando un comprehension"""
    return [article["title"] for article in articles if len(article["title"]) > 10]


print(extract_titles_traditional2(sample_articles))
print("=====")
print(extract_files2(sample_articles))


def extract_article_sumaries(articles):
    return {article["title"]: article["description"] for article in articles}


def extract_article_sumaries2(articles):
    return {
        article["title"]: article["description"]
        for article in articles
        if len(article["description"]) > 20
    }


print("=======")
print(extract_article_sumaries2(sample_articles))


def unique_sources_traditional(articles):
    sources = set()
    for article in articles:
        sources.add(article["source"]["name"])
    return sources


def unique_sources(articles):
    return {article["source"]["name"] for article in articles}


print("======")
print(unique_sources_traditional(sample_articles))
print(unique_sources(sample_articles))
