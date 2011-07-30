#!/usr/bin/env python2
# -*- coding: utf-8 -*-

menu_cmd = (
    ('Capture Entire Screen', 'scru -s -d2 -noup'),
    ('Capture Window or Area', 'scru -sw -d2 -noup'),
    ('Capture Entire Screen &amp; Upload', 'scru -sn -d2 -q0'),
    ('Capture Window or Area &amp; Upload', 'scru -snw -d2 -q0'))

print('<openbox_pipe_menu>')
for label, command in menu_cmd:
    print('  <item label="%s">' % label)
    print('    <action name="Execute">')
    print('      <execute>')
    print('        %s' % command)
    print('      </execute>')
    print('    </action>')
    print('  </item>')
print('</openbox_pipe_menu>')


