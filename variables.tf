variable "project_name" {
  description = "Name of the project"
  type        = string
  default     = "Azure_rg"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "dev"
}

variable "location" {
  description = "Azure region"
  type        = string
  default     = "Central India"
}
