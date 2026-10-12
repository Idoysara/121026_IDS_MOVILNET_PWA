#!/usr/bin/env python3
"""
tests/test_n8n_live_connector.py — Verificación del Conector en Vivo de n8n
===========================================================================
"""

import unittest
from pathlib import Path
from scripts.connect_n8n_live import N8nLiveConnector, ConnectionDiagnostics


class TestN8nLiveConnector(unittest.TestCase):
    """Pruebas unitarias para el conector en vivo Movilnet ↔ n8n."""

    def setUp(self):
        self.connector = N8nLiveConnector()

    def test_workflow_file_validity(self):
        """Verifica que el workflow de 74 nodos existe y tiene la estructura correcta."""
        self.assertTrue(self.connector.workflow_path.exists())
        self.assertEqual(len(self.connector.workflow_data.get("nodes", [])), 74)

    def test_lan_ip_detection(self):
        """Verifica que detecta una IP de formato válido."""
        ip = self.connector.get_lan_ip()
        self.assertTrue(len(ip.split(".")) == 4)

    def test_diagnostics_execution(self):
        """Verifica que el diagnóstico produce un objeto válido."""
        diag = self.connector.run_diagnostics()
        self.assertIsInstance(diag, ConnectionDiagnostics)
        self.assertEqual(diag.workflow_nodes_count, 74)
        self.assertIn("8000/api/v1/n8n/webhook-ingest", diag.core_webhook_url)


if __name__ == "__main__":
    unittest.main()
