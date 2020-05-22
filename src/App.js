import React from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import CustomLayout from './containers/Layout';
import BaseRouter from './routes';

import './scss/app.scss';

function App() {
  return (
    <Router>
      <CustomLayout>
        <BaseRouter />
      </CustomLayout>
    </Router>
  );
}

export default App;
