# -*- encoding: utf-8 -*-
##############################################################################
#
#    Website Blog - Disqus module for Odoo
#    Copyright (C) 2016- XUBI.ME (http://www.xubi.me)
#    @author binhnguyenxuan (https://www.linkedin.com/in/binh-nguyen-xuan-46556279)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Website Blog - Disqus',
    'summary': 'Website_Blog - DISQUS Integration',
    'version': '9.0.1.0.0',
    'category': 'Website',
    'summary': """
Website_Blog - DISQUS Integration
""",
    'author': "binhnguyenxuan (www.xubi.me)",
    'website': 'http://www.xubi.me',
    'license': 'AGPL-3',
    'depends': [
        'website_blog',
    ],
    'data': [
        'views/website_config_settings_views.xml',
        'templates/website_blog_templates.xml',
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
}