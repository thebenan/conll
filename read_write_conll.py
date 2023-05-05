from str_spacy_class import ConllStrSpacyClass



class ReadWriteConll :
    """
    Cette classe contient deux méthodes qui permet de lire et écrire un fichier CoNLL-U.
    """

    def write_conll_file(conll_string: str, output_file: str) -> bool:
        """
        écrit le contenu d'une string au format CoNLL-U dans un fichier

        input:
            - conll_string (str): contenu du fichier CoNLL-U
            - output_file (str): nom du fichier de sortie

        output:
            bool: True si l'écriture du fichier a réussi, False sinon
        """
        try:
            with open(output_file, "w") as f:
                f.write(conll_string)
            return True
        except Exception as e:
            print(f"Erreur lors de l'écriture du fichier {output_file}: {e}")
            return False
        
        
    def lire_fichier_conllu(nom_fichier:str)->str:
        """
        prend en entrée le nom d'un fichier au format conll-u et retourne une chaîne de caractères
        contenant le contenu de ce fichier

        Args:
            nom_fichier (str): le nom du fichier à lire

        Return:
            str: le contenu du fichier sous forme de chaîne de caractères

        Raises:
            FileNotFoundError: si le fichier n'existe pas
            Exception: si une erreur se produit lors de la lecture du fichier
        """
        try:
            with open(nom_fichier, 'r', encoding='utf-8') as f:
                contenu_fichier = f.read()
        except FileNotFoundError:
            print(f"Le fichier {nom_fichier} n'a pas été trouvé.")
            return None
        except Exception as e:
            print(f"Une erreur est survenue lors de la lecture du fichier {nom_fichier}: {e}")
            return None

        return contenu_fichier

        
        
        
if __name__ == "__main__":
    model = "fr_core_news_sm"
    ReadWriteConll.write_conll_file(ConllStrSpacyClass.fill_head_deprel_str_spacy(conll_str_feat, model),"conll_by_spacy.conllu")
    print(ReadWriteConll.lire_fichier_conllu("conll_by_spacy.conllu"))
