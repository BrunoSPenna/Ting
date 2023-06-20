import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for index in range(len(instance)):
        if path_file == instance.search(index)['nome_do_arquivo']:
            return

    lns = txt_importer(path_file)
    file_info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lns),
        "linhas_do_arquivo": lns
    }

    instance.enqueue(file_info)
    print(file_info)


def remove(instance):
    """Aqui irá sua implementação"""
    if len(instance) == 0:
        print("Não há elementos")
        return

    file_info = instance.dequeue()
    path_file = file_info["nome_do_arquivo"]
    print(f"Arquivo {path_file} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        print(instance.search(position))
    except Exception:
        print('Posição inválida', file=sys.stderr)
