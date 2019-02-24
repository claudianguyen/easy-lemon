import React, { Component } from 'react';
import ReactDOM from 'react-dom'
import SearchComponent from './SearchComponent';

$(document).ready(function() {
	let searchComponent = document.getElementById("SearchComponent");
	ReactDOM.render(<SearchComponent name={"React Button?"}/>, searchComponent);
});
