import AppRoutes from "./routes/AppRoutes";
import Header from "./components/layout/Header";
import Footer from "./components/layout/Footer";

export default function App() {
  return (
    <>
      <Header />
      <AppRoutes />
      <Footer />
    </>
  );
}