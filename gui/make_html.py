#!/usr/bin/env python

import codecs

RELEASE_DIR = '../html/'
FILE_NAME_ARR = [
        {'id': 'home', 'name': 'Home', 'link': 'index.html'},
        {'id': 'intro', 'name': 'Introduction', 'link': 'intro.html'},
        {'id': 'staff', 'name': 'Staff', 'link': 'staff.html'},
        {'id': 'teaching', 'name': 'Teaching', 'link': 'teaching.html'},
        {'id': 'papers', 'name': 'Publication', 'link': 'publication.html'},
        {'id': 'projects', 'name': 'Projects', 'link': 'projects.html'},
        {'id': 'software', 'name': 'Software', 'link': 'software.html'},
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
      <div class="row">
        <div class="col-xs-6 ver-line-right">
          <div class="box-title">
            '''

    t = data['home']['welcome'][0]
    hstr += '<h4>%s</h4>' % t['title']
    hstr += '<p>%s</p>' % t['details']

    hstr += \
            '''
          </div>
        </div>
        <div class="col-xs-6">
          <div>
            <div class="box-title">
              <h4>News</h4>
            </div>
            <div class="box-title">
              <ul>
            '''

    index = 0
    for t in data['home']['news']:
        hstr += '<li>%s</li>' % t['title']
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

    type_list = ['Faculty', 'Graduate', 'Undergraduate']

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
        hstr += \
                '''
          <div class="box-item">
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
                <p>%s</p>
              </div>
              <div class="clear-div"></div>
            </div>
          </div>
                ''' % (t['title'], t['type'], t['speaker'], t['venue'], t['date'])

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
          <div class="box-item">
            <div class="item-text bg-yellow">
              <div class="col-xs-4">
                <p>%s</p>
              </div>
              <div class="col-xs-2">
                <p>More Details</p>
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
              <div class="clear-div"></div>
            </div>
          </div>
                ''' % (t['title'], t['speaker'], t['venue'], t['date'])

    hstr += '</div>'

    t = data['teaching']['photo'][0]
    hstr += \
            '''
        <div class="box-title box-ul">
          <ul>
            <li>Photo</li>
          </ul>
        </div>
        <div class="col-xs-12 ver-line-left">
          <div class="box-item">
            <img class="full_width" src="%s" alt="FIT"/>
          </div>
        </div>
            ''' % t['photo']

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
          <div class="box-item">
            <div class="item-text %s">
              <div class="col-xs-4">
                <p>%s</p>
              </div>
              <div class="col-xs-2">
                <p>Links</p>
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
              <div class="clear-div"></div>
            </div>
          </div>
                ''' % (color, t['title'], trans_author_str(t['author']), t['venue'], t['date'])

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


def gen_body_projects(p, data):
    hstr = ''
    hstr += \
            '''
        <div class="box-title box-ul">
          <ul>
            <li>Projects</li>
          </ul>
        </div>
            '''

    hstr += '<div style="min-height: 120px; margin-top: 5px;">'
    hstr += '<div class="col-xs-12 ver-line-left">'
    for t in data['projects']['project']:
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
        <div class="box-title box-ul">
          <div id="ma_trans" class="quick-div">
            <img src="images/publications_07.gif" align="left" alt="CMI" style="float:none;height:32px;" />
            <span> Machine Translation </span>
          </div>
          <div id="im_proc" class="quick-div">
            <img src="images/publications_09.gif" align="left" alt="CMI" style="float:none;height:32px;" />
            <span> Image Processing </span>
          </div>
          <div id="ma_learn" class="quick-div">
            <img src="images/publications_03.gif" align="left" alt="CMI" style="float:none;height:32px;" />
            <span> Machine Learning </span>
          </div>
          <div id="sp_reco" class="quick-div">
            <img src="images/publications_05.gif" align="left" alt="CMI" style="float:none;height:32px;" />
            <span> Speech Recognition </span>
          </div>
          <div id="so_netw" class="quick-div">
            <img src="images/publications_11.gif" align="left" alt="CMI" style="float:none;height:32px;" />
            <span> Social Network </span>
          </div>
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
          <div class="box-item">
            <div class="item-text">
              <p class="name">%s</p>
              <p class="title">%s</p>
              <p class="title">%s</p>
              <p class="title">%s, %s</p>
              <p class="link"><a href="%s" target="_blank">%s</a></p>
              <p class="detail">More Details</p>
            </div>
            <div class="clear-div"></div>
            <div class="dashed-line-h"></div>
          </div>
                ''' % (t['title'], t['category'], trans_author_str(t['author']), t['date'], t['venue'], t['paper_url'], t['fullpaper_url'])

    hstr += \
            '''
        </div>
      </div>
            '''

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
    if p['id'] == 'papers':
        hstr += \
        '''
<script type="text/javascript">
</script>
        '''
    elif p['id'] == 'people':
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


