"""Add Department

Revision ID: 496601c2165e
Revises: fecaaba6ab31
Create Date: 2024-02-12 14:06:55.019268

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '496601c2165e'
down_revision = 'fecaaba6ab31'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    # ### end Alembic commands ###
