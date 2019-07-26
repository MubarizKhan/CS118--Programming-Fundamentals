import subprocess
import os

fn = 'a13'
gpp_path = None

def setup_module(module):
    global gpp_path
    try_paths = [['C:%s'%os.sep, 'Program Files (x86)', 'Dev-Cpp'],
                 ['C:%s'%os.sep, 'Program Files', 'Dev-Cpp'],
                 ['/', 'usr', 'bin']]


    tried_paths = []
    for p in try_paths:
        path = os.path.join(*p)  # splat the list

        gpp_name = 'g++'
        if os.name == 'nt': gpp_name += '.exe'  # windows!

        exec_path = find(gpp_name, path)
        if exec_path is not None:
            gpp_path = exec_path  # gotcha
            return
        tried_paths.append(path)

    assert False, """Failed to find g++ in any known location. Make sure you have one of the following in the default paths:
        - *nix or Mac (we'll look for g++ in /usr/bin)
        - Dev-CPP IDE installed in
        - Cygnus distribution, see here http://www1.cmc.edu/pages/faculty/alee/g++/g++.html

        Looked in:
        """ + str(tried_paths)


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


def teardown_module(module):
    # cleanup()  # cleanup at end to remove object code file
    pass

def compile_program():
    if gpp_path is None:
        assert False, "No g++, cannot continue."

    args = [gpp_path, fn+'.cpp', '-o', fn+'.out', '-w'] # suppress warning (for windows)
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()

    print err
    # print '[', out, ']'
    return (err == '' or err == None) # no error means we compiled fine

def cleanup():
    import os
    frem = fn + '.out'
    if os.path.exists(frem):
        os.remove(frem)

def check_cmd_output(ground, extra_args = None):
    args = ['./' + fn + '.out']
    if extra_args is not None:
        args.extend(extra_args)

    print "Running with args:", args

    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    # windows and it's \r issue
    out_stripped = [i.strip() for i in out.split('\n') if i.strip() != '']
    assert out_stripped == ground


def test_compile():
    res = compile_program()
    assert res


##### TESTS START HERE  ####################

def test_add_s_0():
    args = ['128', '985']
    ground = ['1113']
    check_cmd_output(ground, args)

def test_add_s_1():
    args = ['83758574635364537465746355928476867', '83758574635364537465746355928476867']
    ground = ['167517149270729074931492711856953734']
    check_cmd_output(ground, args)

def test_add_s_2():
    args = ['0', '0']
    ground = ['0']
    check_cmd_output(ground, args)

def test_add_s_3():
    args = ['9238958375668347483475634840234834723562394873562349872356234987356234987347234862348',
            '2389583756683474834756348402348347235623948735623498723562349873562349873472348623489']
    ground = ['11628542132351822318231983242583181959186343609185848595918584860918584860819583485837']
    check_cmd_output(ground, args)
