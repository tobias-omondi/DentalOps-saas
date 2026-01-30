
import React, { useState } from 'react';

const LogInForm = ({ onLogin }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [remember, setRemember] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    setError(null);
    try {
      const res = await fetch('http://127.0.0.1:8000/api/clinic-admins/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password }),
      });

      const payload = await res.json().catch(() => ({}));

      if (!res.ok) {
        const msg = payload?.message || payload?.error || res.statusText || 'Login failed';
        throw new Error(msg);
      }

      // Expecting { token, user }
      if (payload.token) {
        try {
          if (remember) localStorage.setItem('authToken', payload.token);
          else sessionStorage.setItem('authToken', payload.token);
        } catch (_) {}
      }

      if (onLogin) onLogin(payload.user ?? email);
    } catch (err) {
      setError(err.message || 'Login failed');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen w-full flex items-center justify-center bg-slate-50">
      <div className="max-w-2xl w-full bg-white rounded-3xl overflow-hidden shadow-2xl border border-slate-100 p-8">
        <div className="max-w-md mx-auto w-full">
          <div className="mb-6 text-center">
            <h3 className="text-3xl font-bold text-slate-800 mb-2">Welcome Back</h3>
            <p className="text-slate-500">Access your clinic's dashboard.</p>
          </div>

          <form onSubmit={handleSubmit} className="space-y-6">
          <div>
            <label className="block text-sm font-semibold text-slate-700 mb-2">Clinic Email Address</label>
            <input
              type="email"
              required
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="clinic@example.com"
              className="w-full px-4 py-3 rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-sky-500/20 focus:border-sky-500 transition-all bg-slate-50/50"
            />
          </div>

          <div>
            <div className="flex justify-between items-center mb-2">
              <label className="block text-sm font-semibold text-slate-700">Password</label>
              <a href="#" className="text-xs text-sky-600 font-semibold hover:text-sky-700">Forgot Password?</a>
            </div>
            <input
              type="password"
              required
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="••••••••"
              className="w-full px-4 py-3 rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-sky-500/20 focus:border-sky-500 transition-all bg-slate-50/50"
            />
          </div>

          <div className="flex items-center gap-3">
            <input
              type="checkbox"
              id="remember"
              checked={remember}
              onChange={(e) => setRemember(e.target.checked)}
              className="w-4 h-4 rounded border-slate-300 text-sky-600 focus:ring-sky-500"
            />
            <label htmlFor="remember" className="text-sm text-slate-600 cursor-pointer">Remember this device</label>
          </div>

          {error && <div className="text-sm text-red-600">{error}</div>}

          <button
            type="submit"
            disabled={isLoading}
            className={`w-full py-4 rounded-xl font-bold text-white shadow-lg transition-all flex items-center justify-center gap-2
              ${isLoading ? 'bg-sky-400' : 'bg-sky-600 hover:bg-sky-700 hover:shadow-sky-200 shadow-sky-100 active:scale-[0.98]'}`}
          >
            {isLoading ? (
              <>
                <svg className="animate-spin h-5 w-5 text-white" fill="none" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                Securing Connection...
              </>
            ) : 'Log In to Dashboard'}
          </button>
          </form>

          <div className="mt-6 text-center">
            <p className="text-sm text-slate-500">
              New to DentaCloud? <a href="#" className="text-sky-600 font-bold hover:underline">Register your clinic</a>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default LogInForm;
