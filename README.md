# AI Attendance System - Module 1

This module provides User and Role Management for an AI-based Attendance System using Flask and MySQL.

## Project Structure

```text
attendio/
├── app.py
├── config.py
├── database_config.py
├── schema.sql
├── requirements.txt
├── routes/
├── models/
├── services/
└── utils/
```

## Setup

1. Create the MySQL database and table:

```sql
SOURCE schema.sql;
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Copy environment variables:

```bash
copy .env.example .env
```

4. Run the Flask app:

```bash
python app.py
```

## APIs

### Register

- `POST /api/v1/auth/register`

```json
{
  "name": "Admin User",
  "email": "admin@example.com",
  "password": "StrongPassword123",
  "role": "Admin"
}
```

### Login

- `POST /api/v1/auth/login`

```json
{
  "email": "admin@example.com",
  "password": "StrongPassword123"
}
```

### Protected Admin Route

- `GET /api/v1/admin`
- Header: `Authorization: Bearer <jwt_token>`

### Database Health Check

- `GET /api/v1/db-health`
- Verifies that Flask can reach MySQL and query the selected database

### Student APIs

- `POST /api/v1/students`
- `GET /api/v1/students`
- `PUT /api/v1/students/<student_id>`
- `DELETE /api/v1/students/<student_id>`
- All student APIs require `Authorization: Bearer <jwt_token>` for an `Admin` user

Student create/update payload:

```json
{
  "name": "Aarav Sharma",
  "roll_no": "STU-001",
  "class": "10-A"
}
```

### Face Registration API

- `POST /api/v1/students/<student_id>/faces`
- Multipart form-data with one or more `images` files
- Requires `Authorization: Bearer <jwt_token>` for an `Admin` user
- Each image must contain exactly one detectable face

### Attendance Recognition API

- `POST /api/v1/attendance/frame`
- JSON body:

```json
{
  "frame": "data:image/jpeg;base64,...",
  "refresh_embeddings": false
}
```

- Detects one or more faces in the incoming frame
- Detects faces with OpenCV
- Generates embeddings with `face_recognition`
- Compares them against stored MySQL embeddings in memory
- Returns recognized student IDs, student details, confidence, and face locations
- Requires a Teacher JWT and an active attendance session

### Attendance Session APIs

- `POST /api/v1/attendance/sessions`
  Payload:
```json
{
  "class": "10-A",
  "subject": "Mathematics"
}
```
- `POST /api/v1/attendance/sessions/<session_id>/end`
- `GET /api/v1/attendance/sessions/<session_id>/review`
- `PUT /api/v1/attendance/sessions/<session_id>/students/<student_id>`
  Payload:
```json
{
  "status": "Present"
}
```

- All attendance session APIs require a `Teacher` JWT
- Recognized students are auto-marked as `Present` or `Late` based on the configured late threshold
- Students not detected by session end are automatically marked `Absent`
- Duplicate attendance entries are prevented per student per session

### Attendance Reports and Dashboard

- `GET /api/v1/reports/students/<student_id>?period=daily|weekly|monthly`
- `GET /api/v1/reports/dashboard?class=10-A`
- `GET /dashboard`

- Students can view only their own linked student data
- Teachers can view class-level summaries
- Admins can view all student summaries
- Dashboard responses include low-attendance alerts using the configured threshold
