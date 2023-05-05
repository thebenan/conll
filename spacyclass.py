import spacy
from spacy.tokens import Doc


class ConllSpacyClass:
    
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

    
    def fill_lemma_spacy(input_file:str)->str:
        """
        remplit la colonne 3 LEMMA du fichier conllu en utilisant spacy

        input:
            - input_file(str): fichier au format CoNLL-U

        output: 
            str : fichier au format CoNLL-U avec la colonne LEMMA remplie
        """
        nlp = spacy.load("fr_core_news_sm")

        with open(input_file, "r", encoding="utf-8") as f:
            conll_string = f.read()

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
                # crée un objet doc spacy pour le token
                doc = nlp(token[1])
                # obtient le lemme du token et le met dans la colonne LEMMA
                token[2] = doc[0].lemma_
        
        # création de la nouvelle liste de lignes de tokens sous forme de liste
        new_token_lines = []
        for token in token_list:
            # ajout des éléments de la liste de token avec "\t"
            new_token_line = "\t".join(token)
            # djout de la nouvelle ligne de tokens à la liste
            new_token_lines.append(new_token_line)
        # ajout de toutes les lignes de tokens avec un retour à la ligne
        new_conll_string = "\n".join(new_token_lines)

        # retourne la nouvelle string conllu
        return new_conll_string



    def fill_upos_spacy(input_file:str)->str:
        """
        remplit la colonne 4 UPOS du fichier conllu en utilisant spacy

        input:
            - input_file(str): fichier au format CoNLL-U

        output: 
            str : fichier au format CoNLL-U avec la colonne UPOS remplie
        """
        nlp = spacy.load("fr_core_news_sm")

        with open(input_file, "r", encoding="utf-8") as f:
            conll_string = f.read()

        # création de la liste de tokens
        token_lines = conll_string.strip().split("\n")
        token_list = [line.strip().split("\t") for line in token_lines]

        # remplissage de la colonne UPOS
        for token in token_list:
            if token and len(token) == 10:  
                doc = nlp(token[1])  # crée un objet Doc Spacy à partir de la forme du token
                token[3] = doc[0].pos_  # remplace la colonne UPOS avec la catégorie grammaticale universelle du token

        # création de la nouvelle string conllu
        new_token_lines = ["\t".join(token) for token in token_list]
        new_conll_string = "\n".join(new_token_lines)

        # retourne la nouvelle string conllu
        return new_conll_string

    
    
    
    ##################################
    ## pas de XPOS pour le français ##
    ##################################


    
    
    def fill_feat_spacy(input_file:str)->str:
        """
        remplit la colonne 6 FEATS du fichier conllu en utilisant spacy

        input:
            - input_file(str): fichier au format CoNLL-U

        output: 
            str : fichier au format CoNLL-U avec la colonne FEAT remplie
        """
        nlp = spacy.load("fr_core_news_sm")

        with open(input_file, "r", encoding="utf-8") as f:
            conll_string = f.read()

        token_lines = conll_string.strip().split("\n")
        token_list = [line.strip().split("\t") for line in token_lines]

        # remplissage de la colonne FEAT
        for token in token_list:
            if token and len(token) == 10:  # vérification de la longueur de la liste
                doc = nlp(token[1])
                # obtient les traits morpho. du token et le met dans la colonne FEAT
                token[5] = str(doc[0].morph)

        new_token_lines = ["\t".join(token) for token in token_list]
        new_conll_string = "\n".join(new_token_lines)

        # retourne la nouvelle string conllu
        return new_conll_string
    
    

    def fill_head_deprel_spacy(input_file:str,model:str)->str:
        """
        remplit les colonnes HEAD (7) et DEPREL (8) du fichier conllu avec spacy

        input:
            - input_file(str): fichier au format CoNLL-U

        output: 
            str : fichier au format CoNLL-U avec les colonnes HEAD et DEPREL remplies
        """
        nlp = spacy.load(model)
        nlp.tokenizer = ConllSpacyFichierClass.custom_tokenizer(nlp) 


        with open(input_file, "r", encoding="utf-8") as f:
            conll_string = f.read()

        token_lines = conll_string.strip().split("\n")
        token_list = [line.strip().split("\t") for line in token_lines]


        # récupération des dépendances syntaxiques avec spacy
        doc = nlp(" ".join([token[1] for token in token_list]))

        # association de chaque token avec son head et le deprel
        spacy_deps = [(token.i, token.head.i, token.dep_) for token in doc]

        # remplissage des colonnes HEAD et DEPREL
        for i, (token, head, deprel) in enumerate(spacy_deps):
        # Vérifier si l'indice courant est inférieur à la longueur de la liste de tokens
        # et si l'indice de la tête est également inférieur à la longueur de la liste de tokens
            if i < len(token_list) and head < len(token_list):
                if head >= 0:
                    # remplir la colonne HEAD avec l'indice de la tête + 1
                    token_list[i][6] = str(head+1)
                # remplir la colonne DEPREL
                token_list[i][7] = deprel
                # si la colonne 7 (DEPREL) est "ROOT", mettre "0" dans la colonne 6 (HEAD)
                if token_list[i][7] == "ROOT":
                    token_list[i][6] = "0"


        new_token_lines = ["\t".join(token) for token in token_list]
        new_conll_string = "\n".join(new_token_lines)
        
        return new_conll_string




    #######################
    ##    pas de DEPS    ##
    #######################




    
if __name__ == "__main__":
    
    lemtoktok = ConllSpacyClass.fill_lemma_spacy("test_xmltoconll.conllu")
    print(lemtoktok)
    upostoktok = ConllSpacyClass.fill_upos_spacy("test_xmltoconll.conllu")
    print(upostoktok)
    feattoktok = ConllSpacyClass.fill_feat_spacy("test_xmltoconll.conllu")
    print(feattoktok)
    headdeptok = ConllSpacyClass.fill_head_deprel_spacy("test_xmltoconll.conllu")
    print(headdeptok)

    
