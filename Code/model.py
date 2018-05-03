# -*- coding: utf-8 -*-

db.define_table('profile',
                   Field('fname', label="First Name"),
                   Field('lname', label="Last Name"),
                   Field('email',label="Email"),
                   Field('phone',label="Phone"),
                   Field('locationfortea',label="Location"),
                   Field('dayfortea',label="Day For Tea"),
                   Field('timefortea',label="Time For Tea"),
                   Field('otherpartyfname',label="Other Parties First Name"),
                   Field('otherpartylname',label="Other Parties Last Name"),
                   Field('otherpartyemail',label="Other Parties Email"),
                   Field('otherpartycomment', label="Other Party Comment"),
                   Field('otherpartyapprove', 'boolean', label="Other Party Approval"),
                   Field('otherpartyphone',label="Other Parties Phone Number"))

db.define_table('stored_item',
                Field('title', label="Title"),
                   Field('subject',label="Subject"),
                   Field('description', 'text', label="Description"),
                   Field('url', label="Url"), plural="Databases")


db.stored_item._enable_record_versioning(archive_db=db,
                                         archive_name='stored_item_archive',
                                         current_record='current_record',
                                         is_active='is_active')