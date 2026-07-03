# EulerQ Sample Delivery Dataset — README

This is the historical delivery dataset for the **EulerQ AI/ML Internship
Assessment** (ETA Prediction Platform for Quick Commerce). It's synthetic
data generated to look and behave like a real quick-commerce delivery log
for Bengaluru — distances, peak-hour patterns, and delivery times are all
simulated to be realistic, including the messiness real production data
always has.


## Files in this package

| File | What it is |
|---|---|
| `restaurants.csv` | One row per restaurant |
| `riders.csv` | One row per rider |
| `orders.csv` | One row per order — this is where you'll do most of your work |
| `README.md` | This file — quick column reference |


## Quick start

```python
import pandas as pd

restaurants = pd.read_csv("restaurants.csv")
riders      = pd.read_csv("riders.csv")
orders      = pd.read_csv("orders.csv")

orders = orders.merge(restaurants, left_on="restaurant_id", right_on="id",
                       suffixes=("", "_restaurant"))
orders = orders.merge(riders, left_on="rider_id", right_on="id",
                       suffixes=("", "_rider"), how="left")
```
Use `how="left"` on the rider merge — some orders (mostly cancelled ones)
have no rider assigned.

---

## `restaurants.csv`

| Column | What it means |
|---|---|
| `id` | Restaurant identifier |
| `name` | Restaurant name |
| `lat` / `lon` | Restaurant's location |
| `cuisine` | Cuisine category (North Indian, Chinese, Bakery, etc.) |
| `avg_rating` | Historical average customer rating, out of 5 |
| `prep_capacity` | How many orders the kitchen can prepare in parallel per hour — a proxy for how busy/slow the kitchen gets under load |
| `manager_contact` | A phone-number-style string. **Not useful for prediction** — included as a distractor column. |

## `riders.csv`

| Column | What it means |
|---|---|
| `id` | Rider identifier |
| `lat` / `lon` | Rider's last known location |
| `vehicle_type` | What they're delivering on — bike, scooter, bicycle, or car. Formatting is inconsistent on purpose (`Bike`, `BIKE`, `two_wheeler`, etc.) |
| `completed_orders` | Lifetime completed deliveries — a rough proxy for experience |
| `shift_hours` | How many hours into their current shift they are |
| `current_load` | How many orders they're juggling right now |
| `rider_call_sign` | A random call-sign string. **Not useful for prediction** — distractor column. |

## `orders.csv`

| Column | What it means |
|---|---|
| `id` | Order identifier |
| `restaurant_id` | Which restaurant the order came from (join to `restaurants.id`) |
| `rider_id` | Which rider delivered it (join to `riders.id`). Empty for orders where no rider was ever assigned. |
| `drop_lat` / `drop_lon` | Customer's delivery location |
| `order_size` | Number of items in the order |
| `order_value` | Order value in ₹ |
| `timestamp` | When the order was placed. **Format is inconsistent** across rows — you'll need to parse it before doing anything time-based. |
| `promised_eta` | The ETA (in minutes) the platform showed the customer at checkout — this is a *prediction the platform already made*, not the outcome. Useful as a baseline/feature. |
| `actual_delivery_time_min` | **This is the target column.** How long the delivery actually took, in minutes. This is what your model should predict. |
| `order_status` | `delivered` or `cancelled` |
| `promo_code_used` | Promo code applied, if any. **Not useful for prediction** — distractor column. |

### The one column relationship that matters most

> `promised_eta` is the platform's *guess*. `actual_delivery_time_min` is
> *what really happened*. Don't confuse the two — `promised_eta` is a
> legitimate **input feature** (or a baseline to compare your model
> against), while `actual_delivery_time_min` is the **label you're
> training the model to predict**. Never use `actual_delivery_time_min`
> (or anything derived from it) as a feature — that would be leaking the
> answer into the input.

## A few things you'll notice while exploring

This data isn't clean on purpose — that's part of the exercise. You'll run
into missing values, a few duplicate rows, some inconsistent text
formatting, and a handful of outliers. None of it is a bug in the dataset.
