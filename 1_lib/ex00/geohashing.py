import sys
import antigravity


def main():
	if len(sys.argv) != 4:
		print("Usage: python geohashing.py <latitude> <longitude> <date-dow>")
		return 1

	try:
		latitude = float(sys.argv[1])
		longitude = float(sys.argv[2])
	except ValueError:
		print("Error: latitude and longitude must be valid numbers.")
		return 1

	date_dow = sys.argv[3].encode('utf-8')
	try:
		antigravity.geohash(latitude, longitude, date_dow)
	except Exception:
		print("Error: failed to compute geohash with provided arguments.")
		return 1

	return 0

if __name__ == "__main__":
	main()
