import xml.etree.ElementTree as ET
import re
import spacy



class XmlToConllClass:
    """
    Classe pour gérer les fichiers XML : 
        convertir les fichiers XML au format CoNLL-U
        
    Méthodes :
        - tokenize_xml: tokenisation du fichier XML et retourne une str au format CoNLL-U
        - save_xml_to_conll : écriture de ces tokens dans un fichier CoNLL-U
    """
            
    
    
    def tokenize_xml(xml_file, xpath_formula):
        """
        tokenise le texte contenu dans les éléments XML correspondant à une formule XPath donnée
        en utilisant Spacy et retourne une string au format CoNLL-U représentant les tokens

        input:
            - xml_file: chemin du fichier XML à tokeniser - str
            - xpath_formula: formule XPath pour récupérer les éléments à tokeniser - str

        output: 
            str : au format CoNLL-U représentant les tokens

        """
        # modèle fr Spacy
        nlp = spacy.load("fr_core_news_sm")

        # parse le fichier XML et récupère l'élément racine
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # stockage de la position du premier car dans le texte
        current_offset = 0
        # liste de stockage pour les tokens connlu
        conll_tokens = []

        # parcours chaque élément correspondant à la formule XPath
        for element in root.findall(xpath_formula):
            # recup du texte de l'élément et supprime les espaces en début et fin
            text = element.text.strip()
            # stockage de la position du premier car dans l'élément
            element_offset = current_offset
            # tokenisation avec Spacy
            tokens = nlp(text)

            # parcours des tokens
            for token in tokens:
                # récup du dernier token et vérifie s'il a la propriété "SpaceAfter=No"
                if conll_tokens:
                    last_token = conll_tokens[-1]
                    if "SpaceAfter=No" in last_token[9]:  # si le dernier token est pas suivi d'espace
                        token_start = current_offset  # la position de départ du nouveau token est la même que la fin du dernier token
                    else:
                        token_start = current_offset + 1  # sinon elle est la fin du dernier token + espace
                else:
                    token_start = current_offset  # si la liste des tokens conllu est vide la position de départ est la position actuelle
                token_end = token_start + len(token)  # calcul de la position de fin du token en ajoutant sa longueur à la position de départ

                # détermine si le token est suivi d'un espace
                space_after = 'Yes' if token.whitespace_ else 'No'

                # ajout du token à la liste des tokens conllu avec offset et space after
                conll_tokens.append((
                    len(conll_tokens) + 1,  # ID
                    token.text,  # FORM
                    '_',  # LEMMA
                    '_',  # UPOS
                    '_',  # XPOS
                    '_',  # FEATS
                    '_',  # HEAD
                    '_',  # DEPREL
                    '_',  # DEPS
                    f'SpaceAfter={space_after}|Offset={token_start}',  # MISC
                ))

                # mise à jour de la position du premier car pour le next token
                current_offset = token_end
            # vérifie si l'élément est le dernier correspondant à la formule XPath
            is_last_element = (element == root.findall(xpath_formula)[-1])
            # mise à jour de la position du premier car pour le prochain élément
            current_offset += 1

        # stockage des lignes de tokens conllu
        conll_lines = []

        # parcours chaque token dans la liste des tokens conllu
        for token in conll_tokens:
            # stockage des champs de chaque token conllu
            conll_fields = []
            # parcours chaque champ du token et l'ajoute à la liste des champs de ce token
            for idx, field in enumerate(token, start=1):
                # ajoute le champ avec \t en début de ligne sauf pour le FORM
                if idx == 1:
                    conll_fields.append(str(field))
                else:
                    conll_fields.append("\t" + str(field))
            conll_lines.append("".join(conll_fields))
        conll_string = "\n".join(conll_lines)

        # retourne la string des tokens conllu
        return conll_string

    
    
    
    def save_xml_to_conll(xml_file, xpath_formula, output_file):
        try:
            # tokenisation
            conll_string = tokenize_xml(xml_file, xpath_formula)
        except Exception as e:
            print(f"Une erreur s'est produite lors de la tokenisation XML : {e}")
            return # execution s'arrete s'il y a un erreur

        try:
            # écriture
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(conll_string)
        except Exception as e:
            print(f"L'erreur {e} s'est produite lors de l'écriture des tokens CoNLL-U dans le fichier")
            return

        print(f"Les tokens CoNLL-U ont été écrits dans le fichier {output_file}")



        
if __name__ == "__main__":
    toks = XmlToConllClass.tokenize_xml("test.xml","./sentence")
    XmlToConllClass.save_xml_to_conll("test.xml","./sentence","test_xmltoconll.conllu")
    print(toks)