#!/usr/bin/env python3
"""Run LangGraph's official checkpoint conformance suite on InMemorySaver."""

from __future__ import annotations

import asyncio

from langgraph.checkpoint.conformance import checkpointer_test, validate
from langgraph.checkpoint.memory import InMemorySaver


@checkpointer_test(name="ComplexReferenceInMemory")
async def checkpointer():
    yield InMemorySaver()


async def main() -> None:
    report = await validate(checkpointer)
    report.print_report()
    if not report.passed_all_base():
        raise SystemExit(1)


if __name__ == "__main__":
    asyncio.run(main())
