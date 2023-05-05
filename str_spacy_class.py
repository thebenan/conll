import spacy
from spacy.tokens import Doc


class ConllStrSpacyClass:

    """
    classe permettant de remplir les colonnes  du format CoNLL-U en utilisante spacy

    Attributes:
    ----------
    custom_tokenizer (callable): fonction lambda qui prend un texte en entrée et renvoie un objet Doc,
        cette fonction est utilisée pour faire fonctionner la méthode `fill_head_deprel_spacy`

    Méthodes:
    -------
    fill_lemma_str_spacy(conll_string: str, model: str) -> str:
        remplit la colonne 3 LEMMA du fichier conllu en utilisant spacy
        
    fill_upos_str_spacy(conll_string: str, model: str) -> str:
        remplit la colonne 4 UPOS du fichier conllu en utilisant spacy

    fill_feat_str_spacy(conll_string: str, model: str) -> str:
        remplit la colonne 6 FEAT du fichier conllu en utilisant spacy
    fill_head_deprel_spacy(conll_string: str, model: str) -> str:
        remplit les colonnes HEAD (7) et DEPREL (8) du fichier conllu en utilisant spacy
    """


    
    def custom_tokenizer(nlp):
        """
        FONCTION DE YIMI //// ce n'est pas ma fonction 
        -> utilisé seulement pour faire marcher correctement la fonction `fill_head_deprel_spacy`
            (je n'ai pas trouvé d'autres solutions)
        retourne une fonction lambda qui prend un texte en entrée et renvoie un objet Doc

        Args:
            nlp():  objet de spacy contenant le modèle NLP

        Returns:
            function: une fonction lambda qui prend un texte en entrée et renvoie un objet Doc
        """
        # définition de la fonction lambda qui sera retournée
        # cette fonction prend un texte en entrée et renvoie un objet Doc
        tokenizer = lambda text: (
            # création d'un objet Doc à partir du vocabulaire du modèle NLP (nlp.vocab)
            # et des mots extraits du texte en utilisant la méthode split()
            Doc(nlp.vocab, words=text.split(' '),
            # création d'une liste d'espaces pour chaque mot, en utilisant une liste de longueur
            # égale au nombre de mots extraits du texte, dans laquelle chaque élément est True
            spaces=[True] * len(text.split(' ')))
        )
        # retour de la fonction lambda créée
        return tokenizer
    
    
    def fill_lemma_str_spacy(conll_string: str, model: str) -> str:
        """
        remplit la colonne 3 LEMMA du fichier conllu en utilisant spacy

        input:
            - conll_string (str): string au format CoNLL-U représentant les tokens
            - model (str): nom du modèle spacy à utiliser pour l'analyse syntaxique

        output: 
            str : string au format CoNLL-U représentant les tokens avec la colonne LEMMA remplie
        """
        nlp = spacy.load(model)

        token_lines = conll_string.strip().split("\n")
        # liste de tokens
        token_list = []
        for line in token_lines:
            line = line.strip()
            fields = line.split("\t")
            # ajout de la liste de champs à la liste de tokens
            token_list.append(fields)

        # remplissage de la colonne LEMMA
        for token in token_list:
            # vérification de la longueur de la liste
            if token and len(token) == 10:
                # création d'un objet Doc spacy à partir du token
                doc = nlp(token[1])
                # récupération du lemme du token
                lemma = doc[0].lemma_
                # remplacement du champ LEMMA par le lemme
                token[2] = lemma
        

        # création de la chaîne de caractères CoNLL-U avec les tokens modifiés
        conll_lines = []
        for token in token_list:
            conll_fields = []
            for idx, field in enumerate(token, start=1):
                if idx == 1:
                    conll_fields.append(str(field))
                else:
                    conll_fields.append("\t" + str(field))
            conll_lines.append("".join(conll_fields))
        conll_string = "\n".join(conll_lines)

        return conll_string
    
    
    
    def fill_upos_str_spacy(conll_string: str, model: str) -> str:
        """
        remplit la colonne 4 UPOS du fichier conllu en utilisant spacy

        input:
            - conll_string (str): string au format CoNLL-U représentant les tokens
            - model (str): nom du modèle spacy à utiliser pour l'analyse syntaxique

        output: 
            str : string au format CoNLL-U représentant les tokens avec la colonne UPOS remplie
        """
        nlp = spacy.load(model)

        token_lines = conll_string.strip().split("\n")
        # liste de tokens
        token_list = []
        for line in token_lines:
            line = line.strip()
            fields = line.split("\t")
            # ajout de la liste de champs à la liste de tokens
            token_list.append(fields)

        # remplissage de la colonne POS
        for token in token_list:
            # vérification de la longueur de la liste
            if token and len(token) == 10:
                # création d'un objet Doc spacy à partir du token
                doc = nlp(token[1])
                # récupération du POS du token
                pos = doc[0].pos_
                token[3] = pos

        # création de la chaîne de caractères CoNLL-U avec les tokens modifiés
        conll_lines = []
        for token in token_list:
            conll_fields = []
            for idx, field in enumerate(token, start=1):
                if idx == 1:
                    conll_fields.append(str(field))
                else:
                    conll_fields.append("\t" + str(field))
            conll_lines.append("".join(conll_fields))
        conll_string = "\n".join(conll_lines)

        return conll_string


    ##################################
    ## pas de XPOS pour le français ##
    ##################################
    
    
    
    def fill_feat_str_spacy(conll_string: str, model: str) -> str:
        """
        remplit la colonne 6 FEAT du fichier conllu en utilisant spacy

        input:
            - conll_string (str): string au format CoNLL-U représentant les tokens
            - model (str): nom du modèle spacy à utiliser pour l'analyse syntaxique

        output: 
            str : string au format CoNLL-U représentant les tokens avec la colonne FEAT remplie
        """
        nlp = spacy.load(model)

        token_lines = conll_string.strip().split("\n")
        # liste de tokens
        token_list = []
        for line in token_lines:
            line = line.strip()
            fields = line.split("\t")
            # ajout de la liste de champs à la liste de tokens
            token_list.append(fields)

        # remplissage de la colonne FEAT
        for token in token_list:
            # vérification de la longueur de la liste
            if token and len(token) == 10:
                doc = nlp(token[1])
                # récupération du features du token
                feat = doc[0].morph
                # remplacement du champ FEAT par le features
                token[5] = feat

        # création de la chaîne de caractères CoNLL-U avec les tokens modifiés
        conll_lines = []
        for token in token_list:
            conll_fields = []
            for idx, field in enumerate(token, start=1):
                if idx == 1:
                    conll_fields.append(str(field))
                else:
                    conll_fields.append("\t" + str(field))
            conll_lines.append("".join(conll_fields))
        conll_string = "\n".join(conll_lines)

        return conll_string
    
    
    
    def fill_head_deprel_str_spacy(conll_string: str, model: str) -> str:
        """
        remplit les colonnes HEAD (7) et DEPREL (8) du fichier conllu avec spacy

        input:
            - conll_string(str): contenu du fichier au format CoNLL-U
            - model(str): nom du modèle Spacy à utiliser pour la tokenisation

        output:
            str: contenu du fichier au format CoNLL-U avec les colonnes HEAD et DEPREL remplies
        """
        nlp = spacy.load(model)
        nlp.tokenizer = ConllStrSpacyClass.custom_tokenizer(nlp)

        token_lines = conll_string.strip().split("\n")
        token_list = [line.strip().split("\t") for line in token_lines]

        # récupération des dépendances syntaxiques avec spacy
        doc = nlp(" ".join([token[1] for token in token_list]))

        # association de chaque token avec son head et le deprel
        spacy_deps = [(token.i, token.head.i, token.dep_) for token in doc]

        # remplissage des colonnes HEAD et DEPREL
        for i, (token, head, deprel) in enumerate(spacy_deps):
            # vérifier si l'indice courant est inférieur à la longueur de la liste de tokens
            # et si l'indice de la tête est également inférieur à la longueur de la liste de tokens
            if i < len(token_list) and head < len(token_list):
                if head >= 0:
                    # remplir la colonne HEAD avec l'indice de la tête + 1
                    token_list[i][6] = str(head + 1)
                # remplir la colonne DEPREL
                token_list[i][7] = deprel
                # si la colonne 7 (DEPREL) est "ROOT", mettre "0" dans la colonne 6 (HEAD)
                if token_list[i][7] == "ROOT":
                    token_list[i][6] = "0"

        new_token_lines = ["\t".join(token) for token in token_list]
        new_conll_string = "\n".join(new_token_lines)

        return new_conll_string



    ###################
    ## pas de DEPS  ##
    ##################

    
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



if __name__ == "__main__":
    xml_file = "test.xml"
    xpath_formula = "./sentence"
    conll_string = XmlToConllClass.tokenize_xml(xml_file, xpath_formula)

    model = "fr_core_news_sm"
    conll_string_lemma = ConllStrSpacyClass.fill_lemma_str_spacy(conll_string, model)
    print("\nLa colonne LEMMA remplie : \n\n")
    print(conll_string_lemma)
    
    conll_str_upos = ConllStrSpacyClass.fill_upos_str_spacy(conll_string_lemma, model)
    print("\nLa colonne UPOS remplie : \n\n")
    print(conll_str_upos)
    
    conll_str_feat = ConllStrSpacyClass.fill_feat_str_spacy(conll_str_upos, model)
    print("\nLa colonne FEAT remplie : \n\n")
    print(conll_str_feat)
    
    conll_str_dep = ConllStrSpacyClass.fill_head_deprel_str_spacy(conll_str_feat, model)
    print("\nLes colonnes HEAD et DEPREL remplie : \n\n")
    print(conll_str_dep)
    
    ConllStrSpacyClass.write_conll_file(conll_str_dep,"conll_by_spacy.conllu")

