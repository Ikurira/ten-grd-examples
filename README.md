# Ten-Grd examples

Runnable examples for [Ten-Grd](https://pypi.org/project/ten-grd/), a Python SDK
that keeps tenant data isolated in agent tools, memory, retrieval and caches.
Every example installs Ten-Grd from PyPI and uses synthetic tenant data.
Documentation: [ikurira.github.io/ten-grd-examples](https://ikurira.github.io/ten-grd-examples/).

| Example | Shows | Needs |
| --- | --- | --- |
| [basic/agent_memory.py](basic/agent_memory.py) | Two tenants write the same record ID; each reads only its own. | Nothing beyond Ten-Grd |
| [basic/tenant_rag.py](basic/tenant_rag.py) | A foreign document with a closer vector is excluded from retrieval, and a widening selector cannot cross tenants. | In-memory Qdrant |
| [claude_agents/memory_agent.py](claude_agents/memory_agent.py) | Claude reads and writes memory through tools bound to the host's tenant. | Claude Agent SDK; API key for live mode |
| [claude_agents/rag_agent.py](claude_agents/rag_agent.py) | Claude answers from tenant-filtered retrieval. | Claude Agent SDK, in-memory Qdrant; API key for live mode |

## Quickstart

Python 3.10 or later, from the repository root in a virtual environment:

```sh
python -m pip install -r requirements.txt
python basic/agent_memory.py
python basic/tenant_rag.py
python -m claude_agents.memory_agent
python -m claude_agents.rag_agent
```

None of these commands call a model or need an API key. The Claude examples
run their tool checks offline by default. To run them against Claude, see
[claude_agents/README.md](claude_agents/README.md).

## Tests

```sh
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

The tests dispatch the Claude example tools through a real in-memory MCP client
and server without calling a model. CI runs the tests and every offline example
on Python 3.10 and 3.13, and again weekly to catch upstream changes.

## What these examples do and do not show

Ten-Grd checks that every data selection stays within the tenant the host has
authenticated, and fails closed when it cannot prove that. The host remains
responsible for authentication and for authorization within a tenant.

Ten-Grd does not prevent prompt injection, verify model answers, or sandbox a
process. Restrictive Agent SDK settings in these examples are not a sandbox.
The synthetic identities in the examples stand in for a real host's
authentication and must not be copied into production as-is.

## License

[Apache-2.0](LICENSE), the same license as Ten-Grd.
