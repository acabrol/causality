#!/usr/bin/env python3
"""Local dice roller for Causality playtests.

The roller uses secrets.randbelow(n) + 1, which gives each face exactly the
same probability in the program model. For example, d6 returns each face with
probability 1/6, and percentile d10 returns one of 00, 10, ..., 90 with
probability 1/10.
"""

from __future__ import annotations

import argparse
import re
import secrets
from collections import Counter
from dataclasses import dataclass


ROLL_RE = re.compile(r"^(?P<count>[1-9][0-9]*)?d(?P<sides>[1-9][0-9]*|%)(?P<percentile>%)?$", re.IGNORECASE)
OUTCOME_ORDER = ("critical success", "partial success", "partial failure", "critical failure")
OUTCOME_LABELS = {
    "en": {
        "critical success": "critical success",
        "partial success": "partial success",
        "partial failure": "partial failure",
        "critical failure": "critical failure",
    },
    "fr": {
        "critical success": "reussite critique",
        "partial success": "reussite partielle",
        "partial failure": "echec partiel",
        "critical failure": "echec critique",
    },
}
OUTCOME_TEXT_COLORS = {
    "critical failure": "#b42318",
    "partial failure": "#b54708",
    "partial success": "#175cd3",
    "critical success": "#027a48",
}
ABACUS_HEADER_COLOR = "#eaeef2"
ABACUS_ROW_COLORS = ("#ffffff", "#f6f8fa")
ABACUS_TEXT_COLOR = "#000000"
ABACUS_BORDER_COLOR = "#000000"


@dataclass(frozen=True)
class RollSpec:
    count: int
    sides: int
    percentile: bool = False


def parse_roll_spec(value: str) -> RollSpec:
    normalized = value.strip().lower()

    if normalized in {"d%", "d100", "percentile", "d10%"}:
        return RollSpec(count=1, sides=10, percentile=True)

    match = ROLL_RE.match(normalized)
    if not match:
        raise argparse.ArgumentTypeError(
            f"invalid roll '{value}'. Use examples like d6, 2d8, d20, d%, d10%, or percentile."
        )

    count = int(match.group("count") or 1)
    raw_sides = match.group("sides")
    percentile = bool(match.group("percentile"))

    if raw_sides == "%":
        return RollSpec(count=1, sides=10, percentile=True)

    sides = int(raw_sides)
    if sides < 2:
        raise argparse.ArgumentTypeError("dice must have at least 2 sides")

    if percentile:
        if count != 1 or sides != 10:
            raise argparse.ArgumentTypeError("percentile syntax only supports d10%")
        return RollSpec(count=1, sides=10, percentile=True)

    return RollSpec(count=count, sides=sides)


def roll_die(sides: int) -> int:
    return secrets.randbelow(sides) + 1


def roll(spec: RollSpec) -> tuple[list[int], int | str]:
    if spec.percentile:
        value = secrets.randbelow(10) * 10
        return [value], "00" if value == 0 else value

    faces = [roll_die(spec.sides) for _ in range(spec.count)]
    return faces, sum(faces)


def rewind_percentage(result: int, distance: int) -> float:
    return (result / distance) * 100


def format_percentage(value: float) -> str:
    text = f"{value:.2f}".rstrip("0").rstrip(".")
    return f"{text}%"


def causality_outcome(spec: RollSpec, value: int | str, distance: int | None) -> tuple[str, float | None]:
    if spec.percentile or spec.count != 1:
        return "not applicable", None

    if distance is None:
        return "requires --distance", None

    result = int(value)
    percentage = rewind_percentage(result, distance)

    if percentage >= 80:
        return "critical success", percentage
    if percentage >= 50:
        return "partial success", percentage
    if percentage > 20:
        return "partial failure", percentage
    return "critical failure", percentage


def rewind_outcome_for_value(value: int, distance: int) -> tuple[str, float]:
    percentage = rewind_percentage(value, distance)

    if percentage >= 80:
        return "critical success", percentage
    if percentage >= 50:
        return "partial success", percentage
    if percentage > 20:
        return "partial failure", percentage
    return "critical failure", percentage


def color_text(content: str, outcome: str) -> str:
    color = OUTCOME_TEXT_COLORS[outcome]
    return f'<font color="{color}">{content}</font>'


def abacus_cell(value: int, distance: int, language: str) -> tuple[str, str]:
    outcome, percentage = rewind_outcome_for_value(value, distance)
    label = OUTCOME_LABELS[language][outcome]
    content = f"{format_percentage(percentage)}<br>{label}"
    return color_text(content, outcome), OUTCOME_TEXT_COLORS[outcome]


def html_cell(
    tag: str,
    content: str,
    background: str,
    extra_attributes: str = "",
    text_color: str | None = None,
) -> str:
    color = text_color if text_color is not None else ABACUS_TEXT_COLOR
    style = (
        f"background-color:{background}; "
        f"color:{color}; "
        f"border:1px solid {ABACUS_BORDER_COLOR};"
    )
    attributes = f' style="{style}" bgcolor="{background}" bordercolor="{ABACUS_BORDER_COLOR}"'
    if extra_attributes:
        attributes += f" {extra_attributes}"
    return f"<{tag}{attributes}>{content}</{tag}>"


def print_abacus(spec: RollSpec, language: str) -> None:
    if language == "fr":
        title = f"Abaque Rewind Dice - d{spec.sides}"
        intro = (
            "Utilisez cette page pendant le jeu pour lire directement le resultat "
            "d'un Rewind Die selon la distance de rewind."
        )
        formula_label = "Formule"
        cell_label = "Format de cellule"
        distance_header = "Distance de rewind (Time Units)"
        outcome_header = "Effet"
        range_header = "Valeur de r"
        cell_description = "`pourcentage<br>effet`"
        ranges = (
            ("r <= 20%", OUTCOME_LABELS[language]["critical failure"]),
            ("20% < r < 50%", OUTCOME_LABELS[language]["partial failure"]),
            ("50% <= r < 80%", OUTCOME_LABELS[language]["partial success"]),
            ("r >= 80%", OUTCOME_LABELS[language]["critical success"]),
        )
    else:
        title = f"Rewind Dice Abacus - d{spec.sides}"
        intro = (
            "Use this page during play to read the Rewind Die result directly "
            "from the rewind distance."
        )
        formula_label = "Formula"
        cell_label = "Cell format"
        distance_header = "Rewind distance (Time Units)"
        outcome_header = "Outcome"
        range_header = "r value"
        cell_description = "`percentage<br>outcome`"
        ranges = (
            ("r <= 20%", OUTCOME_LABELS[language]["critical failure"]),
            ("20% < r < 50%", OUTCOME_LABELS[language]["partial failure"]),
            ("50% <= r < 80%", OUTCOME_LABELS[language]["partial success"]),
            ("r >= 80%", OUTCOME_LABELS[language]["critical success"]),
        )

    print(f"# {title}")
    print()
    print(intro)
    print()
    print(f"**{formula_label}:** `r = (Rewind Die result / rewind distance) x 100`")
    print()
    print(f"**{cell_label}:** {cell_description}")
    print()
    print(f"| {range_header} | {outcome_header} |")
    print("|---|---|")
    for range_text, outcome_text in ranges:
        outcome_key = next(key for key, label in OUTCOME_LABELS[language].items() if label == outcome_text)
        print(f"| {range_text} | {color_text(outcome_text, outcome_key)} |")
    print()

    print(
        f'<table border="1" cellspacing="0" cellpadding="4" '
        f'bordercolor="{ABACUS_BORDER_COLOR}" '
        f'style="border-collapse:collapse; border:1px solid {ABACUS_BORDER_COLOR};">'
    )
    print("  <thead>")
    print("    <tr>")
    print(f"      {html_cell('th', distance_header, ABACUS_HEADER_COLOR)}")
    for value in range(1, spec.sides + 1):
        print(f"      {html_cell('th', str(value), ABACUS_HEADER_COLOR)}")
    print("    </tr>")
    print("  </thead>")
    print("  <tbody>")
    for distance in range(1, 21):
        background = ABACUS_ROW_COLORS[(distance - 1) % len(ABACUS_ROW_COLORS)]
        print("    <tr>")
        print(f"      {html_cell('th', str(distance), background, 'scope=\"row\"')}")
        for value in range(1, spec.sides + 1):
            cell_content, text_color = abacus_cell(value, distance, language)
            print(f"      {html_cell('td', cell_content, background, text_color=text_color)}")
        print("    </tr>")
    print("  </tbody>")
    print("</table>")


def print_rolls(spec: RollSpec, times: int, show_causality: bool, distance: int | None) -> None:
    for index in range(1, times + 1):
        faces, total = roll(spec)
        if spec.percentile:
            print(f"{index}: percentile d10 -> {total}")
            continue

        face_text = ", ".join(str(face) for face in faces)
        if spec.count == 1:
            line = f"{index}: d{spec.sides} -> {total}"
        else:
            line = f"{index}: {spec.count}d{spec.sides} -> [{face_text}] = {total}"

        if show_causality:
            outcome, percentage = causality_outcome(spec, total, distance)
            if percentage is None:
                line += f" ({outcome})"
            else:
                line += (
                    f" (die value {total}; "
                    f"r = ({total} / {distance}) x 100 = {format_percentage(percentage)}; "
                    f"{outcome})"
                )

        print(line)


def print_distribution(spec: RollSpec, trials: int, show_causality: bool, distance: int | None) -> None:
    totals: Counter[int | str] = Counter()
    outcomes: Counter[str] = Counter()

    for _ in range(trials):
        _, total = roll(spec)
        totals[total] += 1
        if show_causality:
            outcome, _ = causality_outcome(spec, total, distance)
            outcomes[outcome] += 1

    print(f"Distribution for {trials} simulated rolls")
    if show_causality and distance is not None and not spec.percentile and spec.count == 1:
        print("Die value | r calculation | Count | Observed %")
        print("---:|---:|---:|---:")
    else:
        print("Result | Count | Observed %")
        print("---|---:|---:")

    for total in sorted(totals, key=lambda item: int(item) if item != "00" else 0):
        count = totals[total]
        percent = (count / trials) * 100
        if show_causality and distance is not None and not spec.percentile and spec.count == 1:
            value = int(total)
            calculation = rewind_percentage(value, distance)
            print(f"{value} | ({value} / {distance}) x 100 = {format_percentage(calculation)} | {count} | {percent:.3f}")
        else:
            print(f"{total} | {count} | {percent:.3f}")

    if show_causality:
        print()
        print("Causality outcome | Count | Observed %")
        print("---|---:|---:")
        for outcome in OUTCOME_ORDER:
            count = outcomes[outcome]
            percent = (count / trials) * 100
            print(f"{outcome} | {count} | {percent:.3f}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Simulate fair dice rolls for Causality playtests.")
    parser.add_argument("roll", type=parse_roll_spec, help="Roll expression: d4, d6, d8, d10, d12, d20, 2d6, d%, d10%.")
    parser.add_argument("-n", "--times", type=int, default=1, help="Number of rolls to print.")
    parser.add_argument("--distribution", type=int, metavar="TRIALS", help="Run many trials and print observed distribution.")
    parser.add_argument("--causality", action="store_true", help="Show Causality Rewind Die outcome categories for one-die rolls.")
    parser.add_argument("--distance", type=int, help="Rewind distance in Time Units for Causality outcome categories.")
    parser.add_argument("--abacus", action="store_true", help="Print a deterministic Markdown Rewind Dice abacus for distances 1 to 20.")
    parser.add_argument("--language", choices=("en", "fr"), default="en", help="Language for generated abacus labels.")

    args = parser.parse_args()

    if args.times < 1:
        parser.error("--times must be at least 1")

    if args.distance is not None:
        if args.distance < 1 or args.distance > 20:
            parser.error("--distance must be between 1 and 20")

    if args.causality and not args.roll.percentile and args.roll.count == 1 and args.distance is None:
        parser.error("--causality now requires --distance for Rewind Percentage")

    if args.abacus:
        if args.roll.percentile or args.roll.count != 1:
            parser.error("--abacus supports one Rewind Die only, such as d4, d6, d8, d10, d12, or d20")
        print_abacus(args.roll, args.language)
        return 0

    if args.distribution is not None:
        if args.distribution < 1:
            parser.error("--distribution must be at least 1")
        print_distribution(args.roll, args.distribution, args.causality, args.distance)
        return 0

    print_rolls(args.roll, args.times, args.causality, args.distance)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
