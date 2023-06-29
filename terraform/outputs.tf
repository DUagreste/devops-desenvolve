output "ip-dev0" {
    value = "${aws_instance.dev[0].public_ip}"
}

output "ip-dev1" {
    value = "${aws_instance.dev[1].public_ip}"
}

output "ip-dev2" {
    value = "${aws_instance.dev[2].public_ip}"
}