import React from 'react';
import ReactDOM from 'react-dom'
import PropTypes from 'prop-types'

class SearchComponent extends React.Component {

  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    if (this.state.liked) {
      return 'You liked this.';
    }

    return <button onClick={() => {alert("Hola, Cloud!!");}}> {this.props.name}</button>
  }
}
// Props
SearchComponent.propTypes = {
  name: PropTypes.string.isRequired
};

export default SearchComponent;
