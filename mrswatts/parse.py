try:
    import android
except:
    pass

import sys


def messages(tag, contacts):

    dict_contact = {}
    for contact in contacts.splitlines():
        id = contact.split('|')[0]
        name = contact.split('|')[1]
        dict_contact[id] = name

    summary = []
    lines = tag.splitlines()
    for line in lines:
        person = line.split('|')[0]
        data = line.split('|')[1].replace('@cabin', '').strip()
        summary.append(dict_contact[person] + ': ' + data)
    return "\n".join(summary)

if __name__ == "__main__":
    try:
        droid = android.Android()
    except:
        pass
    try:
        lines = droid.getIntent().result[u'extras'][u'%lines']
    except:
        droid.makeToast('data missing')
        sys.exit(1)

    try:
        line_number = int(droid.getIntent().result[u'extras'][u'%line_number'])
    except:
        line_number = 0

    try:
        position = int(droid.getIntent().result[u'extras'][u'%position'])
    except:
        position = 0

    droid.makeToast(position)
    droid.makeToast(lines.splitlines()[line_number].split('|')[position].strip())
    droid.setClipboard(lines.splitlines()[line_number].split('|')[position].strip())
