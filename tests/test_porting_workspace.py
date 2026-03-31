from __future__ import annotations

import subprocess
import sys
import unittest

from src.port_manifest import build_port_manifest
from src.query_engine import QueryEnginePort


class PortingWorkspaceTests(unittest.TestCase):
    def test_manifest_counts_python_files(self) -> None:
        manifest = build_port_manifest()
        self.assertGreaterEqual(manifest.total_python_files, 7)
        self.assertTrue(manifest.top_level_modules)

    def test_query_engine_summary_mentions_workspace(self) -> None:
        summary = QueryEnginePort.from_workspace().render_summary()
        self.assertIn('Python Porting Workspace Summary', summary)
        self.assertIn('Command surface', summary)
        self.assertIn('Tool surface', summary)

    def test_cli_summary_runs(self) -> None:
        result = subprocess.run(
            [sys.executable, '-m', 'src.main', 'summary'],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn('Python Porting Workspace Summary', result.stdout)


if __name__ == '__main__':
    unittest.main()
