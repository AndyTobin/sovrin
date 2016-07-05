

def testListIds(cli):
    cli.enterCmd("new_keypair test")
    assert len(cli.defaultClient.signers) == 2
    pubKeyMsg = cli.lastPrintArgs['msg']
    assert pubKeyMsg.startswith('Public key is')
    pubKey = pubKeyMsg.split(" ")[-1]
    cli.enterCmd("list ids")
    assert cli.lastPrintArgs['msg'] == "test"

