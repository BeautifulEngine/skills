---
name: application-kit
description: Builds a tailored job application from a job posting and a resume - a rewritten resume and cover letter as Word files and PDFs that applicant tracking systems can read, plus a prep sheet PDF with a requirement-by-requirement fit check, keyword coverage, which portfolio pieces to lead with, outreach notes to the recruiter and hiring manager, interview stories, questions to ask and a follow-up schedule. Never invents experience. Use when someone asks to tailor a resume, write a cover letter, apply for a job, prepare an application, or reach out about a role. Usage - /application-kit followed by the job posting link or text, with a resume attached.
---

# Application Kit

Turn a job posting and a resume into everything needed to apply well: a resume and cover letter aimed at this role, a clear-eyed fit check, the portfolio pieces to lead with, notes to the people doing the hiring, and a follow-up plan. Everything comes from the person's real experience, said in the posting's language.

## Usage

```
/application-kit <job posting URL or pasted text> [company brief attached] [portfolio link]
```

Attach a resume (PDF, Word or text) or point to one from earlier in the conversation. Plain requests work too:

- "Tailor my resume and write a cover letter for this role: <link>." (resume attached)
- "Application kit for the Netflix Design Lead posting. Here's my resume and my Company Brief on Netflix."
- "Just the cover letter, warm and direct, for this posting."
- "Outreach note to the hiring manager for this role."
- Add "one page" or "two pages" to set resume length.

Works well after the Company Brief skill: if a brief on the company exists in the conversation or is attached, use its priorities, language, people and interview notes.

**Files.** `<skill-dir>` means this skill's folder, the one holding this SKILL.md. Templates are in `assets/`, scripts in `scripts/`, and the shared PDF steps (fonts, colors, render, check) are in `references/rendering.md`.

## Hard rules

- **Never invent experience.** No new jobs, titles, dates, employers, degrees, tools, metrics or achievements. Reword, reorder, cut and emphasize what's in the resume and what the person tells you. If a stronger bullet needs a number you don't have, write the bullet without it and ask for the number in the reply.
- **Truthful keyword matching.** Use the posting's words where they honestly describe the person's work. If a requirement isn't met, the fit check says so plainly, with an honest way to address it (adjacent experience, a project, a plan to learn). Don't hide gaps in the documents with vague wording.
- **Ask before adding.** Anything the person mentioned in conversation but isn't on the resume goes in only after they confirm it's accurate and theirs to claim.
- **Readable by applicant tracking systems.** Single column, standard section names (Summary, Experience, Skills, Education), plain bullets, no tables, text boxes, icons or images in the Word file, dates on each role, and contact details in the body (not a header).
- **Drafts only.** Outreach notes are drafts for the person to send. Don't send anything, and don't guess anyone's personal email.
- **Respect the length.** One page for under about 10 years of experience, two pages at most for senior roles, unless the person says otherwise.
- **Credit line:** the prep sheet ends with a small Beautiful Engine credit. Keep it unless the person asks to leave it out. The resume, cover letter and outreach notes never carry it.

## Workflow

1. **Read the posting** (fetch the link; use a browser when the page needs one). Extract: title, level, team, location and remote policy, pay range if listed, must-have requirements, nice-to-haves, tools, the hiring manager's title, and the words the posting repeats. Save them in `notes.md`.
2. **Read the resume** and any portfolio link or Company Brief. List the person's real experience, results and tools.
3. **Fit check**: a table of every requirement → the person's strongest evidence → strength (strong, partial, gap) → how to address it. Count keyword coverage: which important posting terms honestly appear, and which are missing.
4. **Tailor the resume** in `resume.md` (format in `scripts/md_doc.py`): a 2–3 line summary aimed at this role; roles in reverse order; the most relevant bullets first in each role, rewritten as action + what + result; skills in the posting's vocabulary where true; cut what doesn't serve this application.
5. **Write the cover letter** in `cover-letter.md`: 250–350 words, addressed to the hiring manager by name if public. Open with why this company and this role, using a specific fact from the posting or the company's recent work; two short paragraphs of proof mapped to their top two needs; a close that asks for the conversation. In the person's voice, no clichés ("I am writing to express my interest", "passionate", "team player").
6. **Make the files**:
   - `python3 <skill-dir>/scripts/md_doc.py resume.md "<Name>-Resume-<Company>.docx" --html resume-body.html`
   - same for the cover letter
   - PDFs: paste each HTML fragment into `assets/resume-template.html` (copy `base.css`) and render per references/rendering.md, with clean, neutral fonts (Inter or Source Serif 4) rather than the company's brand. Check the resume PDF fits the page limit.
7. **Prep sheet** from `assets/kit-template.html`: fit check, keyword coverage, portfolio picks (which 3–5 pieces, in what order, and the one-line framing for each), outreach drafts (recruiter, hiring manager, a referral ask for someone in the person's network), 4–6 interview stories in situation-action-result form mapped to requirements, 5 questions to ask, and a follow-up schedule with dates (apply, nudge after 5–7 business days, thank-you notes within 24 hours of interviews).
8. **Render, audit and check** every file. Re-read the resume against the original: every claim must trace back to it or to something the person confirmed.
9. **Deliver** the resume (Word and PDF), the cover letter (Word and PDF) and the prep sheet. In the reply: the fit in one line (strong, stretch or long shot, and why), the biggest gap and how to handle it, numbers you'd like for stronger bullets, and the first follow-up date.

Output names: `<Name>-Resume-<Company>.docx/.pdf`, `<Name>-Cover-Letter-<Company>.docx/.pdf`, `<Company>-Application-Prep-<YYYY-MM>.pdf`.
