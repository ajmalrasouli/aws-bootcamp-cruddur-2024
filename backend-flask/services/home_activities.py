from datetime import datetime, timedelta, timezone
from opentelemetry import trace
from lib.db import pool, query_wrap_object, query_wrap_array

tracer = trace.get_tracer("home.activities")

class HomeActivities:
  def run(cognito_user_id=None):
    print("HOME ACTIVITY")
    #logger.info("HomeActivities")
    with tracer.start_as_current_span("home-activites-mock-data"):
      span = trace.get_current_span()
      now = datetime.now(timezone.utc).astimezone()
      span.set_attribute("app.now", now.isoformat())

      sql = query_wrap_array("""
      SELECT
        activities.uuid,
        activities.user_uuid,
        activities.message,
        activities.replies_count,
        activities.reposts_count,
        activities.likes_count,
        activities.reply_to_activity_uuid,
        activities.expires_at,
        activities.created_at,
      FROM public.activities
      ORDER BY activities.id
      """)
      print("########==========")
      print(sql)
      with pool.connection() as conn:
        conn.execute(sql)
        json = con.fetchone()
        print(json)

      span.set_attribute("app.result_length", len(results))
      return results
