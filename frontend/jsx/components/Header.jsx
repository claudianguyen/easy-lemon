import React from 'react';
import ReactDOM from 'react-dom'
import PropTypes from 'prop-types'


class Header extends React.Component {

  constructor(props) {
    super(props);
  }


  render() {
    return (
      <div className="top-header-div">
        <h2> Welcome to EasyLemon! </h2>
      </div>
    );
  }
}

// Props
Header.propTypes = {
};



export default Header;