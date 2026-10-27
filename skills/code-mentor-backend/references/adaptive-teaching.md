# Evidence-informed teaching adaptation

Combine stated preferences, concept demands, and observed results. Never classify learners as visual/auditory/kinesthetic. Sequence alone proves no strategy effect; preference or satisfaction proves no learning. General research guides teaching; it does not validate this tutor.

Use [gradual exploration](teaching-exploration.md) from the start and on resumption: variants within normal tasks/reviews, one main aid per block. Ask briefly about clarity only when an aid is new in that context or a sticking point appears. Reuse feedback already given. Check learning in a separate turn. Keep coverage/variants in adaptacion/exploracion.md with the specified template; no new CLI IDs.

## Choose the next step

1. Read accessible preferences/constraints, checkpoint, recent evidence, index, and relevant cards. Use summaries only with known date/source revision; return to the record if stale.
2. For difficulty, first check prerequisites, step size, and instruction clarity. A different explanation alone cannot supply missing foundations.
3. Match aids to content/environment. Provisionally prioritize promising aids with comparable prior evidence; otherwise state that personal evidence is missing. Honor accessibility preferences without scores or diagnosis.
4. Use one idea and one check per turn. Record aid, result, and actual limits; plan new-case transfer and later retrieval. Gradually reduce assistance without hiding errors.
5. If ineffective, change one aid or reduce the step. Never persist for an assumed fixed style. Retain active retrieval/reviews even when rereading feels easier.

| Aid | Suggested use and limitation |
| --- | --- |
| diagram | Show component relationships/flow; use functional diagrams without unnecessary decoration. |
| analogy | Introduce through something familiar; explain limits, then return to code. |
| trace | Follow evaluation, calls, and values; withhold the full exercise solution. |
| worked-example | Reason through another example; remove steps in later practice. |
| comparison | Contrast cases to identify the relevant difference. |
| self-explanation | Ask learners to justify predictions in their own words. |
| retrieval | Recall without materials, then check; failures can guide review. |
| guided-debugging | Use hypotheses, breakpoint/log, and verifiable experiment; never invent execution. |

Combine IDs when needed; never credit a combination's result to individual components. Content, difficulty, prior experience, and order also affect results. Never use speed as the main measure.

## Records and preferences

Use adaptacion/ in the authorized persistent root, outside the skill/public repository. preferencias.md preserves template-based stated preferences and scope; exploracion.md holds variants, feedback, and narrative coverage per teaching-exploration.md; balance.md and graficos/resultados.svg are derived. observaciones.jsonl links strategies to existing evidence IDs in that scope. Read [the adaptation contract](adaptation-contract.md) before running the utility.

Record greater clarity as a declaration, never success. The utility stores no free-text feedback: keep confirmed preferences in preferencias.md; clarity/effort and variants in exploracion.md of the same authorized scope. Never invent modality/aid to fill event fields; missing values leave the observation pending.

The summary separates concept, topic, task type, difficulty, learning/check modalities, activity, assistance, check type, and strategy combination. Groups do not make exercises identical; inspect evidence/context before comparing. Show correct responses/attempts, partial responses, errors, pending items, and actual delay. No global rankings or learning-style percentages. The threshold of 3 attempts and 2 sessions with evaluated attempts is a conservative interface signal, not statistical validation or proof of effectiveness.

## Review and autonomy

At each close, preserve real teaching episodes per session-close.md: stated preferences, aids/combinations, context, results, and failures. Without writing access, include them in the same pending Work batch; saving concepts alone loses observations. Consult this history before choosing aids for recurring difficulty. Manual summaries replace neither mentor_adaptation.py links nor guarantees.

Adapt within tutor mode/current permissions without seeking acceptance of each explanation. Explore relevant variants gradually from the start in normal practice per teaching-exploration.md; avoid continuous experiments. During driving/voice, request no screen, reading, writing, or device interaction. Oral explanation does not demonstrate independent programming.

Use review_due every three sessions; review sooner for difficulty in two different sessions or learner request. Generate summary/chart during review when accessible; disclose insufficient data. Never fill zero observations with examples posing as data. A review observation is not a new session.

Permanent changes require explicit acceptance per improvement-loop.md. propose_improvement supports only its four adjustments; add no strategy IDs to candidate. For other package-rule changes, prepare a skill change and validate after authorization. Preferences/contextual choices alone trigger no permanent improvement.

Without files/Python, offer a traceable manual summary or pending draft with limits; manual writes gain no utility guarantees. No background process, model training, or implicit synchronization.

## Research basis

Consult sources for claims requiring support: learning styles, Clinton-Lisell and Litzinger (2024), doi:10.3389/fpsyg.2024.1428732; techniques, Dunlosky et al. (2013), doi:10.1177/1529100612453266; retrieval, Karpicke and Blunt (2011), doi:10.1126/science.1199327; prior experience, Kalyuga et al. (2003), doi:10.1207/S15326985EP3801_4. Experimental tasks provide no guarantee of learning C# with an LLM.

Check both source_revision and observation_digest against read: adding observations does not increment state.json revision. Regenerate before use if either differs.
