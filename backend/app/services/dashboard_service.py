from datetime import datetime, timedelta

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.survey import LogAB, Pesquisa, Resposta
from app.services import ab_test_service


def _surveys_section(db: Session) -> dict:
    total = db.query(func.count(Pesquisa.id)).scalar() or 0
    active = (
        db.query(func.count(Pesquisa.id))
        .filter(Pesquisa.is_active.is_(True))
        .scalar()
        or 0
    )

    by_type_rows = (
        db.query(Pesquisa.respondent_type, func.count(Pesquisa.id))
        .group_by(Pesquisa.respondent_type)
        .all()
    )
    by_type = [
        {"respondent_type": rtype.value if rtype is not None else None, "count": count}
        for rtype, count in by_type_rows
    ]

    monthly_rows = (
        db.query(
            func.date_trunc("month", Pesquisa.created_at).label("month"),
            func.count(Pesquisa.id),
        )
        .group_by("month")
        .order_by("month")
        .all()
    )
    monthly = [
        {"month": m.isoformat() if m is not None else None, "count": c}
        for m, c in monthly_rows
    ]

    recent_rows = (
        db.query(Pesquisa)
        .order_by(Pesquisa.created_at.desc())
        .limit(5)
        .all()
    )
    recent = [
        {
            "id": p.id,
            "title": p.title,
            "respondent_type": p.respondent_type.value if p.respondent_type else None,
            "is_active": p.is_active,
            "created_at": p.created_at.isoformat() if p.created_at else None,
        }
        for p in recent_rows
    ]

    return {
        "total": total,
        "active": active,
        "inactive": total - active,
        "by_respondent_type": by_type,
        "monthly": monthly,
        "recent": recent,
    }


def _responses_section(db: Session) -> dict:
    total = db.query(func.count(Resposta.id)).scalar() or 0
    last_at = db.query(func.max(Resposta.submitted_at)).scalar()

    per_survey_rows = (
        db.query(Pesquisa.id, Pesquisa.title, func.count(Resposta.id))
        .outerjoin(Resposta, Resposta.survey_id == Pesquisa.id)
        .group_by(Pesquisa.id, Pesquisa.title)
        .order_by(func.count(Resposta.id).desc())
        .limit(10)
        .all()
    )
    per_survey = [
        {"survey_id": sid, "title": title, "count": count}
        for sid, title, count in per_survey_rows
    ]

    cutoff = datetime.utcnow() - timedelta(days=30)
    daily_rows = (
        db.query(
            func.date_trunc("day", Resposta.submitted_at).label("day"),
            func.count(Resposta.id),
        )
        .filter(Resposta.submitted_at >= cutoff)
        .group_by("day")
        .order_by("day")
        .all()
    )
    daily = [
        {"day": d.isoformat() if d is not None else None, "count": c}
        for d, c in daily_rows
    ]

    return {
        "total": total,
        "last_submitted_at": last_at.isoformat() if last_at is not None else None,
        "per_survey": per_survey,
        "daily": daily,
    }


def _logs_section(db: Session) -> dict:
    total = db.query(func.count(LogAB.id)).scalar() or 0
    accesses = 0
    dropouts = 0
    accessibility = 0
    per_log = []

    rows = db.query(LogAB.id, LogAB.response_id, LogAB.data).all()
    for log_id, response_id, data in rows:
        if not isinstance(data, dict):
            continue
        a = int(data.get("accesses") or 0)
        d = int(data.get("dropouts") or 0)
        ai = int(data.get("accessibility_interactions") or 0)
        accesses += a
        dropouts += d
        accessibility += ai
        per_log.append(
            {
                "id": log_id,
                "response_id": response_id,
                "accesses": a,
                "dropouts": d,
                "accessibility_interactions": ai,
                "total": a + d + ai,
            }
        )

    per_log.sort(key=lambda x: x["total"], reverse=True)
    dropout_rate = (dropouts / accesses) if accesses > 0 else 0.0

    return {
        "total": total,
        "accesses": accesses,
        "dropouts": dropouts,
        "accessibility_interactions": accessibility,
        "dropout_rate": round(dropout_rate, 4),
        "top_logs": per_log[:5],
    }


def get_dashboard(db: Session) -> dict:
    return {
        "generated_at": datetime.utcnow().isoformat(),
        "ab_test": ab_test_service.counts(),
        "surveys": _surveys_section(db),
        "responses": _responses_section(db),
        "logs": _logs_section(db),
    }
