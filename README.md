# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain
I chose the domain of Computer Science professor and course reviews at Purdue, as well as a recent controversey that happened at Purdue regarding one of its teachers and his class. This student-generated knowledge is valuable because it highlights critical details like a professor's grading curve, exam style, and lecture slide dependence, which completely dictate a student's day-to-day survival in the major. Official university channels like course catalogs or generic syllabi only provide dry prerequisites and standard descriptions, leaving students blind to the actual teaching quality and workload before enrolling.

---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | RateMyProfessor | Student comments on Jeffery Turkstra, a prominent CS professor at Purdue. | https://www.ratemyprofessors.com/professor/2231495 |
| 2 | r/Purdue | A Purdue University computer science professor, Turkstra, is facing significant backlash for using detection methods to identify and penalize students for using AI assistance on assignments in his CS 240 course. | https://www.reddit.com/r/Purdue/comments/1sngwdx/turkstra_240_and_the_institution_of_purdue/ |
| 3 | yCombinator Hacker News | Students in the Purdue University CS240 course are facing consequences after being caught using AI on assignments, a process believed to involve a tracking system described by professor Jeff Turkstra in his paper, "Tracking Large Class Projects in Real-Time Using Fine-Grained Source Control". | https://news.ycombinator.com/item?id=47814040 |
| 4 | r/Purdue | Following controversy over an AI detection tool that led to mass accusations of academic dishonesty in Purdue University's CS240 course, Professor Jeff Turkstra apologized for the retroactive application of his methodology and nullified the initial ultimatum offered to students. | https://www.reddit.com/r/Purdue/comments/1ss06od/can_someone_explain_the_cs240_drama_to_a_uiuc/ |
| 5 | r/Purdue | Professor Jeff Turkstra is facing significant backlash for using an aggressive and potentially unproven tracking tool to issue mass ultimatums to CS240 students suspected of AI-assisted cheating, creating widespread panic regarding potential expulsion just before the course drop deadline. | https://www.reddit.com/r/Purdue/comments/1snjbdq/what_the_hell/ |
| 6 | r/Purdue | Following the backlash over his aggressive and retroactive use of an unproven AI detection tool, Professor Jeff Turkstra apologized for the stress caused, nullified the coercive self-reporting forms, and limited the tool's application to future assignments, effectively halting the mass internal investigations. | https://www.reddit.com/r/Purdue/comments/1sqsy6x/cs240_lecture_summary/ |
| 7 | r/Purdue | The Reddit post offers advice to incoming Purdue CS students, suggesting that courses like CS240 under Professor Jeff Turkstra are notoriously demanding due to his strict coding standards and aggressive enforcement of academic integrity. | https://www.reddit.com/r/Purdue/comments/alxy1a/some_suggestions_for_incoming_cs_students/ |
| 8 | r/Purdue | The post critiques the instructor's approach to allegations of academic misconduct, arguing that the reliance on algorithmic detection and the use of coercive ultimatums to force confessions undermine the principles of due process and fairness. | https://www.reddit.com/r/Purdue/comments/1sp3s3t/cs240_analysis_from_200_iq_swe/ |
| 9 | r/UIUC | The discussions in the source provided highlight that while students generally agree that AI use in foundational programming courses is problematic, there is significant criticism regarding the professor's coercive handling of the situation and the fairness of using punitive measures to force confessions. | https://www.reddit.com/r/UIUC/comments/1ss0w6d/thoughts_on_purdue_cs240_scandalfiasco/ |
| 10 | r/Purdue | The post captures student skepticism regarding the instructor’s defense of the detection tool, highlighting concerns about the definition of a "low" false positive rate and the reliance on algorithmic methods that students feel fall short of rigorous evidence. | https://www.reddit.com/r/Purdue/comments/1sqqbu6/turkstra_quote_again/ |

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:** 500 characters.

**Overlap:** 100 characters.

**Reasoning:** I decided to use a  500-character window to ensure essential context remains bundled, while a 100-character overlap preserves semantic  continuity between segments. This balance prevents the loss of specific course details while avoiding the dilution of embedding vectors caused by blending unrelated reviews.

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**

**Production tradeoff reflection:**

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**

**How source attribution is surfaced in the response:**

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**

**What the system returned:**

**Root cause (tied to a specific pipeline stage):**

**What you would change to fix it:**

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**

**One way your implementation diverged from the spec, and why:**

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*

**Instance 2**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*
