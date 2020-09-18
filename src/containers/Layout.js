import React, { Fragment } from 'react';
import Header from '../components/layout/Header';
import Footer from '../components/layout/Footer';

const CustomLayout = (props) => {
    return (
        <Fragment>
            <Header />

            <main>
                {props.children}
            </main>
            
            <Footer />
        </Fragment>
    )
}

export default CustomLayout;
