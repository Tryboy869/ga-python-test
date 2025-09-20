#!/usr/bin/env python3
# NEXUS AXION - Moteur de test
import yaml

workflow_yaml = '''
name: Local Test
on: push
jobs:
  test:
    runs-on: ubuntu-latest  
    steps:
      - name: Local Hello
        run: echo "Hello from Python engine!"
'''

print("🎭 Moteur NEXUS AXION activé")
print("Workflow chargé:", yaml.safe_load(workflow_yaml)['name'])
