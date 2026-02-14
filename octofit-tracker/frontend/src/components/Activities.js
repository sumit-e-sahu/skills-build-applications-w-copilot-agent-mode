// Activities.js
import React, { useEffect, useState } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch('https://-8000.app.github.dev/api/activities/')
      .then(res => res.json())
      .then(data => setActivities(data));
  }, []);

  return (
    <div>
      <h2>Activities</h2>
      <ul>
        {activities.map((activity, idx) => (
          <li key={idx}>{activity.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default Activities;
