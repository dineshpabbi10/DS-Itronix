import json
myjson='''
{
"status":"ok",
"source":"itronix",
"value":"id"
}
'''
a=json.loads(myjson)
print a["source"]

