# Application Kit

Builds a tailored job application from a job posting and a resume - a rewritten resume and cover letter as Word files and PDFs that applicant tracking systems can read, plus a prep sheet PDF with a requirement-by-requirement fit check, keyword coverage, which portfolio pieces to lead with, outreach notes to the recruiter and hiring manager, interview stories, questions to ask and a follow-up schedule. Never invents experience.

## Install

**Claude app (web, desktop):** turn on Settings > Capabilities > "Code execution and file creation". Then go to Customize > Skills, click "+", then "+ Create skill" > "Upload a skill", and upload `application-kit.zip` as is (don't unzip it).

**Claude Code:** install the whole Beautiful Engine collection:

```bash
claude plugin marketplace add BeautifulEngine/skills
claude plugin install beautiful-engine@beautiful-engine
```

Then use `/beautiful-engine:application-kit`, or ask in plain words.

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

## Made by Beautiful Engine

Made by [Beautiful Engine](https://www.beautifulengine.com), a creative studio in Los Angeles. Questions, ideas, or something broke? [Open an issue](https://github.com/BeautifulEngine/skills/issues/new). More skills: [github.com/BeautifulEngine/skills](https://github.com/BeautifulEngine/skills).

