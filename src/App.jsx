import { motion } from 'framer-motion';

export default function App() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-50 p-4">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="max-w-4xl w-full bg-white rounded-2xl shadow-xl overflow-hidden"
      >
        <header className="bg-primary-600 p-6 md:p-8">
          <h1 className="text-3xl md:text-4xl font-bold text-white tracking-tight">
            Modern UI Base
          </h1>
          <p className="text-primary-100 mt-2">
            Responsive layout with Tailwind CSS & Framer Motion
          </p>
        </header>

        <main className="p-6 md:p-8 grid grid-cols-1 md:grid-cols-2 gap-6">
          <div className="p-4 bg-gray-50 rounded-lg border border-gray-100">
            <h3 className="font-semibold text-lg mb-2">Visual Consistency</h3>
            <p className="text-gray-600 text-sm">
              Global palette defined in tailwind.config.js ensures unified branding.
            </p>
          </div>
          <div className="p-4 bg-gray-50 rounded-lg border border-gray-100">
            <h3 className="font-semibold text-lg mb-2">Accessibility</h3>
            <p className="text-gray-600 text-sm">
              High contrast colors and reduced motion support are configured by default.
            </p>
          </div>
        </main>
      </motion.div>
    </div>
  );
}
