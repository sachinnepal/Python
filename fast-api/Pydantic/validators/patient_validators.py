def validate_email_domain(value: str) -> str:
    valid_domains = ["nabil.com", "gibl.com"]

    domain = value.split("@")[-1]
    if domain not in valid_domains:
        raise ValueError(
            f"Email domain must be one of {valid_domains}"
        )

    return value


def capitalize_name(value: str) -> str:
    return value.upper()