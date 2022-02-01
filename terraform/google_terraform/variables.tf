variable "credentials" {
  description = "google service account"
}

variable "project_id" {
  description = "project id"
}

variable "region" {
  description = "region"
  default = "europe-west1"
}

variable "network" {
  description = "The VPC network created to host the cluster in"
  default     = "ah-network"
}
variable "subnetwork" {
  description = "The subnetwork created to host the cluster in"
  default     = "ah-subnet"
}

variable "ip_range_pods_name" {
  description = "The secondary ip range to use for pods"
  default     = "ip-range-pods"
}
variable "ip_range_services_name" {
  description = "The secondary ip range to use for services"
  default     = "ip-range-services"
}
