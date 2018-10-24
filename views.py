#-*- coding:utf-8 -*-
def acc_login(request):
	err_msg = {}
	today_str = datetime.date.today().strftime("%Y%m%d")
	verify_code_img_path = "%s/%s" %(settings.VERIFICATION_CODE_IMGS_DIR,
									today_str)
	if not os.path.isdir(verify_code_img_path):
		os.makedirs(verify_code_img_path,exist_ok=True)
	print("session:",request.session.session_key)
	random_filename = "".join(random.sample(string.ascii_lowercase,4))
	random_code = verify_code.gene_code(verify_code_img_path,random_filename)
	cache.set(random_filename, random_code,30) #设置缓存30秒
	
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		_verify_code = request.POST.get('verify_code')
		_verify_code_key = request.POST.get('verify_cpde_key')
		
		print("verify_code_key:",_verify_code_key)
		print("verify_code:",_verify_code)
		if cache.get(_verify_code_key) == _verify_code:
			print("code verification pass!")
			
			user = authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				request.session.set_expiry(60*60)
				return HttpResponseRedirect(request.GET.get("next") if request.GET.get("next") else "/")
			else:
				err_msg["error"] = 'Wrong username or password!'
				
	else:
		err_msg['error'] = '验证码错误！'

return render(request,'login.html',{"filename":random_filename,"today_str":today_str, "error":error_msg})
	
	