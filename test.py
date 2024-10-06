import torch

# Load the checkpoint
checkpoint_path = './final_tsp_model_with_state_dict.pth'
checkpoint = torch.load(checkpoint_path, map_location='cpu')
new_checkpoint = {'state_dict': checkpoint}
# Add the missing version key
new_checkpoint['pytorch-lightning_version'] = '2.1.2'  # e.g., '1.5.0'

# Save the modified checkpoint
torch.save(new_checkpoint, './final.pth')
