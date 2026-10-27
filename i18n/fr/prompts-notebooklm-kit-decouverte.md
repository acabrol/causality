# Causality — prompts NotebookLM pour le kit découverte

Prompts prêts à copier pour créer une présentation de découverte, une vidéo teaser et une infographie boutique autour de **Protocole Fièvre de Verre**.

## Sources à charger dans NotebookLM

Créer un notebook dédié aux contenus publics et importer d’abord :

1. [Source NotebookLM française — Causality et Protocole Fièvre de Verre](./source-notebooklm-presentation.md) : source de contenu principale, rédigée pour une présentation sans révélation.
2. [Univers et System](./univers-et-system.md) : complément sur le fonctionnement fictionnel du System et la référence visuelle au fluide.
3. Le PDF de référence graphique, s’il est disponible dans vos fichiers, comme source séparée.
4. Le fichier Markdown de charte visuelle, s’il s’agit d’un document distinct, comme source séparée.

**Ne pas importer** [l’annexe confidentielle](./source-notebooklm-annexe-confidentielle.md) ni les préparations MJ pour une présentation publique : elles contiennent des révélations. La source NotebookLM principale résume déjà le scénario sans en dévoiler la solution.

### Direction visuelle trouvée dans le dépôt

Aucun PDF ni fichier distinct nommé « charte visuelle » n’est présent dans le dépôt au moment de la rédaction. La source principale contient toutefois une direction visuelle explicitement marquée comme **piste créative, pas comme charte graphique définitive** : enquête documentaire et fragilité du verre, dossiers et encre d’archive, lumière froide, surfaces cristallines et fils reliant les faits ; Toulouse comme ancrage ; ivoire papier, bleu nuit, cyan pâle, ambre pour les branches ouvertes, rouge pour les conflits et vert discret pour les merges réussis. Pour une déclinaison fidèle à une charte approuvée, ajoutez le PDF et le Markdown concernés aux sources avant de générer.

## Réglages et longueur des champs

Les réglages documentés par Google NotebookLM distinguent les options de chaque création. Les pages d’aide ne donnent pas de plafond officiel en caractères pour le champ de personnalisation. Les prompts ci-dessous sont donc volontairement compacts, conçus pour tenir dans un champ unique sans prétendre à une limite technique fixe. Si l’interface affiche une limite, gardez le premier paragraphe de chaque prompt et raccourcissez les détails visuels.

| Création | Réglages à choisir | À savoir |
|---|---|---|
| Diaporama découverte | Langue française ; **Detailed Deck** si le PDF doit se lire seul, ou **Presenter Slides** pour une présentation orale ; longueur **Long** ; demandez un format de page portrait dans le prompt. | Les réglages documentés sont le type, la langue et la longueur. La documentation ne garantit pas un format A4 portrait pour les diapositives : vérifiez le PDF exporté et ajustez la mise en page après export si nécessaire. |
| Vidéo teaser | Format **Cinematic** pour une expérience immersive, si disponible ; sinon **Short** pour une vidéo d’environ 60 secondes. Langue française si l’option est proposée. Activez la relecture des notes du producteur si l’interface la propose. | La documentation actuelle indique que le format Cinematic ne prend en charge que l’anglais. Pour un teaser narré en français, privilégiez Short ou Explainer en français et demandez un traitement visuel immersif. Le style visuel personnalisable peut ne pas être proposé avec Cinematic ou Short. |
| Infographie boutique | Langue française ; orientation **Portrait** ; niveau de détail **Concise** ou **Standard** ; style visuel adapté (par exemple Professional ou Custom). | NotebookLM exporte l’infographie en PNG. « Portrait » ne garantit pas à lui seul les dimensions imprimables A4 : vérifiez le cadrage et la résolution avant impression. |

Ces options et limites fonctionnelles peuvent évoluer. Il n’y a pas de durée garantie par le prompt pour une vidéo Cinematic ; la durée d’environ 60 secondes correspond à l’option Short indiquée dans l’aide. Les contenus générés peuvent contenir des erreurs : relisez noms propres, faits, orthographe, visuels et narration avant diffusion.

## 1. Diaporama A4 portrait — kit de découverte

**Réglages conseillés :** Detailed Deck, français, Long. Demander une mise en page A4 portrait dans le prompt ; vérifier le PDF obtenu avant impression. Pour accompagner une présentation orale, choisir Presenter Slides et garder les notes orales dans le prompt.

```text
Crée en français un kit de découverte de Causality de 8 pages, destiné à des éditeurs, partenaires potentiels et futurs joueurs. Format visuel A4 portrait, une idée forte par page, titres courts, texte lisible à l’impression, marges généreuses et hiérarchie nette. Ouvre sur Toulouse en 2142 et Protocole Fièvre de Verre : une maladie cristallise les poumons, les archives se contredisent, l’équipe doit enquêter sans détruire le présent qui rend sa mission possible. Explique ensuite le jeu coopératif (2 à 5 joueurs et un maître de jeu), le System, les Branch, le Merge, les dés comme capsules d’énergie noire et le poids cognitif des branches non intégrées. Termine par ce qui existe, le statut de conception et une invitation à découvrir ou playtester. N’invente ni prix, disponibilité commerciale, date de sortie, équipe, chiffres de marché ou financement. Aucun spoiler ni solution du scénario. Direction artistique : enquête d’archives et fragilité du verre, Toulouse, ivoire papier, bleu nuit, cyan pâle ; ambre pour une branche ouverte, rouge pour un conflit, vert discret pour un merge. Visuels conceptuels clairement traités comme illustrations, jamais comme photos de matériel réel. Utilise la source principale et les références graphiques jointes ; en cas d’absence de preuve, omets l’affirmation.
```

## 2. Vidéo teaser immersive — Protocole Fièvre de Verre

**Réglages conseillés :** Short en français pour viser environ 60 secondes, avec narration et imagerie immersives. Si seule l’option Cinematic répond à l’intention visuelle, notez que la documentation indique actuellement une narration uniquement en anglais. Dans ce cas, générez avec la langue disponible puis faites vérifier ou refaire la narration en français avant diffusion. Relisez les notes du producteur avant le rendu final lorsqu’elles sont proposées.

```text
Réalise une vidéo teaser immersive en français pour le jeu de rôle Causality, centrée sur Protocole Fièvre de Verre. Vise le format court, autour de 60 secondes si le réglage le permet. Toulouse, 2142 : une maladie de cristallisation pulmonaire a scellé les cités ; des archives portent des horodatages impossibles. Fais entendre une respiration filtrée, le froissement d’un dossier, des dés, puis un tintement de verre. Une équipe d’enquêteurs ouvre le System, remonte une chaîne de causes, agit dans une Branch et tente de fusionner son intervention avec la Main Timeline pour revenir au Now. Chaque action peut sauver une preuve ou fragiliser leur propre réalité ; laisse planer le doute sans révéler la vérité ni la solution. Termine par : « Trouvez le remède. Préservez la réalité. » puis « Causality — jeu coopératif d’enquête causale, 2 à 5 joueurs et un maître de jeu. » Ton tendu, intrigant, humain ; images de dossiers, verre, lumière froide et cartographie causale lisible. Palette : ivoire papier, bleu nuit, cyan pâle, ambre, rouge discret. Pas de gore, de jargon inexpliqué, de faits ajoutés ni de promesse de sortie. Le System et sa science sont fictionnels. Respecte le contenu des sources jointes et protège tous les spoilers.
```

## 3. Infographie portrait — présentoir boutique

**Réglages conseillés :** Portrait, français, Concise pour une lecture à distance ou Standard pour une fiche plus informative. Laisser du vide pour un QR code et les mentions propres à la boutique. Tant que le jeu n’est pas commercialisé, présenter le visuel comme un support de découverte ou de pré-lancement, pas comme une annonce de disponibilité.

```text
Crée une infographie portrait en français, très lisible à quelques mètres, pour faire découvrir Causality dans une boutique spécialisée. Accroche dominante : « Trouvez le remède. Préservez la réalité. » Présente en trois blocs très courts : 1) Toulouse, 2142, sous la Fièvre de Verre ; 2) un jeu de rôle coopératif d’enquête causale où 2 à 5 joueurs et un maître de jeu explorent des Branch ; 3) chaque intervention doit être fusionnée dans un présent cohérent, au risque de perdre une preuve ou de se perdre soi-même. Mets Protocole Fièvre de Verre en avant sans révéler le mystère. Style d’archives d’enquête et verre cristallin, ancrage toulousain, palette ivoire papier, bleu nuit, cyan pâle ; accents ambre, rouge et vert discrets. Grande typographie, contraste élevé, peu de texte, composition verticale, aucun petit paragraphe. Réserve en bas un espace vide clairement délimité pour ajouter ultérieurement le QR code, le prix, le logo de la boutique et l’information de disponibilité ; n’invente aucune URL, aucun prix ni statut de vente. Si le produit n’est pas indiqué comme disponible dans les sources, ajoute une mention neutre « Projet en développement — découvrez le jeu » et n’écris pas « en vente » ou « disponible ». Illustration conceptuelle seulement, pas de boîte, dés ou composants prétendument photographiés. Aucun spoiler. Respecte les sources jointes.
```

## Bonnes pratiques de génération et de finition

- Générer chaque artefact séparément dans le Studio, avec uniquement les sources nécessaires sélectionnées.
- Joindre la charte et le PDF comme **sources** ; résumer dans le prompt les choix visuels prioritaires plutôt que d’y recopier tout le document.
- Pour le diaporama, préciser le public, l’objectif, le nombre de pages, l’orientation demandée, la progression narrative et le niveau de détail. Faire une relecture de cohérence après export PDF.
- Pour la vidéo, choisir explicitement le format et la langue dans les contrôles disponibles ; le prompt seul ne peut pas imposer une option de narration qui n’existe pas dans l’interface.
- Pour l’infographie, choisir portrait dans les réglages et limiter le contenu à trois messages lisibles. Ajouter le QR code, les prix et les mentions légales après génération, depuis les informations validées de la boutique.
- Demander une passe de correction en une seule consigne regroupée : orthographe, noms du jeu, exactitude factuelle, lisibilité, respect des spoilers et cohérence de la palette.
- Vérifier manuellement les textes rendus dans l’image. Pour toute impression ou campagne publique, corriger les erreurs dans un outil de mise en page si NotebookLM ne permet pas un contrôle précis.

## Références NotebookLM

- [Créer un diaporama dans Gemini Notebook](https://support.google.com/gemininotebook/answer/16757456?hl=fr)
- [Créer une infographie dans Gemini Notebook](https://support.google.com/gemininotebook/answer/16758265?hl=fr)
- [Créer des aperçus vidéo dans Gemini Notebook](https://support.google.com/gemininotebook/answer/16454555?hl=fr)
