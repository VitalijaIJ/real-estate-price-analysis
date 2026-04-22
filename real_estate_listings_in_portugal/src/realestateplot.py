import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


sns.set_theme(style="whitegrid")


def plot_outliers_before_after(df_before, df_after):
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    sns.boxplot(data=df_before, x="Category", y="price_per_m2", ax=axes[0])
    axes[0].set_title("Before Removing Outliers")

    sns.boxplot(data=df_after, x="Category", y="price_per_m2", ax=axes[1])
    axes[1].set_title("After Removing Outliers")
    axes[1].set_ylim(axes[0].get_ylim())

    for ax in axes:
        ax.tick_params(axis="x", rotation=45)

    plt.tight_layout()
    plt.show()


def plot_price_distribution_by_category(df):
    g = sns.displot(
        data=df,
        x="price_per_m2",
        col="Category",
        bins=60,
        facet_kws={"sharex": False, "sharey": False},
    )
    g.fig.suptitle("Price per m² Distribution by Category", y=1.02)
    plt.show()


def plot_property_age_distribution(df):
    plt.figure(figsize=(8, 5))
    sns.histplot(df["PropertyAge"], bins=50)
    plt.title("Distribution of Property Age")
    plt.tight_layout()
    plt.show()


def plot_price_and_log_price_distribution(df):
    df_plot = df.copy()
    df_plot["log_price"] = np.log1p(df_plot["Price"])

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    sns.histplot(df_plot["price_per_m2"], bins=50, ax=axes[0])
    axes[0].set_title("Price per m² Distribution")

    sns.histplot(df_plot["log_price"], bins=50, ax=axes[1])
    axes[1].set_title("Log-transformed Price Distribution")

    plt.tight_layout()
    plt.show()


def plot_property_characteristics_vs_price(df, sample_size=5000):
    df_sample = df.sample(min(sample_size, len(df)), random_state=42)
    df_rooms = df[df["TotalRooms"] <= 10]

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    sns.scatterplot(
        data=df_sample,
        x="LivingArea",
        y="price_per_m2",
        alpha=0.35,
        s=20,
        ax=axes[0, 0],
    )
    axes[0, 0].set_xlim(0, 500)
    axes[0, 0].set_title("Price per m² vs Living Area", fontsize=12)

    sns.regplot(
        data=df_sample,
        x="PropertyAge",
        y="price_per_m2",
        scatter_kws={"alpha": 0.25, "s": 15},
        line_kws={"color": "red"},
        ax=axes[0, 1],
    )
    axes[0, 1].set_title("Price per m² vs Property Age", fontsize=12)

    sns.boxplot(
        data=df_rooms,
        x="TotalRooms",
        y="price_per_m2",
        ax=axes[1, 0],
    )
    axes[1, 0].set_title("Price per m² by Total Rooms", fontsize=12)

    sns.boxplot(
        data=df,
        x="EnergyEfficiencyLevel",
        y="price_per_m2",
        ax=axes[1, 1],
    )
    sns.pointplot(
        data=df,
        x="EnergyEfficiencyLevel",
        y="price_per_m2",
        estimator="median",
        color="red",
        markers="D",
        linestyles="-",
        ax=axes[1, 1],
    )
    axes[1, 1].set_title("Price per m² by Energy Efficiency", fontsize=12)

    for ax in axes.flat:
        ax.tick_params(axis="x", rotation=45)
        sns.despine(ax=ax)

    plt.suptitle(
        "Relationship Between Property Characteristics and Price per m²",
        fontsize=15,
        y=1.02,
    )
    plt.tight_layout()
    plt.show()


def plot_price_by_property_category(df):
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x="Category", y="price_per_m2")
    plt.title("Price per m² by Property Category")
    plt.tight_layout()
    plt.show()


def plot_property_age_by_energy_efficiency(df):
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x="EnergyEfficiencyLevel", y="PropertyAge")
    plt.title("Property Age by Energy Efficiency Rating")
    plt.tight_layout()
    plt.show()


def plot_district_price_and_listing_counts(district_median, district_count):
    fig, axes = plt.subplots(1, 2, figsize=(16, 8))

    district_median.plot(kind="barh", ax=axes[0])
    axes[0].set_title("Median Price per m² by District")
    axes[0].set_xlabel("Price per m²")
    axes[0].set_ylabel("District")
    axes[0].invert_yaxis()

    district_count.plot(kind="barh", ax=axes[1])
    axes[1].set_title("Number of Listings by District")
    axes[1].set_xlabel("Number of Listings")
    axes[1].set_ylabel("")
    axes[1].invert_yaxis()

    plt.tight_layout()
    plt.show()


def plot_district_category_distribution(df, order):
    g = sns.catplot(
        data=df,
        x="District",
        y="price_per_m2",
        col="Category",
        kind="box",
        col_wrap=2,
        height=4,
        aspect=2.5,
        order=order,
    )

    for ax in g.axes.flat:
        ax.tick_params(axis="x", rotation=70)

    g.fig.subplots_adjust(top=0.9)
    g.fig.suptitle(
        "Price per m² Distribution by District and Property Category",
        fontsize=14,
    )
    plt.show()


def plot_top_cities_by_category(df, top_cities):
    plt.figure(figsize=(14, 6))
    sns.boxplot(
        data=df[df["City"].isin(top_cities)],
        x="City",
        y="price_per_m2",
        hue="Category",
    )
    plt.xticks(rotation=45)
    plt.title("Price per m² by Top 7 Cities and Property Category")
    plt.tight_layout()
    plt.show()



def plot_correlation_heatmap(corr, mask):
    plt.figure(figsize=(10, 8))
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        linewidths=0.5,
    )
    plt.title("Correlation Matrix (Lower Triangle)")
    plt.tight_layout()
    plt.show()


def plot_correlation_with_price(corr):
    plt.figure(figsize=(8, 6))
    corr.plot(kind="barh")
    plt.title("Correlation with Price")
    plt.tight_layout()
    plt.show()


def plot_lisbon_porto_distributions(lisbon, porto):
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    sns.histplot(lisbon, bins=40, ax=axes[0])
    axes[0].set_title("Lisboa price distribution")

    sns.histplot(porto, bins=40, ax=axes[1])
    axes[1].set_title("Porto price distribution")

    plt.tight_layout()
    plt.show()


def plot_new_old_distributions(new, old):
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    sns.histplot(new, bins=40, kde=True, ax=axes[0], color="steelblue")
    axes[0].set_title("New properties (≤10 years)")

    sns.histplot(old, bins=40, kde=True, ax=axes[1], color="orange")
    axes[1].set_title("Old properties (>30 years)")

    plt.tight_layout()
    plt.show()


def plot_energy_group_distributions(high, low):
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    sns.histplot(high, bins=40, kde=True, ax=axes[0])
    axes[0].set_title("High efficiency price distribution")

    sns.histplot(low, bins=40, kde=True, ax=axes[1])
    axes[1].set_title("Low efficiency price distribution")

    plt.tight_layout()
    plt.show()


def plot_category_confidence_intervals(df):
    plt.figure(figsize=(8, 5))
    sns.pointplot(
        data=df,
        x="Category",
        y="price_per_m2",
        errorbar=("ci", 95),
        join=False,
        capsize=0.3,
        markers="D",
        color="darkblue",
    )
    plt.ylabel("Price per m²")
    plt.title("Mean price per m² with 95% confidence intervals by property category")
    plt.tight_layout()
    plt.show()


def plot_model_rmse_comparison(all_results):
    plt.figure(figsize=(8, 5))
    sns.barplot(
        data=all_results.sort_values("RMSE"),
        x="RMSE",
        y="Model",
        palette="viridis",
    )
    plt.title("Model Comparison (RMSE)")
    plt.xlabel("RMSE (lower is better)")
    plt.ylabel("Model")
    plt.tight_layout()
    plt.show()


def plot_actual_vs_predicted(y_test, y_test_pred):
    plt.figure(figsize=(6, 6))
    sns.scatterplot(x=y_test, y=y_test_pred, alpha=0.3)
    plt.xlabel("Actual Price")
    plt.ylabel("Predicted Price")
    plt.title("Actual vs Predicted Prices")
    plt.plot(
        [y_test.min(), y_test.max()],
        [y_test.min(), y_test.max()],
        color="red",
    )
    plt.tight_layout()
    plt.show()


def plot_feature_importance(feat_imp, top_n=15):
    plt.figure(figsize=(8, 6))
    top_features = feat_imp.head(top_n)
    plt.barh(
        top_features["Feature"][::-1],
        top_features["Importance"][::-1],
    )
    plt.title(f"Top {top_n} Feature Importances (Random Forest)")
    plt.xlabel("Importance")
    plt.tight_layout()
    plt.show()

def prepare_map_data(df, category, district_coords):

    if category == "All":
        df_map = df.copy()
    else:
        df_map = df[df["Category"] == category].copy()

    district_stats = df_map.groupby("District").agg(
        listings=("Price", "count"),
        median_price_m2=("price_per_m2", "median")
    ).reset_index()

    mainland = district_stats[
        ~district_stats["District"].str.contains("Ilha|Fora de Portugal", na=False)
    ].copy()

    mainland["lat"] = mainland["District"].map(
        lambda x: district_coords.get(x, (None, None))[0]
    )

    mainland["lon"] = mainland["District"].map(
        lambda x: district_coords.get(x, (None, None))[1]
    )

    return mainland


def plot_map(df, category, district_coords):

    mainland = prepare_map_data(df, category, district_coords)

    fig = px.scatter_geo(
        mainland,
        lat="lat",
        lon="lon",
        size="listings",
        color="median_price_m2",
        hover_name="District",
        projection="mercator",
        title=f"Listings and Median Price per m² ({category})",
        width=900,
        height=700
    )

    fig.update_geos(
        showcountries=True,
        showcoastlines=True,
        showland=True,
        lataxis_range=[36.5, 42.5],
        lonaxis_range=[-10.5, -6.0]
    )

    fig.show()

def plot_residuals_vs_predicted(y_pred, residuals):
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x=y_pred, y=residuals, alpha=0.3)
    plt.axhline(0, color="red", linestyle="--")
    plt.xlabel("Predicted Price")
    plt.ylabel("Residuals")
    plt.title("Residuals vs Predicted Values")
    plt.show()


def plot_model_comparison_rmse(ml_results):
    ml_results.sort_values("RMSE").plot(
        x="Model",
        y="RMSE",
        kind="bar",
        figsize=(8, 4),
        title="Model Comparison (RMSE)"
    )
    plt.ylabel("RMSE")
    plt.show()