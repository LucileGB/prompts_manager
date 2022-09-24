function toggleEdit(promptId) {
    let editButton = document.getElementById(`edit_${promptId}`);
  
    if (editButton.classList.contains("editFormHidden")) {
      editButton.classList.toggle("editFormShown");
    } else {
      editButton.classList.toggle("editFormHidden");
      }
  }
  