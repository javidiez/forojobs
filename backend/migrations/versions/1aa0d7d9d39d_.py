"""empty message

Revision ID: 1aa0d7d9d39d
Revises: 404909a7bf76
Create Date: 2024-09-20 13:42:22.474704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1aa0d7d9d39d'
down_revision = '404909a7bf76'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('themes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date', sa.Date(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('themes', schema=None) as batch_op:
        batch_op.drop_column('date')

    # ### end Alembic commands ###