#!/usr/bin/env python

import codecs

RELEASE_DIR = '../html/'
FILE_NAME_ARR = [
        {'id': 'home', 'name': 'Home', 'link': 'index.html'},
        {'id': 'intro', 'name': 'Introduction', 'link': 'intro.html'},
        {'id': 'staff', 'name': 'Staff', 'link': 'staff.html'},
        {'id': 'teaching', 'name': 'Teaching', 'link': 'teaching.html'},
        {'id': 'papers', 'name': 'Publication', 'link': 'publication.html'},
        {'id': 'competition', 'name': 'Competition', 'link': 'competition.html'},
        {'id': 'software', 'name': 'Software', 'link': 'software.html'},
        {'id': 'seminars', 'name': 'Seminars', 'link': 'seminars.html'},
        {'id': 'announcements', 'name': 'Announcements', 'link': 'announcements.html'},
        {'id': 'opening', 'name': 'Opening', 'link': 'opening.html'},
        ]
HOME_LIMIT = 3
PAGE_LIMIT = 10


def gen_html(data):
    for t in FILE_NAME_ARR:
        hstr = ''
        hstr += gen_header(t)
        hstr += gen_body(t, data)
        hstr += gen_footer(t, data)

        f_name = RELEASE_DIR + t['link']
        with codecs.open(f_name, 'w', "utf-8") as output:
            output.write(hstr)
            output.close()


def gen_body(p, data):
    hstr = ''
    hstr += globals()['gen_body_' + p['id']](p, data)
    return hstr


def gen_body_home(p, data):
    hstr = ''
    hstr += \
            '''
      <div class="row">
        <img class="full_width" src="images/bg.png" alt="CMI"/>
      </div>
            '''

    hstr += \
            '''
      <div class="row" style="display:table;">
        <div class="col-xs-6 ver-line-right" style="display: table-cell; min-height: 100%; float: none;">
          <div class="box-title">
            '''

    t = data['home']['welcome'][0]
    hstr += '<h4>%s</h4>' % t['title']
    hstr += '<p>%s</p>' % t['details']

    hstr += \
            '''
          </div>
        </div>
        <div class="col-xs-6" style="display: table-cell; float: none;">
          <div>
            <div class="box-title">
              <h4>News</h4>
            </div>
            <div class="box-title">
              <ul>
            '''

    index = 0
    for t in data['announcements']['announcement']:
        if t == []:
            continue
        else:
            hstr += '<li>%s</br>%s</li>' % (t['title'], format_app_str(t))
            index += 1
            if index >= HOME_LIMIT:
                break

    hstr += \
            '''
              <ul>
           </div>
          </div>
        </div>    
      </div>
            '''

    return hstr


def gen_body_intro(p, data):
    hstr = ''

    t = data['intro']['content'][0]
    hstr += \
            '''
     <div class="row intro-row">
        <div align="center">
          <h4>%s</h4>
        </div>
      </div>
            ''' % t['title']

    hstr += \
            '''
     <div class="row intro-row">
        <div class="col-xs-12 ver-line-left">
          <div class="box-title">
            <p>%s</p>
          </div>
        </div>
      </div>
            ''' % t['details']
    
    hstr += \
            '''
      <div class="row intro-row">
        <img class="full_width" src="%s" alt="FIT"/>
      </div>
            ''' % t['photo']

    return hstr


def gen_body_seminars(p, data):
    hstr = ''
    hstr += \
            '''
        <div class="box-title box-ul">
          <ul>
            <li>Machine Learning Seminars</li>
          </ul>
        </div>

        <div class="col-xs-12 ver-line-left">
            '''

    for t in data['seminars']['seminar']:
        if t == []:
            continue
        hstr += \
                '''
                <div class="box-item collapse-group">
                  <div class="item-text">
                    <p class="name">%s</p>
                    <p class="title">%s</p>
                    <p class="title">Speaker: <a href="%s" target="_blank">%s</a></p>
                    <p class="title">Place: %s, Time: %s</p>
                    <a class="details expand-click" href="#">View details &raquo;</a>
                  </div>
                ''' % (t['title'], t['date'], t['speaker_homepage'], t['speaker'], t['venue'], t['time'])

        hstr += '<div class="item-text hidden-div" style="display:none;">'
        hstr += '<li style="margin-top: 5px;">Abstract</li>'
        hstr += '<p class="details">%s</p>' % t['abstract']
        if t['speaker_bio'] != '':
            hstr += '<li style="margin-top: 5px;">Bio</li>'
            hstr += '<p class="details">%s</p>' % t['speaker_bio']
        if t['urls'] != '':
            hstr += '<li style="margin-top: 5px;">Links</li>'
            for u in t['urls'].split(','):
                hstr += '<p class="details"><a href="%s" target="_blank">%s</a></p>' % (u, u)
        hstr += '</div>'

        hstr += \
                '''
                  <div class="clear-div"></div>
                  <div class="dashed-line-h"></div>
                </div>
                '''
        
    hstr += '</div>'

    return hstr


def format_app_str(t):
    arr = []
    if t['speaker'] != '':
        arr.append('Speaker: %s' % t['speaker'])
    if t['venue'] != '':
        arr.append('Venue: %s' % t['venue'])
    if t['date'] != '':
        arr.append('Date: %s' % t['date'])
    app_str = '</br>'.join(arr)
    return app_str


def gen_body_announcements(p, data):
    hstr = ''
    hstr += '<div class="row intro-row">'

    for t in data['announcements']['announcement']:
        hstr += \
                '''
            <div class="box-title box-ul">
              <ul>
                <li>%s</li>
              </ul>
            </div>
            <div class="col-xs-12 ver-line-left">
                ''' % (t['title'])

        hstr += \
                '''
          <div class="box-item">
            <div class="item-text bg-green">
              <div class="col-xs-3">
                <p>%s</p>
              </div>
              <div class="col-xs-1">
              </div>
              <div class="col-xs-8">
                <p>%s</p>
              </div>
              <div class="clear-div"></div>
            </div>
          </div>
                ''' % (format_app_str(t), t['details'])
        
        hstr += '</div>'

    hstr += '</div>'

    return hstr


def gen_body_opening(p, data):
    hstr = ''
    t = data['opening']['content'][0]
    hstr += \
            '''
     <div class="row intro-row">
        <div align="center">
          <h4>%s</h4>
        </div>
      </div>
            ''' % t['title']

    hstr += \
            '''
     <div class="row intro-row">
        <div class="col-xs-12 ver-line-left">
          <div class="box-title">
            <p>%s</p>
          </div>
        </div>
      </div>
            ''' % t['details']

    return hstr


def gen_body_staff(p, data):
    hstr = ''
    hstr += '<div class="row intro-row">'

    type_list = ['Faculty', 'Affiliated Faculty', 'Graduate', 'Undergraduate']

    for g in type_list:
        hstr += \
                '''
            <div class="box-title box-ul">
              <ul>
                <li>%s</li>
              </ul>
            </div>
                ''' % g
        hstr += '<div style="min-height: 120px; margin-top: 5px;">'
        hstr += '<div class="col-xs-12 ver-line-left">'

        for t in data['staff']['member']:
            if t == [] or t['type'] != g:
                continue
            hstr += '<div class="box-people">'
            if t['photo'] != '':
                hstr += '<img src="%s" style="width:75px;float:left;" alt=""/>' % t['photo']
            hstr += '<div class="people-text bg-purple">'
            hstr += '<p class="name">%s</p>' % t['name']
            hstr += '<p class="title">%s</p>' % t['role']
            hstr += '<p class="link"><a href="%s" target="_blank">%s</a></p>' % (t['homepage'], t['homepage'])
            if t['interest'] != '':
                hstr += '<p class="interest">%s</p>' % t['interest']
            if t['details'] != '':
                hstr += '<p class="details">%s</p>' % t['details']
            hstr += '</div>'
            hstr += '</div>'
            
        hstr += '</div>'
        hstr += '</div>'

    hstr += \
            '''
        <div class="box-title box-ul">
          <ul>
            <li>Alumi</li>
          </ul>
        </div>
            '''

    hstr += '<div style="min-height: 120px; margin-top: 5px;">'
    hstr += '<div class="col-xs-12 ver-line-left">'
    for t in data['staff']['alumi']:
        if t == []:
            continue
        hstr += '<div class="box-people">'
        if t['photo'] != '':
            hstr += '<img src="%s" style="width:75px;float:left;" alt=""/>' % t['photo']
        hstr += '<div class="people-text bg-purple">'
        hstr += '<p class="name">%s</p>' % t['name']
        hstr += '<p class="title">%s</p>' % t['role']
        hstr += '<p class="title">%s</p>' % t['current_affiliation']
        hstr += '<p class="link"><a href="%s" target="_blank">%s</a></p>' % (t['current_homepage'], t['current_homepage'])
        if t['interest'] != '':
            hstr += '<p class="interest">%s</p>' % t['interest']
        if t['details'] != '':
            hstr += '<p class="details">%s</p>' % t['details']
        hstr += '</div>'
        hstr += '</div>'
    
    hstr += '</div>'
    hstr += '</div>'

    hstr += '</div>'

    return hstr


def gen_body_teaching(p, data):
    hstr = ''
    hstr += '<div class="row intro-row">'
    hstr += \
            '''
        <div class="box-title box-ul">
          <ul>
            <li>Lecture</li>
          </ul>
        </div>
        <div class="col-xs-12 ver-line-left">
            '''

    for t in data['teaching']['lecture']:
        title_html = t['title']
        if t['urls'] != '':
            title_html = '<a href="%s" target=_blank >%s</a>' % (t['urls'].split(',')[0], t['title'])

        hstr += \
                '''
          <div class="box-item collapse-group">
            <div class="item-text bg-green">
              <div class="col-xs-4">
                <p>%s</p>
              </div>
              <div class="col-xs-2">
                <p>%s</p>
              </div>
              <div class="col-xs-2">
                <p>%s</p>
              </div>
              <div class="col-xs-2">
                <p>%s</p>
              </div>
              <div class="col-xs-2">
                <a class="details expand-click" href="#">View details &raquo;</a>
              </div>
              <div class="clear-div"></div>
            </div>
            <div class="item-text bg-green hidden-div" style="display:none;">
              <div class="col-xs-10">
                <p>%s</p>
              </div>
              <div class="col-xs-2">
                <p>%s</p>
              </div>
              <div class="clear-div"></div>
            </div>
          </div>
                ''' % (title_html, t['speaker'], t['date'], t['type'], t['abstract'], t['venue'])

    hstr += '</div>'

    hstr += \
            '''
        <div class="box-title box-ul">
          <ul>
            <li>Seminar</li>
          </ul>
        </div>
        <div class="col-xs-12 ver-line-left">
            '''

    for t in data['teaching']['seminar']:
        hstr += \
                '''
          <div class="box-item collapse-group">
            <div class="item-text bg-yellow">
              <div class="col-xs-4">
                <p>%s</p>
              </div>
              <div class="col-xs-2">
                <p>%s</p>
              </div>
              <div class="col-xs-2">
                <p>%s</p>
              </div>
              <div class="col-xs-2">
                <p>%s</p>
              </div>
              <div class="col-xs-2">
                <a class="details expand-click" href="#">View details &raquo;</a>
              </div>
              <div class="clear-div"></div>
            </div>
            <div class="item-text bg-yellow hidden-div" style="display:none;">
              <div class="col-xs-10">
                <p>%s</p>
              </div>
              <div class="col-xs-2">
              </div>
              <div class="clear-div"></div>
            </div>
          </div>
                ''' % (t['title'], t['speaker'], t['venue'], t['date'], t['abstract'])

    hstr += '</div>'

    hstr += \
            '''
        <div class="box-title box-ul">
          <ul>
            <li>Photo</li>
          </ul>
        </div>
        <div class="col-xs-12 ver-line-left">
          <div class="box-item">
            '''

    index = 0
    bg_str = \
            '''
            '''

    for t in data['teaching']['photo']:
        bg_str += \
                '''
            <a data-toggle="lightbox" data-title="%s" href="%s" data-gallery="teachingimages" class="col-xs-4">
            <img src="%s" alt="Click to view the lightbox" class="img-responsive">
            </a>
                ''' % (t['title'], t['photo'], t['photo'])
        
        index += 1

    hstr += bg_str

    hstr += \
            '''
          </div>
          <div class="clear-div"></div>
        </div>
            '''
    hstr += '</div>'

    return hstr


def gen_body_software(p, data):
    hstr = ''
    hstr += '<div class="row intro-row">'
    hstr += \
            '''
        <div class="box-title box-ul">
          <ul>
            <li>Software</li>
          </ul>
        </div>
        <div class="col-xs-12 ver-line-left">
            '''

    index = 0
    for t in data['software']['items']:
        color = 'bg-green'
        if index%2 == 0:
            color = 'bg-yellow'
        index += 1

        hstr += \
                '''
          <div class="box-item collapse-group">
            <div class="item-text %s">
              <div class="col-xs-4">
                <p>%s</p>
              </div>
              <div class="col-xs-2">
                <p>%s</p>
              </div>
              <div class="col-xs-2">
                <p>%s</p>
              </div>
              <div class="col-xs-2">
              </div>
              <div class="col-xs-2">
                <a class="details expand-click" href="#">View details &raquo;</a>
              </div>
              <div class="clear-div"></div>
            </div>
            <div class="item-text %s hidden-div" style="display:none;">
              <div class="col-xs-10">
                <p>%s</p>
              </div>
              <div class="col-xs-2">
              </div>
              <div class="clear-div"></div>
            </div>
          </div>
                ''' % (color, t['title'], trans_author_str(t['author']), t['date'], color,t['abstract'])

    hstr += '</div>'

    return hstr


def trans_author_str(in_str):
    temp_arr = []
    for tt in in_str.split(','):
        if '#' in tt:
            temp_arr.append('<a href="%s" target=_blank >%s</a>' % (tt.split('#')[1], tt.split('#')[0]))
        else:
            temp_arr.append(tt)

    return ', '.join(temp_arr)


def gen_body_competition(p, data):
    hstr = ''
    hstr += \
            '''
        <div class="box-title box-ul">
          <ul>
            <li>Competition</li>
          </ul>
        </div>
            '''

    hstr += '<div style="min-height: 120px; margin-top: 5px;">'
    hstr += '<div class="col-xs-12 ver-line-left">'
    for t in data['competition']['item']:
        if t == []:
            continue
        hstr += '<div class="box-item">'
        hstr += '<div class="item-text col-xs-6">'
        hstr += '<p class="name">%s</p>' % t['title']
        hstr += '<p class="title">%s</p>' % trans_author_str(t['author'])
        hstr += '<p class="title">%s</p>' % t['date']
        hstr += '<p class="detail">%s</p>' % t['details_html']
        hstr += '</div>'
        if t['photo'] != '':
            hstr += '<img src="%s" alt="CMI" style="width:400px;margin-left:65px;"/>' % t['photo']
        hstr += '<div class="clear-div"></div>'
        hstr += '<div class="dashed-line-h"></div>'
        hstr += '</div>'
    
    hstr += '</div>'
    hstr += '</div>'

    return hstr


def gen_body_papers(p, data):
    hstr = ''
    hstr += \
            '''
      <div class="row intro-row">
        <div id="pub_nav" class="box-title btn-group">
          <button value="all" class="btn btn-default quick-div active">
            <img src="images/publications_11.gif" align="left" alt="CMI" style="float:none;height:32px;" />
            <span> All Publications </span>
          </button>
          <button value="MT" class="btn btn-default quick-div">
            <img src="images/publications_07.gif" align="left" alt="CMI" style="float:none;height:32px;" />
            <span> Machine Translation </span>
          </button>
          <button value="IP" class="btn btn-default quick-div">
            <img src="images/publications_05.gif" align="left" alt="CMI" style="float:none;height:32px;" />
            <span> Image Processing </span>
          </button>
          <button value="ML" class="btn btn-default quick-div">
            <img src="images/publications_09.gif" align="left" alt="CMI" style="float:none;height:32px;" />
            <span> Machine Learning </span>
          </button>
          <!--
          <button value="SR" class="btn btn-default quick-div">
            <img src="images/publications_05.gif" align="left" alt="CMI" style="float:none;height:32px;" />
            <span> Speech Recognition </span>
          </button>
          -->
        </div>
            '''

    hstr += \
            '''
        <div class="box-title box-ul">
          <ul>
            <li>Publication</li>
          </ul>
        </div>

        <div class="col-xs-12 ver-line-left">
            '''

    for t in data['papers']['paper']:
        hstr += \
                '''
          <div class="box-item collapse-group" value="%s">
            <div class="item-text">
              <p class="name">%s</p>
              <p class="title">%s</p>
              <p class="title">%s, %s</p>
              <p class="link"><a href="%s" target="_blank">%s</a></p>
              <a class="details expand-click" href="#">View details &raquo;</a>
            </div>
                ''' % (t['category'], t['title'], trans_author_str(t['author']), t['date'], t['venue'], t['paper_url'], t['fullpaper_url'])

        hstr += '<div class="item-text hidden-div" style="display:none;">'
        hstr += '<li style="margin-top: 5px;">Abstract</li>'
        hstr += '<p class="details">%s</p>' % t['abstract']
        if t['bibtex'] != '':
            hstr += '<li style="margin-top: 5px;">Bibtex</li>'
            hstr += '<p class="details">%s</p>' % t['bibtex']
        hstr += '</div>'

        hstr += \
            '''
            <div class="clear-div"></div>
            <div class="dashed-line-h"></div>
          </div>
            '''

    hstr += '</div>'

    hstr += \
            '''
        <div class="box-title box-ul">
          <ul>
            <li>Patent</li>
          </ul>
        </div>

        <div class="col-xs-12 ver-line-left">
            '''

    for t in data['papers']['patent']:
        hstr += \
                '''
          <div class="box-item collapse-group" value="%s">
            <div class="item-text">
              <p class="name">%s</p>
              <p class="title">%s</p>
              <a class="details expand-click" href="#">View details &raquo;</a>
            </div>
                ''' % (t['category'], t['title'], trans_author_str(t['author']))

        hstr += '<div class="item-text hidden-div" style="display:none;">'
        hstr += '<li style="margin-top: 5px;">Abstract</li>'
        hstr += '<p class="details">%s</p>' % t['abstract']
        hstr += '</div>'

        hstr += \
            '''
            <div class="clear-div"></div>
            <div class="dashed-line-h"></div>
          </div>
            '''

    hstr += '</div>'

    hstr += '</div>'

    return hstr


def gen_header(p):
    hstr = ''
    hstr += \
    '''
<!DOCTYPE html>
<html>
  <head>
    <title>CMI/IIIS - Tsinghua Univ.</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />

    <script type='text/javascript' src='js/jquery.js'></script>
    <script type='text/javascript' src='js/bootstrap.js'></script>
    <script type='text/javascript' src='js/lightbox.js'></script>
    <script type='text/javascript' src='js/basic.js'></script>

    <link rel="stylesheet" type="text/css" href="css/bootstrap.css" media="screen" />
    <link rel='stylesheet' type='text/css' href='css/basic.css' media='screen' />
    '''

    hstr += gen_js(p)

    hstr += \
            '''
  </head>
  <body>
    <div class="container">
      <div class="row logo-row">
        <div id="logo">
          <img src="images/logo.png" align="left" alt="CMI" />
        </div>
      </div>
      <div class="row top-nav">
        <ul class="nav navbar-nav">
          <li><a class='sep-line' >|</a></li>
            '''

    for t in FILE_NAME_ARR:
        hstr += '<li '
        if t['id'] == p['id']:
            hstr += 'class="active"'
        hstr += '><a href="%s">%s</a></li>' % (t['link'], t['name'])
        hstr += '<li><a class="sep-line">|</a></li>'

    hstr += \
            '''
        </ul>
      </div>
            '''

    return hstr


def gen_js(p):
    # TODO
    hstr = ''
    if p['id'] in ['papers', 'seminars', 'teaching', 'software']:
        hstr += \
        '''
<script type="text/javascript">
$(function() {
    $('a.expand-click').on('click', function(e) {
        e.preventDefault();
        var act_div = $(this).closest('.collapse-group').find('.hidden-div');
        act_div.slideToggle();
    });
});
</script>
        '''

    if p['id'] == 'papers':
        hstr += \
        '''
<script type="text/javascript">
$(function() {
    $('#pub_nav button').on('click', function(e) {
        var this_div = $(this);
        $('#pub_nav button').removeClass('active');
        this_div.addClass('active');

        var active_val = this_div.val();
        if (active_val === 'all') {
            $('.box-item').show();
        } else {
            $('.box-item').hide();
            $('.box-item[value='+active_val+']').show();
        }
    });
});
</script>
        '''

    if p['id'] == 'people':
        hstr += \
        '''
<script type="text/javascript">
</script>
        '''
    return hstr


def gen_footer(p, data):
    hstr = ''
    
    hstr += \
            '''
      <div class="row">
        <div class="separator-line"></div>
        <a href="http://www.iiis.tsinghua.edu.cn">
        <img src="images/logo-thu.png" align="right" style="width: 80px; margin-top: -10px; margin-left: -80px;" alt="CMI">
        </a>
        <p class="footer-text">Copyright &copy; 2013 CMI, Tsinghua University. All rights reserved.</p>
      </div>
    </div>
            '''

    hstr += \
            '''
  </body>
</html>
            '''

    return hstr


