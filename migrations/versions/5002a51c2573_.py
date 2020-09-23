"""empty message

Revision ID: 5002a51c2573
Revises: 
Create Date: 2020-09-22 23:53:22.041263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5002a51c2573'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article',
    sa.Column('article_id', sa.Integer(), nullable=False),
    sa.Column('article_name', sa.String(length=255), nullable=True),
    sa.Column('article_tag', sa.String(length=255), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.Column('reading_number', sa.Integer(), nullable=True),
    sa.Column('edit_user', sa.String(length=50), nullable=True),
    sa.Column('comment_number', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('article_id')
    )
    op.create_table('blog_config',
    sa.Column('system_id', sa.Integer(), nullable=False),
    sa.Column('visitors_number', sa.Integer(), nullable=True),
    sa.Column('authority', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('system_id')
    )
    op.create_table('blog_tag',
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.Column('tag_name', sa.String(length=32), nullable=True),
    sa.Column('is_valid', sa.Boolean(), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('tag_id')
    )
    op.create_index(op.f('ix_blog_tag_tag_name'), 'blog_tag', ['tag_name'], unique=True)
    op.create_table('blog_visit',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.Integer(), nullable=True),
    sa.Column('system', sa.String(length=64), nullable=True),
    sa.Column('browser', sa.String(length=64), nullable=True),
    sa.Column('ip', sa.Integer(), nullable=True),
    sa.Column('visitors_number', sa.Integer(), nullable=True),
    sa.Column('last_time', sa.DateTime(), nullable=True),
    sa.Column('access_rights', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('comment',
    sa.Column('comment_id', sa.Integer(), nullable=False),
    sa.Column('topic_id', sa.Integer(), nullable=True),
    sa.Column('content', sa.String(length=255), nullable=True),
    sa.Column('from_uid', sa.Integer(), nullable=True),
    sa.Column('comment_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('comment_id')
    )
    op.create_table('reply',
    sa.Column('reply_id', sa.Integer(), nullable=False),
    sa.Column('comment_id', sa.Integer(), nullable=True),
    sa.Column('content', sa.String(length=255), nullable=True),
    sa.Column('from_uid', sa.Integer(), nullable=True),
    sa.Column('comment_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('reply_id')
    )
    op.create_table('statistics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pv_h', sa.Integer(), nullable=True),
    sa.Column('pv_n', sa.Integer(), nullable=True),
    sa.Column('uv_h', sa.Integer(), nullable=True),
    sa.Column('uv_n', sa.Integer(), nullable=True),
    sa.Column('ip_h', sa.Integer(), nullable=True),
    sa.Column('ip_n', sa.Integer(), nullable=True),
    sa.Column('vv_h', sa.Integer(), nullable=True),
    sa.Column('vv_n', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('s_name', sa.String(length=20), nullable=True),
    sa.Column('s_password', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('system_user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=50), nullable=False),
    sa.Column('user_avatar', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('create_at', sa.Integer(), nullable=True),
    sa.Column('update_at', sa.Integer(), nullable=True),
    sa.Column('authority', sa.String(length=255), nullable=True),
    sa.Column('is_valid', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=16), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('system_user')
    op.drop_table('student')
    op.drop_table('statistics')
    op.drop_table('reply')
    op.drop_table('comment')
    op.drop_table('blog_visit')
    op.drop_index(op.f('ix_blog_tag_tag_name'), table_name='blog_tag')
    op.drop_table('blog_tag')
    op.drop_table('blog_config')
    op.drop_table('article')
    # ### end Alembic commands ###