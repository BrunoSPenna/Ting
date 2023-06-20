from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue):
    word_results = []

    for i in range(len(instance)):
        file_info = instance.search(i)
        word_occurrences = []

        for line_number, line in enumerate(file_info["linhas_do_arquivo"], start=1):
            if word.lower() in line.lower():
                word_occurrences.append({"linha": line_number})

        if word_occurrences:
            word_results.append({
                "palavra": word,
                "arquivo": file_info["nome_do_arquivo"],
                "ocorrencias": word_occurrences,
            })

    return word_results


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
