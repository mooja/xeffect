var HabitCardBox = React.createClass({displayName: "HabitCardBox",

    render: function() {
        return (
            React.createElement("div", {className: "habitBox"}, 
              React.createElement("h1", null, " ", this.state.data.title, " "), 
              React.createElement("br", null), 
              React.createElement("br", null), 
               React.createElement(HabitDaysListing, {days: this.state.data.status, onDaysUpdate: this.handleUpdatedDays})
           )
        );
    },

    getInitialState: function () {
        return {data: []};
    },

    loadHabitsFromServer: function() {
      $.ajax({
        url: this.props.url,
        dataType: 'json',
        cache: false,
        success: function(data) {
          this.setState({data: data});
        }.bind(this),
        error: function(xhr, status, err) {
          console.error(this.props.url, status, err.toString());
        }.bind(this)
      });
    },

    componentDidMount: function() {
      this.loadHabitsFromServer();
      setInterval(this.loadHabitsFromServer, this.props.pollInterval);
    },

    handleUpdatedDays: function(o) {
      this.state.data.status = o.days;

      $.ajax({
        url: this.props.url,
        dataType: 'json',
        type: 'PUT',
        data: this.state.data,
        success: function(data) {
          this.setState({data: data});
        }.bind(this),
        error: function(xhr, status, err) {
          console.error(this.props.url, status, err.toString());
        }.bind(this)
      });
    }
});



var HabitDaysListing = React.createClass({displayName: "HabitDaysListing",
  render: function() {
    if (this.props.days == null)  {
        return (
          React.createElement("div", {className: "noneLoaded"}, 
            React.createElement("h1", null, " nothing loaded! ")
          )
        );
    }

    var dayNodes = [];

    for (var i = 0; i < this.props.days.length; i++) {
      if (this.props.days[i] == '0') {
        var dayNode = (
          React.createElement("div", {className: "day dayOff", id: i, onClick: this.handleDayClick}, 
            i+1
          )
        );
      }
      else {
        var dayNode = (
          React.createElement("div", {className: "day dayOn", id: i, onClick: this.handleDayClick}, 
            i+1
          )
        );
      }

      dayNodes.push(dayNode);
    }

    return (
      React.createElement("div", {className: "habitDays"}, 
        dayNodes
      )
    );
  },

  handleDayClick: function(e) {
    var day_id = Number(e.target.attributes.id.value);
    var new_days = this.props.days.split('');

    if (new_days[day_id] == '0')
      new_days[day_id] = '1';
    else if (new_days[day_id] == '1') 
      new_days[day_id] = '0';

    new_days = new_days.join('');
    this.props.onDaysUpdate({days: new_days});
  },
});

