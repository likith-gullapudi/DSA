from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'AWS Cloud Practitioner', 0, 1, 'C')
        self.ln(10)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

# Create instance of PDF class
pdf = PDF()

# Add a page
pdf.add_page()

# Title
pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 10, 'AWS Cloud Practitioner', 0, 1, 'C')
pdf.ln(10)

# Brief Report
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'BRIEF REPORT', 0, 1, 'C')
pdf.ln(10)

# Submitted To
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Submitted To:', 0, 1)
pdf.set_font('Arial', '', 12)
pdf.cell(0, 10, 'SHAIK KHASIM BASHA', 0, 1)
pdf.ln(10)

# Submitted By
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Submitted By:', 0, 1)
pdf.set_font('Arial', '', 12)
pdf.cell(0, 10, 'REGETI GYANAKAUSHIK', 0, 1)
pdf.cell(0, 10, '21BCE9209', 0, 1)
pdf.ln(10)

# Abstract
pdf.chapter_title('ABSTRACT:')
abstract = """The purpose of the AWS Cloud Practitioner certification is to provide candidates with a foundational understanding of the Amazon Web Services (AWS) cloud platform, enabling them to effectively demonstrate their overall grasp of the AWS Cloud. This certification targets individuals in technical, managerial, sales, purchasing, or financial roles within an organization. It serves as an entry-level credential. The certification encompasses a broad range of topics essential for cloud literacy, including cloud concepts, AWS core services, security, architecture, cost management, and support.

The course begins with the basics of cloud computing, highlighting the benefits of cloud adoption such as scalability, elasticity, agility, and cost efficiency. It delves into essential AWS services, including database services like RDS, storage services like S3, and compute services like EC2. The certification also emphasizes shared responsibility, compliance controls, and best practices related to the AWS security model.

To grasp how AWS ensures high availability and fault tolerance, one must understand its global infrastructure, which consists of regions and availability zones. The certification also covers fundamental architectural principles, helping students design scalable and reliable applications on the AWS platform.

A crucial aspect of the AWS Cloud Practitioner certification is cost management and optimization. The certification explains the pay-as-you-go model and other AWS pricing models, equipping learners with the knowledge and skills to manage and optimize costs using AWS Budgets and AWS Cost Explorer. Upon completing the certification, candidates will have a solid understanding of AWS cloud concepts, positioning them to contribute effectively to cloud-related initiatives within their organizations."""
pdf.chapter_body(abstract)

# Introduction
pdf.chapter_title('INTRODUCTION:')
introduction = """The AWS Certified Cloud Practitioner (CLF-C02) exam is designed for individuals who can demonstrate a comprehensive understanding of the AWS Cloud, regardless of their specific job role.

The exam validates a candidate’s ability to:

- Explain the value of the AWS Cloud.
- Understand and articulate the AWS shared responsibility model.
- Recognize security best practices.
- Comprehend AWS Cloud costs, economics, and billing practices.
- Describe and position the core AWS services, including compute, network, database, and storage services.
- Identify AWS services for common use cases.

The AWS Certified Cloud Practitioner certification is an entry-level credential provided by Amazon Web Services (AWS) for individuals seeking to demonstrate their overall understanding of the AWS Cloud. It is ideal for those in non-technical roles who need a basic understanding of the AWS Cloud, as well as for those in technical roles who require foundational knowledge before advancing to more specialized AWS certifications. The certification covers a broad range of topics, which can be categorized into the following areas:

I. Cloud Concepts
II. AWS Core Services
III. Security and Compliance
IV. Billing and Pricing
V. Cloud Architecture and Design Principles"""
pdf.chapter_body(introduction)

# Cloud Concepts
pdf.chapter_title('1) Cloud Concepts')
cloud_concepts = """Definition and Advantages of Cloud Computing:

a) Definition:

Cloud computing is the on-demand delivery of IT resources over the internet with pay-as-you-go pricing. Instead of owning and maintaining physical data centers and servers, you can access technology services such as computing power, storage, and databases on an as-needed basis from a cloud provider like AWS.

b) Benefits:

- Cost Efficiency: Reduces or eliminates the need for significant upfront hardware investments.
- Scalability: Easily adjusts resources based on demand.
- Elasticity: Automatically increases or decreases resource capacity to handle variability in workloads.
- Agility: Facilitates rapid development, testing, and deployment of applications.
- Global Reach: Allows deployment of applications in multiple regions worldwide with low latency.
- Reliability: Offers high availability, disaster recovery, and backup options provided by cloud infrastructure.

c) Cloud Deployment Models:

- Public Cloud:
  - Infrastructure and services are owned and operated by a third-party cloud provider (like AWS) and delivered over the internet.
  - Resources are shared among multiple customers, but with strict isolation.
- Private Cloud:
  - Infrastructure is used exclusively by a single organization.
  - Can be hosted on-premises or by a third-party provider.
  - Provides enhanced security and control over resources.
- Hybrid Cloud:
  - Combines public and private cloud resources.
  - Enables data and applications to be shared between them.
  - Offers greater flexibility and optimization of existing infrastructure, security, and compliance."""
pdf.chapter_body(cloud_concepts)

# Save PDF to file
pdf_output_path = "/mnt/data/AWS_Cloud_Practitioner_Rephrased.pdf"
pdf.output(pdf_output_path)

pdf_output_path
