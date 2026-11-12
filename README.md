# orbit-energy-step-lab

## Français

Mesurer la dérive énergétique des pas orbitaux.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m orbit_energy_step_lab examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Mesurer la dérive énergétique des pas orbitaux : calcul déterministe sur entrées structurées, témoins et cas limites explicites.

### Limites

Modèle borné, données fictives, aucun service ou matériel de production validé. Méthodes classiques ; aucune supériorité SOTA générale ni adoption humaine démontrée.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Measure orbital integration energy drift.

Synthetic data; no network access or secret required.

```sh
python -m orbit_energy_step_lab examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Measure orbital integration energy drift: deterministic computation over structured inputs, explicit witnesses and boundary cases.

### Limits

Bounded model and synthetic data; no production service or hardware validated. Classical methods; no general SOTA superiority or human adoption demonstrated.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Medir deriva energética de integración orbital.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m orbit_energy_step_lab examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Medir deriva energética de integración orbital: cálculo determinista con entradas estructuradas, testigos y casos límite explícitos.

### Límites

Modelo acotado y datos ficticios; ningún servicio ni hardware de producción validado. Métodos clásicos; sin superioridad SOTA general ni adopción humana demostrada.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/req/abcorr.html
- https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.transform.Rotation.html

## Projets voisins / Neighboring projects / Proyectos vecinos

FR : [orbit-hermite-gap-check](https://github.com/gbesse/orbit-hermite-gap-check) est un autre diagnostic du portefeuille. Ici : Mesurer la dérive énergétique des pas orbitaux. Comparaison de périmètres seulement, sans affiliation ni benchmark de supériorité.

EN: [orbit-hermite-gap-check](https://github.com/gbesse/orbit-hermite-gap-check) is a different portfolio diagnostic. Here: Measure orbital integration energy drift. Scope comparison only, no affiliation or superiority benchmark.

ES: [orbit-hermite-gap-check](https://github.com/gbesse/orbit-hermite-gap-check) es otro diagnóstico del portafolio. Aquí: Medir deriva energética de integración orbital. Comparación de alcance, sin afiliación ni benchmark de superioridad.
