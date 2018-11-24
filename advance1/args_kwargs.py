
def test_var_args(f_arg, *argv):
    print ("first normal arg:", f_arg)
    for arg in argv:
        print ("another arg through *argv :", arg)

def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print ("%s == %s" %(key,value))

def main():
	test_var_args('yasoob','python','eggs','test')
	greet_me(kwargs_1="Shark", kwargs_2=4.5, kwargs_3=True)
	print ()
	greet_me(name="dk", id=3522, kwargs_3=False)
	
if __name__ == '__main__':
	main()

