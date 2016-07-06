===================
Website Blog - Disqus Integration module for Odoo
===================

This project aims to integrate Disqus comments for all of Blog post

Installation
============

Installation process is at present stage only possible in manual way.
Then go to you odoo webinterface to the module section and start "Update module list". Then look for the "Website Blog - Disqus" in Apps (module list) and install.
I hope you enjoy checking out what all you can do with this application.


Prerequisite
============
Before installing the module make sure that the you have configured an addon path for custom addons. In a Linux system the parameter in the config file usually looks similar as the following example:
specify additional addons paths (separated by commas)
addons_path = /opt/odoo/odoo-server/addons, /opt/odoo/custom/addons
In this case you have to install the modules into /opt/odoo/custom/addons. At the present stage on dependency could not automatically resolved so you have to install one extra module that vertical community depends on.

Usage
====
Maybe images in github do not fit with the Odoo apps, so you can check: https://apps.odoo.com/apps/modules/9.0/website_blog_disqus/ for more details.
Thank you.


Configuration
============

Create your Disqus account at: https://disqus.com/
-------------------------------------------------

Get your universal code at: https://disqus.com/admin/universalcode/
------------------------------------------------------------------
|
.. figure:: universal_code.jpg
   :scale: 80 %
   :alt: Get disqus Universal Code
|
Actually you just need remember your disqus_account
|
Config with Odoo
---------------
|
.. figure:: config.jpg
   :scale: 80 %
   :alt: Config Disqus with your disqus account