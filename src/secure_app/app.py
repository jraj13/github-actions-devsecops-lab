"""Small application used to demonstrate DevSecOps CI/CD controls."""

from __future__ import annotations


def calculate_total(amount: float, tax_rate: float) -> float:
    """Return the total amount including tax."""
    if amount < 0:
        raise ValueError("amount must be non-negative")

    if tax_rate < 0:
        raise ValueError("tax_rate must be non-negative")

    return round(amount * (1 + tax_rate), 2)


def main() -> None:
    """Run a small demonstration."""
    total = calculate_total(100.0, 0.07)
    print(f"Total: ${total:.2f}")


if __name__ == "__main__":
    main()
