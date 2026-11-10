#!/usr/bin/env python3
"""Install Aurelia into explicit skill folders, without executing downloaded code."""
import argparse
import json
from pathlib import Path
import shutil
import sys

SOURCE = Path(__file__).resolve().parent
TARGETS = {
    'claude': Path.home() / '.claude' / 'skills',
    'codex': Path.home() / '.agents' / 'skills',
    'antigravity': Path('.agent') / 'skills',
    'generic': Path('.ai') / 'skills',
}


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--target', choices=TARGETS, default='generic')
    p.add_argument('--dest', help='Override skills parent directory (recommended if host paths differ)')
    p.add_argument('--force', action='store_true', help='Replace only a prior managed Aurelia install')
    p.add_argument('--dry-run', action='store_true')
    a = p.parse_args(argv)
    parent = Path(a.dest).expanduser().resolve() if a.dest else TARGETS[a.target].resolve()
    destination = parent / 'aurelia-studio'
    if destination == SOURCE or destination.is_relative_to(SOURCE) or SOURCE.is_relative_to(destination):
        p.error('Source and destination must not overlap')
    marker = destination / '.aurelia-installed.json'
    if destination.is_symlink():
        p.error('Refusing symlink destination')
    if destination.exists():
        if not a.force:
            p.error('Destination exists; use --force only for a prior managed installation')
        if not marker.is_file() or marker.is_symlink():
            p.error('Refusing to replace a folder not created by this installer')
        try:
            valid = json.loads(marker.read_text()).get('package') == 'aurelia-studio'
        except (OSError, ValueError):
            valid = False
        if not valid:
            p.error('Invalid managed install marker')
    print('Target:', a.target)
    print('Install folder:', destination)
    print('No API calls. No package manager. No shell profile changes.')
    if a.dry_run:
        return 0
    parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(SOURCE, destination, ignore=shutil.ignore_patterns('__pycache__', '*.pyc', 'aurelia-runs', '.git'))
    marker.write_text(json.dumps({'package': 'aurelia-studio', 'version': '1.0.0'}), encoding='utf-8')
    print('Installed. Open SKILL.md in your host, or use scripts/runner.py --plan.')
    print('Host support/model permissions are required; installation does not spawn agents.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
