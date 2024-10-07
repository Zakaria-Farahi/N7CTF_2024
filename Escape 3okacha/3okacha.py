from math import *
Blacklisted = ["import",')','(',"'",'"',".","{",'#',"_",'}','%',"@","!",">","<","$","\\","~","?",";",":","system","exec","execl","python","hhhhhhhhhhhhhhh","charikat dajaj","flag{bniytk}","hayfa2 wahbi","eval","include",
    "eval",
    "exec",
    "input",
    "os.system",
    "subprocess.Popen",
    "subprocess.call",
    "subprocess.run",
    "pickle.load",
    "marshal.load",
    "open",
    "shutil.rmtree",
    "shutil.move",
    "shutil.copyfile",
    "shutil.copytree",
    "os.remove",
    "os.rmdir",
    "os.chdir",
    "os.chmod",
    "os.chown",
    "os.link",
    "os.symlink",
    "os.rename",
    "os.walk",
    "os.popen",
    "getattr",
    "setattr",
    "delattr",
    "globals",
    "locals",
    "compile",
    "super",
    "ctypes.CDLL",
    "ctypes.windll",
    "ctypes.PyDLL",
    "ctypes.pointer",
    "socket",
    "http.client.HTTPConnection",
    "http.client.HTTPSConnection",
    "xml.etree.ElementTree.parse",
    "xml.etree.ElementTree.fromstring",
    "xml.sax.make_parser",
    "xmlrpc.client.ServerProxy",
    "xmlrpc.server.SimpleXMLRPCServer",
    "xml.dom.minidom.parse",
    "xml.dom.minidom.parseString",
    "json.load",
    "json.loads",
    "yaml.load",
    "ast.literal_eval",
    "ast.parse",
    "ast.dump",
    "ast.NodeVisitor.visit",
    "re.compile",
    "re.sub",
    "hashlib.md5",
    "hashlib.sha1",
    "hashlib.new",
    "random.seed",
    "random.random",
    "random.randint",
    "random.choice",
    "tempfile.mktemp",
    "tempfile.mkdtemp",
    "sys.setrecursionlimit",
    "sys.exit",
    "sys._getframe",
    "sys.modules",
    "logging.basicConfig",
    "sqlite3.connect",
    "pymysql.connect",
    "pymongo.MongoClient",
    "ftplib.FTP",
    "smtplib.SMTP",
    "ssl.wrap_socket",
    "paramiko.SSHClient",
    "binascii.a2b_base64",
    "binascii.b2a_base64",
    "inspect.getmembers",
    "inspect.getmodule",
    "inspect.getsource",
    "tarfile.open",
    "zipfile.ZipFile",
    "glob.glob",
    "multiprocessing.Process",
    "multiprocessing.Pool",
    "threading.Thread",
    "concurrent.futures.ProcessPoolExecutor",
    "concurrent.futures.ThreadPoolExecutor",
    "time.sleep",
    "signal.alarm",
    "signal.pause",
]


quote = """
hacker.target = target
while True:
	hacker.see()
	hacker.learn()
	hacker.see_with_passion()
	hacker.learn()
	hacker_see()
	detect = hacker.detect()
	if detect:
		hacker.exploit()
		break

this is not a part of the challenge it's an life style
"""

print("Welcome to python secure calculator")
while True:
	execute = True
	command = str(input(">>>"))
	for b in Blacklisted :
		if b in command :
			print(quote)
			print("are you smayka ?")
			execute = False
			break
	if execute :
		try:
			if exec(command) == None: # check the expression is correct
				print(eval(command))
		except Exception as e:
			print("dik chi herban",e)

















