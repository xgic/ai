# XGIC CLI command usage

**Status:** Documented requirement; implementation later  
**Tracking:** https://github.com/xgic/ai/issues/65

When required parameters or options are missing, every `xgic` command
and subcommand should print **full usage**, matching top-level `xgic`.
Do not emit only a short argparse error that forces the user to run
`-h`.

This is a **medium-priority** UX rule. Do not implement it until
higher-priority work is complete, unless a change already touches that
CLI module — then decide whether the usage fix ships in the same pull
request or stays on this milestone.

Apply the pattern first to **new** modules (including planned
`xgic wagtail`). Existing Payload CMS commands are not the first
implementation target.

Removing the architecture footer from `xgic` help (entry-point / ADR
blurb) needs **explicit approval** and must not drop operationally
useful output. Do not copy that footer class into new module help.

Catalog: [ecosystem/catalog.md](ecosystem/catalog.md). Modular CLI:
[ADR-0005](adr/0005-modular-xgic-cli-and-retirement-of-xde.md).
