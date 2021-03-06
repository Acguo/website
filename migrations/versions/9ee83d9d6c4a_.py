"""empty message

Revision ID: 9ee83d9d6c4a
Revises: 101514f15fbc
Create Date: 2018-08-06 11:31:02.671106

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ee83d9d6c4a'
down_revision = '101514f15fbc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movie',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('href', sa.String(length=200), nullable=True),
    sa.Column('picsrc', sa.String(length=200), nullable=True),
    sa.Column('tag_list', sa.String(length=200), nullable=True),
    sa.Column('country', sa.String(length=20), nullable=True),
    sa.Column('years', sa.String(length=20), nullable=True),
    sa.Column('grade', sa.String(length=20), nullable=True),
    sa.Column('intro', sa.TEXT(), nullable=True),
    sa.Column('nums', sa.String(length=100), nullable=True),
    sa.Column('star_list', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movie')
    # ### end Alembic commands ###
