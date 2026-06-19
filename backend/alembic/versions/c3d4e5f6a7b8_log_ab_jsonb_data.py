"""log_ab jsonb data column

Revision ID: c3d4e5f6a7b8
Revises: b2c3d4e5f6a7
Create Date: 2026-06-18 00:02:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision: str = 'c3d4e5f6a7b8'
down_revision: Union[str, Sequence[str], None] = 'b2c3d4e5f6a7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('log_a_b', sa.Column('data', postgresql.JSONB(), nullable=True))

    op.execute("""
        UPDATE log_a_b
        SET data = jsonb_build_object(
            'accesses', accesses,
            'dropouts', dropouts,
            'accessibility_interactions', accessibility_interactions
        )
    """)

    op.alter_column('log_a_b', 'data', nullable=False)

    op.drop_column('log_a_b', 'accesses')
    op.drop_column('log_a_b', 'dropouts')
    op.drop_column('log_a_b', 'accessibility_interactions')


def downgrade() -> None:
    op.add_column('log_a_b', sa.Column('accesses', sa.Integer(), nullable=True))
    op.add_column('log_a_b', sa.Column('dropouts', sa.Integer(), nullable=True))
    op.add_column('log_a_b', sa.Column('accessibility_interactions', sa.Integer(), nullable=True))

    op.execute("""
        UPDATE log_a_b
        SET accesses = (data->>'accesses')::int,
            dropouts = (data->>'dropouts')::int,
            accessibility_interactions = (data->>'accessibility_interactions')::int
    """)

    op.alter_column('log_a_b', 'accesses', nullable=False)
    op.alter_column('log_a_b', 'dropouts', nullable=False)
    op.alter_column('log_a_b', 'accessibility_interactions', nullable=False)

    op.drop_column('log_a_b', 'data')
