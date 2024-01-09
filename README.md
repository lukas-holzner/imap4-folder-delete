# IMAP Mailbox Manager

![GitHub release (latest by date)](https://img.shields.io/github/v/release/lukas-holzner/imap4-folder-delete)
![Docker Image Version (latest by date)](https://img.shields.io/docker/v/lukas-holzner/imap4-folder-delete)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/lukas-holzner/imap4-folder-delete/Build%20Docker%20Image%20and%20Create%20Release)
![GitHub](https://img.shields.io/github/license/lukas-holzner/imap4-folder-delete)

This is a Streamlit application that allows you to manage your IMAP mailboxes. You can connect to your IMAP server, fetch your mail folders, and delete selected folders.

## Installation

Clone this repository:

```bash
git clone https://github.com/lukas-holzner/imap4-folder-delete.git
```

Navigate to the project directory:

```bash
cd imap4-folder-delete
```

Build the Docker image:

```bash
docker build -t imap-manager .
```

## Usage

Run the Docker container:

```bash
docker run -p 8501:8501 imap-manager
```

Then, open your web browser and go to `http://localhost:8501` to use the application.

## License

[MIT](https://choosealicense.com/licenses/mit/)