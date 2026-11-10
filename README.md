# Aurelia Studio 1.0

Portable skill + six role instructions + actual asset library + optional API orchestrator.

## Quick start / jaldi shuru karein
Requires Python 3.10+ (Windows `py -3`, macOS/Linux `python3`). Extract the ZIP first. Run from the extracted folder's parent:

```sh
python3 aurelia-studio/install.py --target generic
```
Windows: `py -3 aurelia-studio/install.py --target generic`
No pip packages, admin rights, API calls or shell-profile changes. Generic installation lives in `.ai/skills/aurelia-studio` in your current directory. Restart/reload your host and explicitly open its SKILL.md if it doesn't auto-discover that folder.

Host-specific folder presets (not a guarantee of host support):
```sh
python3 aurelia-studio/install.py --target antigravity
python3 aurelia-studio/install.py --target claude
python3 aurelia-studio/install.py --target codex
python3 aurelia-studio/install.py --dest ./my-tool/skills
```
Antigravity preset is project-local `.agent/skills`; Claude is `~/.claude/skills`; Codex/open agent-skills preset is `~/.agents/skills`. Actual host versions may use different locations: override `--dest`. Arena products have no universal agent/skill install standard; use the generic folder and supply SKILL.md or configure the provider runner. The installer only copies files. It does not register native subagents or unlock model entitlements. Use `--dry-run` to inspect and `--force` only to replace a prior managed installation. Uninstall by deleting only its managed `aurelia-studio` directory.

## What is actually included
| Library | Exact scope |
|---|---|
| 1,080 designs | Explicit combinatorial recipes: 18 domains × 12 layouts × 5 themes, NOT bespoke finished websites |
| 520 components | 52 semantic patterns × 10 styled variants, browseable HTML/CSS/JS; integrate real handlers before production |
| 160 fonts | Real open-license families, bundled webfont files, CSS, source URLs and individual licenses; subset/weights vary |
| 64 animations | CSS recipes + scroll/reveal enhancement + reduced-motion + pause control |
| Six agents | Named role files, registry and original SVG logos, NOT six bundled LLMs |

Open `index.html` directly for the library. `components/index.html`, `animations/index.html`, and `fonts/index.html` also work locally without a server; the design explorer reads a packaged JS catalog. No telemetry or remote JavaScript. Font files are local. Large libraries should be selectively loaded in production, not imported all at once.

### Agent team
- ATLAS: 3D structure, Three.js, Blender, Unity, Godot.
- VELVET: premium UI and motion, responsiveness and interactions.
- CHROMA: font/color/type/motion selection and contrast.
- LUMEN: lighting, polish and authorized reference reconstruction (no promised copy percentage).
- FORGE: integration, backend, durable storage and repairs.
- SENTINEL: independent QA, security, bugs and fake-functionality detection.

## How host mode works
Paste the prompt from `PROMPT.txt` into your AI coding host after loading SKILL.md. If it has actual subagent APIs, it can use the six roles and approved models. Otherwise it must state that it is a sequential single-model simulation. Model assignment happens in the HOST; Markdown cannot force it. A chat-only tool cannot execute Blender or real browser tests. Six parallel discovery passes are followed by integration and independent QA; running every dependency blindly in parallel is not correct.

## Optional real parallel API runner
Python standard library only; requires an authorized OpenAI-compatible Chat Completions endpoint supporting `max_tokens`. It is NOT a native Arena or Antigravity connector. No API key is included.
1. Copy `models.example.json` to a private `models.local.json` OUTSIDE a git-tracked folder. Set base_url and all six model IDs. Choose models you can actually access; strongest model/cost depends on your provider.
2. Set `AURELIA_API_KEY` securely in your terminal, not in JSON or prompts. Bash: `read -rsp 'API key: ' AURELIA_API_KEY; export AURELIA_API_KEY; echo`. PowerShell: use a secure secret manager/environment injection rather than putting the key in command history.
3. Inspect offline:
```sh
python3 aurelia-studio/scripts/runner.py --config /path/to/models.local.json --plan
```
4. Run with explicit cost consent:
```sh
python3 aurelia-studio/scripts/runner.py --config /path/to/models.local.json --brief aurelia-studio/templates/brief.txt --out ./aurelia-runs --confirm-api-cost
```
Six simultaneous consultations + one Forge implementation + one Sentinel static review = 8 paid requests maximum, no automatic retry. Outputs are a fresh timestamped folder: role responses/usage, actual generated source, implementation manifest, audit and summary. Requests send your brief and generated source to your selected provider: do not include secrets/private material without approval. Explicit models are required; no automatic "best model" claims. Provider output can be malformed or incomplete; the runner stops on missing/truncated/unsafe responses.

**Important:** The runner generates candidate files but NEVER executes shell commands, installs their dependencies, runs browser tests, auto-fixes in a loop or deploys them. It always reports GENERATED_UNVERIFIED and release_ready=false. Read `audit.json` and run actual tests with your host; ask Forge to fix findings and Sentinel to rerun checks. Exit 2 means static review failed/blocked or service blockers remain, 1 is execution/config error, 0 means generation+static pass only, never production certification. Local safety tests use a mocked API explicitly; no live model run is included with this ZIP.

## Catalog search
```sh
python3 aurelia-studio/scripts/catalog.py designs 'SaaS Midnight' --limit 5
python3 aurelia-studio/scripts/catalog.py components dialog --limit 5
python3 aurelia-studio/scripts/catalog.py fonts sans --limit 5
python3 aurelia-studio/scripts/catalog.py animations scroll --limit 10
```

## Fonts and licensing
See `fonts/SOURCES.json`, `catalogs/fonts.json`, `fonts/licenses/` and `THIRD_PARTY_NOTICES.md`. Preserve the font licenses on redistribution. Latin web subsets do not imply Devanagari/Arabic support. A listed family does not imply every weight is bundled. No proprietary paid fonts are included. Original skill code/docs/catalog recipes/logos use LICENSE; font licenses take precedence for their files.

## Limits and non-goals
No universal one-command install exists for every terminal/LLM. Python must be installed, ZIP must be extracted, host must read skills. This pack cannot grant API access, paid model credits, professional experience, native engines, guaranteed 80–95% similarity or guaranteed bug-free apps. Backend credentials/cloud account/real test infrastructure are not included. Demo UI specimens are intentionally not complete applications and label sample data/actions. Production functional completeness is a gated workflow, not a claim about every component.

## Verification
`python3 -m unittest discover -s aurelia-studio/tests -v` validates inventory, font signatures/licenses, safe artifact writing, installer and runner using a local mocked API. Optional real browser checks: install Playwright separately (`python3 -m pip install playwright`, then `python3 -m playwright install chromium`) and run `python3 aurelia-studio/tests/browser_check.py`. Linux may need `python3 -m playwright install-deps chromium`. These test dependencies are not needed to install or use the skill. Browser checks cover the local library, not future generated applications. `TEST_REPORT.json` contains execution evidence from package creation. Real cloud/native-engine/API production validation remains NOT_RUN. No public application is deployed by this skill installation.
