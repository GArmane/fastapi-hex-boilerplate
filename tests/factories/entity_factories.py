from typing import Any

import factory

# Register providers
providers: Any = []

for provider in providers:
    factory.Faker.add_provider(provider)
