# Beautiful Engine skills

Claude skills made by [Beautiful Engine](https://www.beautifulengine.com), a creative studio in Los Angeles working across brand, experiential and interactive design.

**Website:** [beautifulengine.com](https://www.beautifulengine.com) · **Questions, ideas, or something broke?** [Open an issue](https://github.com/BeautifulEngine/skills/issues/new)

## Skills

| Skill | What it does | Get it |
|---|---|---|
| **Company Brief** | Name any company and get a designed, sourced PDF brief in its brand colors, a one-page cheat sheet, and a brand kit. Built for interview prep, offers, client work and pitches. | [Details, examples and the Claude app download](https://github.com/BeautifulEngine/company-brief) |

More are on the way. Installing the collection below gets you new skills as they're added.

![Animated demo: example requests typed into Claude, each followed by what Company Brief makes](https://raw.githubusercontent.com/BeautifulEngine/company-brief/main/docs/how-to-ask.gif)

## Install in Claude Code

```bash
claude plugin marketplace add BeautifulEngine/skills
claude plugin install beautiful-engine@beautiful-engine
```

Inside a Claude Code session you can do the same with `/plugin marketplace add BeautifulEngine/skills`, then `/plugin install beautiful-engine@beautiful-engine`.

Then use the skills with the `beautiful-engine:` prefix, or just ask in plain words:

```
/beautiful-engine:company-brief linear.app
/beautiful-engine:company-brief Figma for Senior Brand Designer
/beautiful-engine:company-brief compare Figma and Canva
```

To get the latest versions:

```bash
claude plugin marketplace update beautiful-engine
claude plugin update beautiful-engine@beautiful-engine
```

## Install in the Claude app

The Claude app (web and desktop) installs skills one at a time from a zip. Each skill's own page has the zip and step-by-step instructions:

- **Company Brief:** [github.com/BeautifulEngine/company-brief](https://github.com/BeautifulEngine/company-brief)

## Get in touch

- **Website:** [beautifulengine.com](https://www.beautifulengine.com)
- **Feedback on a skill:** [open an issue](https://github.com/BeautifulEngine/skills/issues/new) and say which skill, what you asked for, and what happened.

## For maintainers

```
.claude-plugin/marketplace.json                 the catalog Claude Code reads
plugins/beautiful-engine/
├── .claude-plugin/plugin.json                  plugin name, description, author, website
└── skills/
    └── company-brief/                          one folder per skill
```

**Update Company Brief** after changing it in its own repo:

```bash
scripts/sync-skill.sh ../company-brief/company-brief company-brief
git add -A && git commit -m "Sync company-brief" && git push
```

**Add a new skill:** put its folder (with its `SKILL.md`) in `plugins/beautiful-engine/skills/`, add a row to the Skills table above, run `claude plugin validate .`, then push. Name each skill for what it does, in lowercase with hyphens; the `beautiful-engine:` prefix comes from the plugin.

The plugin has no `version` field on purpose, so every push reaches users when they update. The validator shows a warning about this; it's safe to ignore.

## License

MIT. See [LICENSE](LICENSE).
