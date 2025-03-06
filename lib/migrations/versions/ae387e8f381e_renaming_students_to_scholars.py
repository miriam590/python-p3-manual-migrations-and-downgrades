"""Renaming students to scholars

Revision ID: ae387e8f381e
Revises: 791279dd0760
Create Date: 2025-03-06 15:45:26.441540

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae387e8f381e'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')
    pass


def downgrade() -> None:
    op.rename_table('scholars', 'students')
    pass
