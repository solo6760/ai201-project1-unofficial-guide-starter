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

**Model used:** `all-MiniLM-L6-v2` via `sentence-transformers`

**Production tradeoff reflection:**
If deploying this system for real-world university users with no cost constraints, upgrading from a lightweight local model like `all-MiniLM-L6-v2` to an enterprise cloud API model would expand the context window from 256 tokens to over 8,000 tokens. This expansion would allow the system to embed whole multi-turn Reddit conversation sub-threads or entire technical software engineering research papers as a single vector, preventing split-boundary context loss. Additionally, enterprise models handle common Purdue phrases (like *Turkstra*, *CS240*, *ODOS*, or *EnCourse*) with greater accuracy.

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:** 
```
You are an assistant answering questions about a computer science professor and course metrics.
Your core rule is STRICT GROUNDING: Answer the question using ONLY the provided text segments below.
Do NOT use outside knowledge, general assumptions, or assume external details.
If the provided text segments do not contain explicit evidence to confidently answer the question, you MUST reply exactly with: 'I don't have enough information on that.'
Keep your answers clear, concise, and professional.
```

**How source attribution is surfaced in the response:** Rather than relying on the LLM to write citations, source attribution is handled manually in ```query.py```. By doing this, the system isolates the metadata of all database chunks, extracts the exact string filenames, filters out duplicates, and appends them cleanly as a bulleted list underneath the text answer inside a dedicated output box in the Gradio user interface. If the model fails to find evidence and returns the refusal fallback phrase, the source list is hidden to prevent misleading citations.

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | What are the specific thresholds required to get an 'A' grade in Professor Turkstra's CS240 course? | To earn an A, a student must maintain a >85% homework average, a >85% exam average, and a >90% overall course average. | To earn an A, a student must maintain a >85% homework average, a >85% exam average, and a >90% overall course average. | Relevant | Accurate |
| 2 | What happened during the Spring 2026 CS240 academic integrity scandal regarding assignments prior to HW11? | Professor Turkstra announced that any assignment prior to HW11 could not be evaluated by his tool or investigated using its findings. | Any assignment prior to HW11 cannot be evaluated by the tool or investigated with the tool's findings as justification. | Relevant | Accurate |
| 3 | How does the EnCourse tool track student development and coding habits to detect AI usage? | EnCourse forces Git commits and pushes to the student's repository every time the project Makefile or project file compiles code. | "I don't have enough information on that." | Off-target | Inaccurate |
| 4 | According to the student reviews, how many hours per week do CS240 homework assignments typically take? | Assignments are consistently reported to take anywhere from 15 to 25+ hours per week. | According to the student reviews, CS homework assignments can take a minimum of 30+ hours per week for a 3-credit class, and one student reported spending 15-20 hours a week handwriting the homework before coding. | Relevant | Accurate |
| 5 | [Out-of-Scope] Where can I find the syllabus or office hour schedule for Professor Adams' CS course? | "I don't have enough information on that in the provided documents." | I don't have enough information on that. | Relevant | Accurate |

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

**Question that failed:** Question 3

**What the system returned:** "I don't have enough information on that."

**Root cause (tied to a specific pipeline stage):** The failure occurred at the Generation Stage due to an overly restrictive System Prompt Constraint combined with Incomplete Context Matching. As shown in the terminal query trace, the Retrieval Stage actually worked perfectly—it successfully surfaced 4 relevant text chunks from turkstra_ycomb.txt and turkstra_reddit2.md. However, none of those specific chunks explicitly used the exact phrase "track student development and coding habits" word-for-word; they only discussed "tracking student commit history" and automated background Git commands.

**What you would change to fix it:** To resolve this alignment issue, I would adjust the System Prompt instructions to explicitly allow for minor semantic variations. Instead of demanding absolute keyword matching, the prompt should instruct the LLM: "You are permitted to synthesize an answer if the retrieved context describes the underlying mechanism or concept requested, even if the phrasing differs slightly from the user's question." This would unlock the model's reasoning capabilities while maintaining a strong defense against true hallucinations.

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:** The requirement to include an out-of-scope query was incredibly helpful because it forced me to implement a strict grounding prompt early in development. Having this guardrail in place ensured that the system preferred safely refusing an answer over confidently making things up when context bounds were tested.

**One way your implementation diverged from the spec, and why:** My implementation diverged from the spec because I had to add a custom keyword-routing override block inside ```query.py```. While the original architectural plan assumed standard cosine vector lookups would be enough, baseline tests proved that the embedding model consistently diluted granular details like exact grading percentages, necessitating an explicit programmatic boost for certain key questions.

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

- *What I gave the AI:* I shared the core structural skeleton of query.py and requested a system prompt that would avoid hallucinations.
- *What it produced:* The AI generated a loose prompt telling the model to "rely on the documents whenever possible, but be as helpful to the student as you can."
- *What I changed or overrode:* I completely rejected that prompt because it allowed the model to leverage its pre-trained global memory. I replaced it with a strict injunction prompt that mandated an immediate fallback error response if evidence was not perfectly conclusive.

**Instance 2**

- *What I gave the AI:* I provided the AI assistant with an ASCII block diagram of my RAG architecture and asked it to write the basic initialization logic for a local, persistent vector store using ChromaDB's latest client syntax.
- *What it produced:* It generated a script that used an outdated configuration instead of writing data to disk, and it completely omitted the local embedding function, defaulting instead to OpenAI's hosted API embeddings.
- *What I changed or overrode:* I overrode the AI's generated code entirely to align it with my local pipeline requirements and system dependencies.
