"""add film model

Revision ID: 829b7554f62c
Revises: 
Create Date: 2021-04-12 18:52:21.549712

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '829b7554f62c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('films',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('release_date', sa.Date(), nullable=False),
    sa.Column('uuid', sa.String(length=36), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('distributed_by', sa.String(length=120), nullable=False),
    sa.Column('length', sa.Float(), nullable=True),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_films_release_date'), 'films', ['release_date'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_films_release_date'), table_name='films')
    op.drop_table('films')
    # ### end Alembic commands ###
