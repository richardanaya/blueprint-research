'use client';

import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select';
import { getAllCategories, getAllProducts } from '@/lib/data';

interface CategoryFilterProps {
  value: string;
  onChange: (value: string) => void;
}

export function CategoryFilter({ value, onChange }: CategoryFilterProps) {
  const categories = getAllCategories();

  return (
    <Select value={value} onValueChange={onChange}>
      <SelectTrigger className="w-[180px]">
        <SelectValue placeholder="All Categories" />
      </SelectTrigger>
      <SelectContent>
        <SelectItem value="">All Categories</SelectItem>
        {categories.map((category) => (
          <SelectItem key={category} value={category}>
            {category}
          </SelectItem>
        ))}
      </SelectContent>
    </Select>
  );
}

interface ProductFilterProps {
  value: string;
  onChange: (value: string) => void;
}

export function ProductFilter({ value, onChange }: ProductFilterProps) {
  const products = getAllProducts();

  return (
    <Select value={value} onValueChange={onChange}>
      <SelectTrigger className="w-[180px]">
        <SelectValue placeholder="All Products" />
      </SelectTrigger>
      <SelectContent>
        <SelectItem value="">All Products</SelectItem>
        {products.map((product) => (
          <SelectItem key={product} value={product}>
            {product}
          </SelectItem>
        ))}
      </SelectContent>
    </Select>
  );
}
