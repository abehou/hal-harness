import json

data = json.load(open('assistantbench_assistantbench_browser_agent_gpt5_1754633901_UPLOAD.json'))

failed_tasks = data['raw_eval_results']['failed_tasks']

failed_runs = [d for d in data['raw_logging_results'] if d['summary']['weave']['status']!="success"]
