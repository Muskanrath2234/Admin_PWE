
{% comment %} 
<main class="main-container">
    <form class="container" action="" method="POST" enctype="multipart/form-data">
        {% csrf_token %}
        <div class="profile-photo-container profile-photo-form-container">
            <p class="profile-page-heading">Edit your profile</p>
            <img src="{{ user.profile.profile_img.url }}" alt="user-image" width="" srcset="">
            {{ form.profile_img }}
        </div>

        <div class="user-content-container user-profile-form-container">
            <ul>
                <li class="name">
                    <label for="id_name">Your Name</label>
                    {{ form.name.errors }}
                    {{ form.name }}
                </li>
                <li class="address">
                    <label for="id_address">Address</label>
                    {{ form.address.errors }}
                    {{ form.address }}
                </li>
                <li class="profession">
                    <label for="id_profession">Profession</label>
                    {{ form.profession.errors }}
                    {{ form.profession }}
                </li>
                <li class="associated-with">
                    <label for="id_assosiat_with">Associated with</label>
                    {{ form.assosiat_with.errors }}
                    {{ form.assosiat_with }}
                </li>
                <li class="college-name">
                    <label for="id_college_name">College Name</label>
                    {{ form.college_name.errors }}
                    {{ form.college_name }}
                </li>
                <li class="coaching-name">
                    <label for="id_coaching_name">Coaching Name</label>
                    {{ form.coaching_name.errors }}
                    {{ form.coaching_name }}
                </li>
                <li class="office-name">
                    <label for="id_office_name">Office Name</label>
                    {{ form.office_name.errors }}
                    {{ form.office_name }}
                </li>
                <li class="other">
                    <label for="id_other">Other</label>
                    {{ form.other.errors }}
                    {{ form.other }}
                </li>
                <li class="photo">
                    <label for="id_photo">Photo</label>
                    {{ form.photo.errors }}
                    {{ form.photo }}
                </li>
                <li class="adhar-card">
                    <label for="id_adhar_card">Adhar Card</label>
                    {{ form.adhar_card.errors }}
                    {{ form.adhar_card }}
                </li>
                <li class="phone-number">
                    <label for="id_phone_number">Phone Number</label>
                    {{ form.phone_number.errors }}
                    {{ form.phone_number }}
                </li>
                <li class="father-contact-number">
                    <label for="id_father_contact_number">Father's Contact Number</label>
                    {{ form.father_contact_number.errors }}
                    {{ form.father_contact_number }}
                </li>
                <li class="date-of-birth">
                    <label for="id_date_of_birth">Date of Birth</label>
                    {{ form.date_of_birth.errors }}
                    {{ form.date_of_birth }}
                </li>
                <li class="date-of-joining">
                    <label for="id_date_of_joing">Date of Joining</label>
                    {{ form.date_of_joing.errors }}
                    {{ form.date_of_joing }}
                </li>
            </ul>
            <button type="submit" class="profile-save-button">Save</button>
        </div>
    </form>
</main>

<script>
    var id_name = document.getElementById('id_name');
    var id_address = document.getElementById('id_address');
    var id_profession = document.getElementById('id_profession');
    id_name.placeholder = 'Your Name';
    id_address.placeholder = 'Address';
    id_profession.placeholder = 'Profession';
</script>
    <!-- Your home page content goes here -->{% endcomment %}