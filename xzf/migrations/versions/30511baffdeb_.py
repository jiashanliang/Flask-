"""empty message

Revision ID: 30511baffdeb
Revises: 8a36bb65e4f1
Create Date: 2018-10-20 14:33:38.573935

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '30511baffdeb'
down_revision = '8a36bb65e4f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog', sa.Column('b_active', sa.Boolean(), nullable=True))
    op.add_column('blog', sa.Column('id', sa.Integer(), autoincrement=True, nullable=False))
    op.create_unique_constraint(None, 'blog', ['b_title'])
    op.drop_column('blog', 'b_id')
    op.add_column('collection', sa.Column('b_id', sa.Integer(), nullable=True))
    op.add_column('collection', sa.Column('u_id', sa.Integer(), nullable=True))
    op.drop_constraint('collection_ibfk_1', 'collection', type_='foreignkey')
    op.drop_constraint('collection_ibfk_2', 'collection', type_='foreignkey')
    op.create_foreign_key(None, 'collection', 'blog', ['b_id'], ['id'])
    op.create_foreign_key(None, 'collection', 'user', ['u_id'], ['id'])
    op.drop_column('collection', 'c_u_id')
    op.drop_column('collection', 'c_b_id')
    op.add_column('user', sa.Column('id', sa.Integer(), autoincrement=True, nullable=False))
    op.drop_column('user', 'u_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('u_id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False))
    op.drop_column('user', 'id')
    op.add_column('collection', sa.Column('c_b_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('collection', sa.Column('c_u_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'collection', type_='foreignkey')
    op.drop_constraint(None, 'collection', type_='foreignkey')
    op.create_foreign_key('collection_ibfk_2', 'collection', 'user', ['c_u_id'], ['u_id'])
    op.create_foreign_key('collection_ibfk_1', 'collection', 'blog', ['c_b_id'], ['b_id'])
    op.drop_column('collection', 'u_id')
    op.drop_column('collection', 'b_id')
    op.add_column('blog', sa.Column('b_id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False))
    op.drop_constraint(None, 'blog', type_='unique')
    op.drop_column('blog', 'id')
    op.drop_column('blog', 'b_active')
    # ### end Alembic commands ###
