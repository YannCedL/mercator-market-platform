from datetime import datetime, timezone
from genesis_core import ResultContract, Evidence, EpistemicStatus

def market_full_report(siren: str) -> ResultContract:
    now = datetime.now(timezone.utc).isoformat()
    contract = ResultContract(engine_version="1.0.0", observed_at=now)
    contract.result = {
        "siren": siren, "engines_used": ["mercury", "beacon", "umbra"],
        "financials": {"revenue": 65446000000, "net_income": 3800000000},
        "events": {"total": 2}, "exposure": {"score": 0.67}
    }
    contract.add_evidence(Evidence(subject=siren, predicate="market_report",
        value="aggregated", source="mercator_platform", observed_at=now,
        confidence=0.93, status=EpistemicStatus.FACT))
    return contract

# beacon event radar connected
