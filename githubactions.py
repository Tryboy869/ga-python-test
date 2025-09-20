
import yaml, subprocess, re

class GitHubActionsEngine:
    """Moteur Python qui simule l'exécution d'un workflow GitHub Actions."""
    def __init__(self, workflow_yaml_content: str):
        self.workflow = yaml.safe_load(workflow_yaml_content)
        # Valeurs en dur pour la simulation
        self.GITHUB_USERNAME = "Tryboy869"
        self.REPO_NAME = "ga-python-test"
        self.context = self._setup_context()

    def _setup_context(self):
        return {'github': {'repository': f"{self.GITHUB_USERNAME}/{self.REPO_NAME}", 'actor': self.GITHUB_USERNAME}, 'env': {}}

    def _substitute_context(self, command_string: str) -> str:
        matches = re.findall(r'\${{\s*([\w\.]+)\s*}}', command_string)
        for match in matches:
            parts = match.split('.')
            value = self.context
            try:
                for part in parts: value = value[part]
                command_string = command_string.replace(f'${{{{ {match} }}}}', str(value))
            except KeyError:
                print(f"  [AVERTISSEMENT] Variable de contexte non trouvée : {match}")
        return command_string

    def run(self):
        print(f"🚀 Démarrage de l'exécution du workflow : '{self.workflow.get('name', 'Untitled')}'")
        print("-" * 50)
        for job_id, job_data in self.workflow.get('jobs', {}).items():
            print(f"\n Job: '{job_id}'")
            print(f"  [INFO] Simulation sur runner: '{job_data.get('runs-on', 'unknown')}'")
            for i, step in enumerate(job_data.get('steps', [])):
                step_name = step.get('name', f'Step {i + 1}')
                print(f"\n  ▶️  Exécution du step: '{step_name}'")
                if 'run' in step:
                    command = self._substitute_context(step['run'])
                    print(f"    [CMD] Exécution :\n---\n{command.strip()}\n---")
                    try:
                        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True, executable='/bin/bash')
                        if result.stdout: print(f"    [SORTIE]\n{result.stdout.strip()}")
                    except subprocess.CalledProcessError as e:
                        print(f"    [ERREUR] Step échoué (code {e.returncode}):\n{e.stderr.strip()}")
                        return
            print("-" * 50)

# --- Section d'exemple pour l'exécution en standalone ---
if __name__ == "__main__":
    workflow_content = """

name: Simple Python Engine Test
on: [push]
jobs:
  test_job_1:
    runs-on: ubuntu-latest # Simulé par le moteur
    steps:
      - name: Say Hello
        run: echo "Hello from the Python-based NEXUS AXION engine!"

      - name: Show Simulated Context
        run: echo "Repository should be ${{ github.repository }}"

      - name: Run a multi-line script
        run: |
          echo "This is a multi-line script."
          echo "Line 2."
          
      - name: Check Python version
        run: python --version

    """
    print("--- Démarrage de la simulation en mode standalone ---")
    engine = GitHubActionsEngine(workflow_content)
    engine.run()
