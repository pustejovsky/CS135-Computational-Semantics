# CS135 / COSI 135B — Computational Semantics

Course materials for **263COSI-135B-1: Computational Semantics**, Brandeis University,
Fall 2026 — taught by [James Pustejovsky](https://www.cs.brandeis.edu/~jamesp/).

This repository is a preserved export of the course Moodle site
(`moodle.brandeis.edu/course/view.php?id=6309`, exported 21 October 2026). The original
directory layout is kept **exactly as Moodle produced it**, so the whole site can be
browsed offline: open [`index.html`](index.html) in a browser and every section, lecture
and reading links through as it did on Moodle.

---

## Browsing the course

| Entry point | What it is |
| --- | --- |
| [`index.html`](index.html) | The course front page — the full topic outline with links to every item |
| [`about.html`](about.html) | Course summary page |
| `shared/moodle.css` | Moodle's stylesheet, needed for the pages to render properly |
| `overviewfiles/` | The course banner image |

Each course item lives in its own directory named
`<Type>_<Title>_.<Moodle id>`, for example
`File_Lecture_3_--_Predicate_L..._.477415`. Inside each one:

```
File_Lecture_3_--_Predicate_L..._.477415/
├── index.html      # the Moodle page for this item (title, description, link)
└── content/
    └── session03_predicate_logic.pdf   # the actual slides / handout / reading
```

Forum, Assignment, Feedback and External-tool items contain only `index.html`
(their submissions and posts are not part of a content export).

---

## Course outline

### Part I — Meaning as Logic (6 sessions)

Lambda calculus, semantic types, predicate logic, and the compositional treatment of a
fragment of English, up through quantifier scope and monotonicity.

- Lecture 1 — Introduction and Lambda Calculus · `session01_intro_lambda.pdf`
- Details of Lambda Calculus Syntax and de Bruijn Indexing · `session01a_conversions_debruijn.pdf`
- Lecture 2 — Semantic Types · `session02_semantic_types.pdf`
- Lecture 2 — Computational Semantics from the NLP Perspective · `session02alt_nlp_view.pdf`
- Lecture 3 — Predicate Logic · `session03_predicate_logic.pdf`
- The Fragment of English · `session04_fragment.pdf`
- Lecture 5 — Quantifier Scope · `session05_quantifiers_scope.pdf`
- Lecture 5 Extra — Monotonicity · `session05a_monotonicity.pdf`
- Lecture 5 Extra — Negative Polarity Items (NPIs) · `session05b_npi.pdf`
- Lecture 5 Extra — Taking Stock · `session05-positioning.pdf`
- Lecture 6 — Beyond the Sentence · `session06_beyond_sentence.pdf`

Prerequisite review material:

- Linear Algebra Self-assessment · `CS135_LinearAlgebra_SelfAssessment.pdf` (+ answer key)
- Linear Algebra Review Guide · `CS135_LinearAlgebra_ReviewGuide.pdf`
- Haskell Review Companion · `haskell_reference.pdf`

### Part II — Meaning as Distribution (4 sessions)

From count-based vector spaces through SVD and prediction-based embeddings to
contextual representations, alongside the algebra that underlies them.

- Lecture 6 — Linear Algebra Refresher for Formal Semantics · `session05c_la_refresher.pdf`
- Lecture 6 — Types as Vectors · `session06b_types_as_vectors.pdf`
- λ-DCS: Dependency-Based Compositional Semantics · `session06a_lambda_dcs.pdf`
- Lecture 7 — Distributional Semantics · `session07_distributional.pdf`
- Lecture 8 — Reduction and Prediction · `session08_reduction.pdf`
- Reduction II: What the SVD Actually Does · `session08b_svd_geometry.pdf`
- Count-Based NLP · `session08c_count_based_nlp.pdf`
- What the Inner Product Left Out · `session08d_inner_product.pdf`
- Mechanisms of Skipgram with Negative Sampling · `session08e_sgns_mechanics.pdf`
- Prediction — Details of SGNS · `session09_prediction.pdf`
- SVD Word Embeddings: Where Did the Context Matrix Go? · `session09b_where_did_C_go.pdf`
- Contextual Embeddings: Why a Word Should Not Have One Vector · `session09_contextual.pdf`
- Bilinear Maps (updated 11 Oct 2026) · `bilinear_maps.pdf`
- Quiz 1 sample questions, with and without answers

### Part III — The Algebraic Thread and Geometric Algebra (5 sessions)

### Part IV — Functional Geometric Algebra (8 sessions)

### Recitations and labs

- Lab 1: Haskell — setup and basics · `lab_1.html`
- Lab 2: Haskell — data types, function application, higher-order functions · `lab_2.html`
- Recitation 4 — Distributional semantics · `recitation3.pdf`
- Recitation 5 — Why go low-dimensional · `slides.html`
- Recitation 6 — Prelude to VSA · `slides.html`
- Recitation 7 — Quiz 1 review · `slides.html`

### Problem sets

- Problem Set 1 · `Assignment_Problem_Set_1_.478573/`
- Problem Set 2 · `Assignment_Problem_Set_2_.485261/`

### Syllabus

- Course Syllabus · `File_Course_Syllabus_.474050/content/CS135_Fall2026.pdf`

---

## Readings not included

Four items in the Moodle site are third-party copyrighted books. Their `index.html`
pages are preserved so the course structure is unchanged, but the PDFs themselves are
**not** redistributed here (each `content/` directory carries a `NOT_INCLUDED.md` note):

| Reading | Where to get it |
| --- | --- |
| Jurafsky & Martin, *Speech and Language Processing*, 3rd ed. draft | Free from the authors: [web.stanford.edu/~jurafsky/slp3](https://web.stanford.edu/~jurafsky/slp3/) |
| van Eijck & Unger, *Computational Semantics with Functional Programming* | Cambridge University Press, 2010 |
| Lenci & Sahlgren, *Distributional Semantics* | Cambridge University Press, 2023 |
| Dorst, Fontijne & Mann, *Geometric Algebra for Computer Science* | Morgan Kaufmann, 2007 |

Pustejovsky's own review of Lenci & Sahlgren (2024) **is** included.

---

## Licensing

The lecture slides, handouts, problem sets and review guides are course materials by
James Pustejovsky, shared here for students and for reference. They are not placed in
the public domain — please credit the author and the course if you reuse them. The
third-party readings above remain under their publishers' copyright and are excluded
from this repository.
