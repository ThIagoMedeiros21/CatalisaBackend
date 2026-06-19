"""log_ab per response

Revision ID: a1b2c3d4e5f6
Revises: 091e5e6950d6
Create Date: 2026-06-18 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'a1b2c3d4e5f6'
down_revision: Union[str, Sequence[str], None] = '091e5e6950d6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("DELETE FROM log_a_b")

    op.drop_constraint('log_a_b_survey_id_fkey', 'log_a_b', type_='foreignkey')
    op.drop_column('log_a_b', 'survey_id')
    op.drop_column('log_a_b', 'respondent_type')

    op.alter_column('log_a_b', 'session_id', nullable=True)

    op.add_column('log_a_b', sa.Column('response_id', sa.Integer(), nullable=False))
    op.create_foreign_key('log_a_b_response_id_fkey', 'log_a_b', 'responses', ['response_id'], ['id'])


def downgrade() -> None:
    op.execute("DELETE FROM log_a_b")

    op.drop_constraint('log_a_b_response_id_fkey', 'log_a_b', type_='foreignkey')
    op.drop_column('log_a_b', 'response_id')

    op.alter_column('log_a_b', 'session_id', nullable=False)

    op.add_column('log_a_b', sa.Column('survey_id', sa.Integer(), nullable=False))
    op.add_column('log_a_b', sa.Column('respondent_type', sa.String(), nullable=False))
    op.create_foreign_key('log_a_b_survey_id_fkey', 'log_a_b', 'surveys', ['survey_id'], ['id'])
