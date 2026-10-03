# XGIC CLI command usage

**Status:** Documented requirement. Missing ACTION prints full usage
on `xgic wagtail` and `xgic gitlab`. Other modules later.  
**Tracking:** https://github.com/xgic/ai/issues/65

When required parameters or options are missing, every `xgic` command
and subcommand should print **full usage**, matching top-level `xgic`.
Do not emit only a short argparse error that forces the user to run
`-h`.

This is a **medium-priority** UX rule. Do not implement it until
higher-priority work is complete, unless a change already touches that
CLI module — then decide whether the usage fix ships in the same pull
request or stays on this milestone.

Shipped on `xgic wagtail`
(https://github.com/xgic/wagtail-cli) and `xgic gitlab`
(https://github.com/xgic/gitlab-cli/pull/18). Existing Payload CMS
commands are not the next implementation target.

## Option defaults

Every optional option shows its default in `--help`. Required options
do not. Use `argparse.ArgumentDefaultsHelpFormatter`, or a subclass
when the stored default is not the value a reader should see. Write
that value in the help text.

A command that is already being edited includes this formatter. Leave
untouched commands for their own change.

The architecture footer was removed from `xgic` help after explicit
approval ([xgic/cli#18](https://github.com/xgic/cli/pull/18); landed in
**xgic-cli 0.2.1**). Do not copy that footer class into new module help.

Catalog: [ecosystem/catalog.md](ecosystem/catalog.md). Modular CLI:
[ADR-0005](adr/0005-modular-xgic-cli-and-retirement-of-xde.md).
