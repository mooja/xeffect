var habit_display_elm = document.querySelector("#habitdisplay");

React.render(
    <HabitCardBox url={habit_json_url} pollInterval={3000} />,
    habit_display_elm
);
