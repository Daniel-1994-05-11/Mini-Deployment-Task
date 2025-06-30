
----- Answers to Add-On Questions -----

1. Form Validation:
   The app checks that all fields are filled and the date of birth is in the past. If a required field is missing or the date is invalid/future, an error is shown on the form.

2. Therapist Login Structure:
   Use Flask-Login and a `users` table. Protect routes using `@login_required`. Store session securely, hash passwords with bcrypt.

3. HIPAA-Compliant Deployment:
   Deploy on a HIPAA-compliant cloud (like AWS with BAA), use HTTPS, encrypted RDS for DB, IAM for access control, logging (CloudTrail), and environment isolation (e.g., ECS or Lambda).

4. Database Initialization:
   The database setup code is in `init_db()` within `app.py`, run at startup. This ensures the DB is ready before handling requests and avoids missing tables.
