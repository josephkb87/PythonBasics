$images = array("your-file.jpg"); //You can use a URL as well

$pdf = new Imagick($images);
$pdf->setImageFormat('pdf');
$pdf->writeImages('combined.pdf', true); //The file name

//When ran, it will save in the same directory as the php file/script