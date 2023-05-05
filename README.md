# Projet Python CoNLL-U




## `XmlToConllClass`
La classe `XmlToConllClass` fournit des méthodes qui servent à convertir des fichiers XML en format CoNLL-U. Les fichiers XML sont tokenisés à l'aide de Spacy, puis les tokens sont stockés dans un format CoNLL-U. La classe contient deux méthodes :

### Méthodes

-  `tokenize_xml(xml_file, xpath_formula)`

    Tokenise le texte contenu dans les éléments XML correspondant à une formule XPath donnée et retourne une string au format CoNLL-U avec les tokens et les informations MISC (SpaceAfter et Offset).

    **Paramètres:**
    xml_file : chemin du fichier XML à tokeniser (str)
    xpath_formula : formule XPath pour récupérer les éléments à tokeniser (str)
    Retourne :
    str : une string au format CoNLL-U 

-   `save_xml_to_conll(xml_file, xpath_formula, output_file)`

    Tokenise un fichier XML avec la méthode tokenize_xml et écrit les tokens CoNLL-U dans un fichier de sortie.

    **Paramètres**
    xml_file : chemin du fichier XML à tokeniser (str)
    xpath_formula : formule XPath pour récupérer les éléments à tokeniser (str)
    output_file : chemin du fichier de sortie (str)
    Retourne :
    Aucune valeur de retour. Si une erreur se produit lors de la tokenisation ou de l'écriture, un message d'erreur est affiché.


## `ConllStrSpacyClass`

La classe `ConllStrSpacyClass` permet de remplir les colonnes du format CoNLL-U en utilisant Spacy. La classe est contient des méthodes pour remplir les colonnes LEMMA, UPOS, FEAT, HEAD et DEPREL ainsi qu'une méthode qui permet d'écrire nu fichier CoNLL-U avec les colonnes remplies.

### Méthodes

-   `fill_lemma_str_spacy(conll_string: str, model: str) -> str:`
    
    Remplit la colonne 3 (LEMMA) du format CoNLL-U en utilisant Spacy.
    
    **Paramètres:**
    conll_string : string au format CoNLL-U (str)
    model : nom du modèle spacy
    Retourne :
    contenu du fichier au format CoNLL-U avec la colonne LEMMA remplie (str)


-   `fill_upos_str_spacy(conll_string: str, model: str) -> str:`
    
    La méthode "fill_upos_str_spacy" remplit la colonne 4 (UPOS) du format CoNLL-U en utilisant Spacy.

    **Paramètres:**
    conll_string : string au format CoNLL-U (str)
    model : nom du modèle spacy
    Retourne :
    contenu du fichier au format CoNLL-U avec la colonne UPOS remplie (str)

-   `fill_feat_str_spacy(conll_string: str, model: str) -> str:`
   
    La méthode "fill_feat_str_spacy" remplit la colonne 6 (FEAT) du format CoNLL-U en utilisant Spacy.

    **Paramètres:**
    conll_string : string au format CoNLL-U (str)
    model : nom du modèle spacy
    Retourne :
    contenu du fichier au format CoNLL-U avec la colonne FEAT remplie (str)

-   `fill_head_deprel_str_spacy(conll_string: str, model: str) -> str:`
    
    La méthode "fill_head_deprel_spacy" remplit les colonnes 7 et 8 (HEAD et DEPREL) du format CoNLL-U en utilisant Spacy. 

    **Paramètres:**
    conll_string : string au format CoNLL-U (str)
    model : nom du modèle spacy
    Retourne :
    contenu du fichier au format CoNLL-U avec les colonnes HEAD et DEPREL remplies (str)

- `custom_tokenizer(nlp):`
    
    Une fonction lambda qui prend un texte en entrée et renvoie un objet Doc. Cette fonction est utilisée pour faire fonctionner correctement la méthode `fill_head_deprel_spacy` (sinon on constate un décalage sur les données).

    **Paramètres:**
    nlp : objet NLP
    Retourne :
    function: une fonction lambda qui prend un texte en entrée et renvoie un objet Doc





## `ReadWrite`
Cette classe contient deux méthodes qui de lire et écrire un fichier CoNLL-U.

-   `write_conll_file(conll_string: str, output_file: str) -> bool:`
    
    **Paramètres:**
    conll_string : string au format CoNLL-U (str)
    output_file : nom du fichier à écrire (str)
    Retourne :
    True si le fichier a pu être écrit, False sinon

-   `lire_fichier_conllu(nom_fichier:str)->str:`
    
    **Paramètres:**
    nom_fichier : nom du fichier à lire (str)
    Retourne :
    contenu du fichier au format CoNLL-U (str)

