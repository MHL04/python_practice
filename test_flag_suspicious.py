from Log_Analyzer import  flag_suspicious


def test_flag_suspicious():
    ip ={
        '192.168.2.10': {'failed': 1, 'success': 1, 'usernames': {'smith'}},
        '192.168.5.10': {'failed': 6, 'success': 2, 'usernames': {'jack'}},
        '192.168.6.10': {'failed': 7, 'success': 6, 'usernames': {'oriol'}}
        
    }
    result = flag_suspicious(ip)
    assert result == {
        "192.168.5.10": {'failed' : 6 , 'success': 2, 'usernames': {'jack'}}, 
        '192.168.6.10': {'failed': 7, 'success': 6, 'usernames': {'oriol'}}           
                      
                      }
    
