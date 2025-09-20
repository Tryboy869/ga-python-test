
# NEXUS AXION : Validation de Concept - GitHub Actions en Python Pur

Ce repository a été créé pour tester une hypothèse : **l'essence de GitHub Actions peut être "absorbée" en Python pur.**

## Le Concept

L'idée est de démontrer qu'un script Python peut parser, interpréter et exécuter un workflow `.yml` en reproduisant la logique fondamentale de GitHub Actions (jobs, steps, contexts) sans dépendre de l'infrastructure de GitHub.

-   `githubactions.py`: Le prototype du moteur d'absorption.
-   `.github/workflows/test.yml`: Un workflow de référence pour comparer l'exécution réelle.
-   `examples/simple-workflow.yml`: Le fichier de test utilisé par notre moteur Python.
