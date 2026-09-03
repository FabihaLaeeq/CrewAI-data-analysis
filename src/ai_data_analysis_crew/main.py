#!/usr/bin/env python
import sys
import warnings

from ai_data_analysis_crew.crew import AiDataAnalysisCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the customer behavior analysis crew.
    """
    inputs = {
        "topic": "customer purchasing behavior",
        "current_year": "2026"
    }

    try:
        AiDataAnalysisCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(
            f"An error occurred while running the crew: {e}"
        )


def train():
    """
    Train the crew.
    """
    inputs = {
        "topic": "customer purchasing behavior",
        "current_year": "2026"
    }

    try:
        AiDataAnalysisCrew().crew().train(
            n_iterations=int(sys.argv[1]),
            filename=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(
            f"An error occurred while training the crew: {e}"
        )


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        AiDataAnalysisCrew().crew().replay(
            task_id=sys.argv[1]
        )
    except Exception as e:
        raise Exception(
            f"An error occurred while replaying the crew: {e}"
        )


def test():
    """
    Test the crew execution.
    """
    inputs = {
        "topic": "customer purchasing behavior",
        "current_year": "2026"
    }

    try:
        AiDataAnalysisCrew().crew().test(
            n_iterations=int(sys.argv[1]),
            eval_llm=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(
            f"An error occurred while testing the crew: {e}"
        )


def run_with_trigger():
    """
    Run the crew with trigger payload.
    """
    import json

    if len(sys.argv) < 2:
        raise Exception(
            "No trigger payload provided."
        )

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception(
            "Invalid JSON payload provided as argument"
        )

    inputs = {
        "crewai_trigger_payload": trigger_payload,
        "topic": "customer purchasing behavior",
        "current_year": "2026"
    }

    try:
        result = AiDataAnalysisCrew().crew().kickoff(
            inputs=inputs
        )
        return result
    except Exception as e:
        raise Exception(
            f"An error occurred while running the crew with trigger: {e}"
        )
