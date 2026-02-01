'use client';

import { useState, useEffect, useCallback } from 'react';
import { Input } from '@/components/ui/input';
import { useDebounce } from '@/lib/hooks';

interface SearchBarProps {
  onSearch: (query: string) => void;
  initialValue?: string;
}

export function SearchBar({ onSearch, initialValue = '' }: SearchBarProps) {
  const [value, setValue] = useState(initialValue);
  const debouncedValue = useDebounce(value, 300);

  useEffect(() => {
    onSearch(debouncedValue);
  }, [debouncedValue, onSearch]);

  return (
    <div className="relative">
      <Input
        type="text"
        placeholder="Search ingredients..."
        value={value}
        onChange={(e) => setValue(e.target.value)}
        className="w-full"
      />
    </div>
  );
}
