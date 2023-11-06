def show_completed_models(completed_models):
  msg = "\n" + f"The following models have been printed: "
  print(msg)
  for completed_model in completed_models:
    print(completed_model.title())
