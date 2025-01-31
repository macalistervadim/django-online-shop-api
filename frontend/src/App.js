import { BrowserRouter, Route, Routes, Navigate } from "react-router-dom";
import Home from "./Home";
import OnlineShop from "./online-shop/OnlineShop";
import Products from "./online-shop/products/products";
import CartComp from "./online-shop/cart/CartComp";
import DetailMain from "./online-shop/detail/detailmain";
import Orders from "./online-shop/orders/orders";
import Contacts from "./pages/Contacts";

function App() {

  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/online-shop' element={<OnlineShop />} />
          <Route path='/online-shop/category/:id' element={<Products />} />
          <Route path='/online-shop/product/:id' element={<DetailMain />} />
          <Route path='/online-shop/orders' element={<Orders />} />
          <Route path='/online-shop/cart' element={<CartComp />} />
          <Route path='/contacts' element={<Contacts />} />
          <Route path='*' element={<Navigate to='/' />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;