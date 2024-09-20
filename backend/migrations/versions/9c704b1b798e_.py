"""empty message

Revision ID: 9c704b1b798e
Revises: 8400e1f91b10
Create Date: 2024-09-20 13:51:09.456108

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c704b1b798e'
down_revision = '8400e1f91b10'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('signup_date',
               existing_type=sa.DATE(),
               type_=sa.DateTime(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('signup_date',
               existing_type=sa.DateTime(),
               type_=sa.DATE(),
               existing_nullable=True)

    # ### end Alembic commands ###
