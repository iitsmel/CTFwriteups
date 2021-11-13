#!c:/perl
use Crypt::Blowfish;

while ($pass = <>)
{
    chomp $pass; 
    $key = pack ("H16","0123456789ABCDEF");
    $cipher = new Crypt::Blowfish $key;
    $ciphertext = $cipher->decrypt("$pass");
    print unpack ("H16",$ciphertext),"\n";
}