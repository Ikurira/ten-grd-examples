"""The demo's search, sent with and without Ten-Grd's tenant restriction. No API key needed."""
import json

from qdrant_client import models
from ten_grd import Eq, TenantContext, tenant_scope

from rag_agent_demo import REFUNDS, docs, store  # Same seeded store as the agent demo.

print("Query: topic == 'refunds', nearest to the refunds vector\n")

# Without Ten-Grd: the tool's query sent straight to Qdrant.
topic = models.Filter(must=[models.FieldCondition(
    key="metadata.topic", match=models.MatchValue(value="refunds"))])
raw = store.query_points("policies", query=REFUNDS, query_filter=topic,
                         limit=3, with_payload=True).points
print("Without Ten-Grd:")
for point in raw:
    print(f"  {point.payload['tenant_id']:<7} {json.loads(point.payload['data_json'])['text']}")

# With Ten-Grd: the same query inside each host-authenticated tenant scope.
for tenant in ("acme", "globex"):
    with tenant_scope(TenantContext(tenant, "demo-user", f"compare-{tenant}")):
        hits = docs.search(REFUNDS, predicate=Eq("topic", "refunds"), limit=3)
    print(f"\nWith Ten-Grd as {tenant}:")
    for hit in hits:
        print(f"  [ok] {hit.record.tenant_id:<7} {hit.record.data['text']}")

store.close()
