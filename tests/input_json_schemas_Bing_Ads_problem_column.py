
"""
if you remove this key-value pair, then JSON schema conversion works with either method 1 or 2

"TaxCertificates":{"type":["null","object"],"properties": {
                    "KeyValueOfstringbase":{"type":["null","array"],"items":"KeyValueOfstringbase"}}},

"""


problem_schema = """
{"type":"SCHEMA",

"stream":"accounts",

"schema":

    {"type":["null","object"],

        "additionalProperties":false,

        "properties":{
            
            "SoldToPaymentInstrumentId":{"type":["null","integer"]},
            
            "TaxCertificate":{"type":["null","object"],"additionalProperties":false,"properties":{
                "TaxCertificateBlobContainerName":{"type":["null","string"]}, 

                "TaxCertificates":{"type":["null","object"],"properties": {
                    "KeyValueOfstringbase":{"type":["null","array"],"items":"KeyValueOfstringbase"}}},

                "Status":{"type":["null","string"]}}
                            }
        
        }
    
    },"key_properties":[]
    
}
"""


# this schema is the same as the one above, but because it's a dictionary, it's easier to see its structure
problem_schema_dict = {"type":"SCHEMA",

"stream":"accounts",

"schema":

    {"type":["null","object"],

        "additionalProperties":False,

        "properties":{
            
            "SoldToPaymentInstrumentId":{"type":["null","integer"]},
            
            "TaxCertificate":{"type":["null","object"],"additionalProperties":False,"properties":{
                "TaxCertificateBlobContainerName":{"type":["null","string"]}, 

                "TaxCertificates":{"type":["null","object"],"properties": {
                    "KeyValueOfstringbase":{"type":["null","array"],"items":"KeyValueOfstringbase"}}},

                "Status":{"type":["null","string"]}}
                            }
        
        }
    
    },"key_properties":[]
    
}




