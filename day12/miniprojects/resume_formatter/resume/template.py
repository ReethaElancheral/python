def generate_resume(data, format="text"):
    lines = []

    lines.append(f"# {data['name']}" if format == "markdown" else data['name'])
    lines.append(data['email'])
    lines.append("")
    lines.append(data['summary'])
    lines.append("")

    # Education
    lines.append("## Education" if format == "markdown" else "Education:")
    for edu in data['education']:
        lines.append(f"- {edu['degree']} at {edu['institution']} ({edu['year']})")

    lines.append("")

    # Experience
    lines.append("## Experience" if format == "markdown" else "Experience:")
    for exp in data['experience']:
        lines.append(f"- {exp['role']} at {exp['company']} ({exp['years']})")
        lines.append(f"  {exp['details']}")

    lines.append("")

    # Skills
    lines.append("## Skills" if format == "markdown" else "Skills:")
    lines.append(", ".join(data['skills']))

    return "\n".join(lines)
