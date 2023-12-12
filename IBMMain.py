class Livro:
    def __init__(self, titulo, autor, exemplaresDisponiveis):
        self.titulo = titulo
        self.autor = autor
        self.exemplaresDisponiveis = exemplaresDisponiveis

class CatalogoLivros:
    def __init__(self):
        self.catalogo = []

    def cadastrarLivro(self, titulo, autor, exemplares):
        novo_livro = Livro(titulo, autor, exemplares)
        self.catalogo.append(novo_livro)
        print(f"O livro '{titulo}' foi cadastrado com sucesso!")

    def pesquisarLivro(self, termo):
        resultados = []
        for livro in self.catalogo:
            if termo.lower() in livro.titulo.lower() or termo.lower() in livro.autor.lower():
                resultados.append((livro.titulo, livro.autor, livro.exemplaresDisponiveis))
        return resultados

catalogo = CatalogoLivros()

livros = [
    Livro("Python for Beginners", "John Smith", 5),
    Livro("Intro to Data Science", "Emily Johnson", 3),
    Livro("Advanced Python", "Alice Brown", 0),
    Livro("Learning Python", "Mark Lutz", 7),
    Livro("Python Cookbook", "David Beazley", 4),
    Livro("Making the IBM PC", "Mark Dean", 3),
    Livro("The Dictionary", "Various Authors", 6),
    Livro("Art: A Visual History", "Robert Cumming", 2),
    Livro("The Art Book", "Phaidon Press", 5),
    Livro("Encyclopedia of Artists", "Jane Turner", 3),
    Livro("The Complete Works of Shakespeare", "William Shakespeare", 8),
    Livro("A Brief History of Time", "Stephen Hawking", 4),
    Livro("Sapiens: A Brief History of Humankind", "Yuval Noah Harari", 6),
    Livro("Brotopia: Breaking Up the Boys' Club of Silicon Valley", "Emily Chang", 5),
    Livro("Inferior: How Science Got Women Wrong", "Angela Saini", 3),
    Livro("Algorithms of Oppression: How Search Engines Reinforce Racism", "Safiya Umoja Noble", 4)
]


for livro in livros:
    catalogo.cadastrarLivro(livro.titulo, livro.autor, livro.exemplaresDisponiveis)

print("Bem-vindo à livraria 'Gato Sem Rabo'!")

while True:
    escolha = input("Digite 'cadastrar' para adicionar um novo livro ou 'buscar' para pesquisar um livro: ")

    if escolha.lower() == 'cadastrar':
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o nome do autor: ")
        exemplares = int(input("Digite a quantidade de exemplares disponíveis: "))

        while exemplares <= 0:
            exemplares = int(input("Digite uma quantidade válida de exemplares (maior que zero): "))


        catalogo.cadastrarLivro(titulo, autor, exemplares)
    elif escolha.lower() == 'buscar':
        termoBusca = input("Digite o termo de busca: ")
        resultadosPesquisa = catalogo.pesquisarLivro(termoBusca)
        if resultadosPesquisa:
            print(f"Resultados da pesquisa para '{termoBusca}':")
            for resultado in resultadosPesquisa:
                print(f"Título: {resultado[0]}, Autor: {resultado[1]}, Disponíveis: {resultado[2]}")
        else:
            print(f"Nenhum resultado encontrado para '{termoBusca}'.")
    else:
        print("Opção inválida. Tente novamente.")