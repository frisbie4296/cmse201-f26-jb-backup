#!/usr/bin/env python3
"""
CodeGrade Export Tool (MSU)
- Login via codegrade.login_from_cli()
- Loop: enter Course ID → pick assignment
- Export JSON via raw endpoints:
    • Rubric:   /api/v1/assignments/{assignment_id}/rubrics/
    • AutoTest: /api/v2/autotest/{assignment_id}
- Files saved as:
    <assignment_id>_rubric.json
    <assignment_id>_autotest.json
"""

from __future__ import annotations

import json
import sys
from typing import Any, List

import codegrade


# -------- Utilities --------

def save_json(filename: str, data: Any) -> None:
    """Write JSON to disk, pretty-printed."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"✔ Saved {filename}")


def http_get_json(client, path: str) -> Any:
    """
    GET a raw JSON endpoint via the CodeGrade client's HTTP session.
    Raises RuntimeError with a concise message on non-200 responses.
    """
    http = getattr(client, "http", None)
    if http is None:
        raise RuntimeError("CodeGrade HTTP session not available on client (missing .http).")

    resp = http.get(path, timeout=None)
    status = getattr(resp, "status_code", None)
    if status != 200:
        url = getattr(resp, "url", path)
        body = ""
        try:
            body = resp.text
        except Exception:
            pass
        preview = (body[:400] + "…") if body and len(body) > 400 else body
        raise RuntimeError(f"HTTP {status} for {url}. Body: {preview}")

    try:
        return resp.json()
    except Exception:
        return json.loads(resp.content.decode("utf-8", errors="ignore"))


def get_assignments(client, course_id: int) -> List[Any]:
    """Fetch all assignments for a course (paginated Response → list)."""
    try:
        resp = client.course.get_assignments(course_id=course_id)
        return list(resp)
    except Exception as e:
        print(f"✖ Could not fetch assignments: {e}")
        return []


# -------- Export actions --------

def export_rubric(client, assignment_id: int) -> None:
    path = f"/api/v1/assignments/{assignment_id}/rubrics/"
    try:
        data = http_get_json(client, path)
        if data:
            save_json(f"{assignment_id}_rubric.json", data)
        else:
            print("ℹ No rubric found.")
    except Exception as e:
        print(f"✖ Rubric fetch failed: {e}")


def export_autotest(client, assignment_id: int) -> None:
    path = f"/api/v2/autotest/{assignment_id}"
    try:
        data = http_get_json(client, path)
        if data:
            save_json(f"{assignment_id}_autotest.json", data)
        else:
            print("ℹ No AutoTest found.")
    except Exception as e:
        print(f"✖ AutoTest fetch failed: {e}")


# -------- Main CLI --------

def main() -> int:
    print("Authenticating with CodeGrade…")
    try:
        with codegrade.login_from_cli() as client:
            print("✓ Authenticated.\n")

            while True:
                raw = input("Enter Course ID (or 'q' to quit): ").strip().lower()
                if raw == "q":
                    break
                if not raw.isdigit():
                    print("✖ Invalid course ID.\n")
                    continue

                course_id = int(raw)
                try:
                    course = client.course.get(course_id=course_id)
                except Exception:
                    print("✖ Could not fetch course.\n")
                    continue

                print(f"\n📚 Course: {course.name} (ID {course.id})")

                assignments = get_assignments(client, course_id)
                if not assignments:
                    print("ℹ No assignments found for this course.\n")
                    continue

                while True:
                    print("\nAssignments:")
                    for i, a in enumerate(assignments, start=1):
                        a_name = getattr(a, "name", "Unnamed")
                        a_id = getattr(a, "id", "?")
                        print(f"[{i}] {a_name} (ID {a_id})")
                    print("[0] Back to courses")

                    sel = input("Select assignment: ").strip()
                    if not sel.isdigit():
                        continue
                    sel = int(sel)

                    if sel == 0:
                        break
                    if not (1 <= sel <= len(assignments)):
                        continue

                    assignment = assignments[sel - 1]
                    print(f"\n📝 Assignment: {assignment.name} (ID {assignment.id})")

                    while True:
                        print("[1] Export Rubric JSON")
                        print("[2] Export AutoTest JSON")
                        print("[0] Back to assignments")
                        action = input("Choose: ").strip()

                        if action == "0":
                            break
                        elif action == "1":
                            export_rubric(client, assignment.id)
                        elif action == "2":
                            export_autotest(client, assignment.id)
                        else:
                            print("Invalid choice.")

            return 0

    except Exception as e:
        print(f"Login failed: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
