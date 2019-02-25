import React from 'react';
import ReactDOM from 'react-dom'
import PropTypes from 'prop-types'

class SearchComponent extends React.Component {

  constructor(props) {
    super(props);    
  }

  render() {
    return (
      <div>
        <h1>Welcome to easy lemon!</h1>
        <div>
          <label htmlFor="job-title" >
            <span className="label">Job Title</span>
            <br/>
            <input type="text" className="texbox" id="job-title" value="software engineer" />
          </label>
          <br/>
          <label htmlFor="job-location" >
            <span className="label">Location</span>
            <br/>
            <input type="text" className="texbox" id="job-location" value="San Mateo" />
          </label>
          <br/>
          <label htmlFor="job-salary" >
            <span className="label">Desired Salary</span>
            <br/>
            <input type="text" className="texbox" id="job-salary" value="100000" />
          </label>
          <br/>
          <input type="button" className="submit-button" value="Submit" onClick={this.props.handleJobSubmission} />
        </div>
      </div>      
    );
  }
}
// Props
SearchComponent.propTypes = {
  handleJobSubmission: PropTypes.func.isRequired
};

export default SearchComponent;
