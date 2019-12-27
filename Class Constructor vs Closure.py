# From http://blog.dhananjaynene.com/2013/10/partially-applied-functions-and-decorators-in-python/
# It is not uncommon to see classes with only one significant public method.
# In many such scenarios, the class constructor is used to specify the arguments of the method, and the method itself is used to perform the desired behaviour.
# This gives us temporal separation (object construction and method execution) and encapsulation of the arguments.
# It so happens the same can be done through using closures as well. (Note: although the example below is quite similar to the one above they serve to describe different intents)


# traditional method
class Connection(object):
    def __init__(userid, password):
        self.userid = self.userid
        self.password = self.password

    def execute(sql):
        # execute SQL using userid, password.
        # return results

c = Connection("myuserid", "mypassword")
c.execute("select 'x' from dual;")

# Using closures
def get_connection(userid, password):
    def execute(sql):
        # execute SQL using userid, password & sql
        # return results
    return execute

c = get_connection("myuserid", "mypassword")
c("select 'x' from dual;")
