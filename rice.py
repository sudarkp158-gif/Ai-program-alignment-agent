def calculate_rice(reach, impact, confidence, effort):
    """
    Calculate the RICE score.

    RICE = (Reach × Impact × Confidence) / Effort
    """

    if effort <= 0:
        raise ValueError("Effort must be greater than zero.")

    return (reach * impact * confidence) / effort


if __name__ == "__main__":
    score = calculate_rice(
        reach=5000,
        impact=3,
        confidence=0.8,
        effort=4
    )

    print(f"RICE Score: {score}")
