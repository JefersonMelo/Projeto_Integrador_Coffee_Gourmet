import React, { useState } from "react";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import { Button, TextField } from "@mui/material";
import { useAppContext } from "../../Contexts/AppContext";
import { useAuthContext } from "../../Contexts/AuthenticationContext";
import api from "../../Services/api";
import { apiRouts } from "../../Helpers/Globals";
import {
  ShowErrorSnackBar,
  ShowSuccessSnackBar,
} from "../../Helpers/SnackBars";
import { useUserContext } from "../../Contexts/UserContext";

export default function NewIdentificationForm() {
  const [, setAppContext] = useAppContext();
  const [authContext] = useAuthContext();
  const [, setUserContext] = useUserContext();
  const [docNumber, setDocNumber] = useState("");
  const [lastName, setLastName] = useState("");
  const [name, setName] = useState("");

  const onSubmit = () => {
    let data = {
      FK_UserID: authContext.userid,
      DocNumber: docNumber,
      LastName: lastName,
      Name: name,
    };

    if (!docNumber || !lastName || !name) return;

    api.post(
        apiRouts.ADD_IDENTIFICATION_BY_USER_ID.replace(
          "%user_id%",
          authContext.userid
        ),
        data
      )
      .then((res) => {
        setUserContext((prev) => ({
          ...prev,
          identification: res.data.results,
        }));
        ShowSuccessSnackBar(res, setAppContext);
      })
      .catch((err) => {
        ShowErrorSnackBar(err, setAppContext);
      });
  };

  return (
    <>
      <Box display="flex" flexDirection="column" alignItems="flex-start">
        <Typography variant="h6">Adicionar Identidade</Typography>

        <TextField
          disabled
          variant="outlined"
          
          size="small"
          margin="normal"
          fullWidth
          id="usernameID"
          label="User Name"
          name="username"
          defaultValue={authContext.username}
        />

        <TextField
          variant="outlined"
          
          size="small"
          margin="normal"
          fullWidth
          required={true}
          id="nomeID"
          label="Nome"
          name="name"
          autoFocus
          onChange={(e) => {
            setName(e.target.value);
          }}
        />

        <TextField
          variant="outlined"
          
          size="small"
          margin="normal"
          fullWidth
          required={true}
          id="sobrenomeID"
          label="Sobrenome"
          name="lastname"
          onChange={(e) => {
            setLastName(e.target.value);
          }}
        />

        <TextField
          type="number"
          
          variant="outlined"
          size="small"
          margin="normal"
          fullWidth
          required={true}
          id="docNumberID"
          label="Número do Documento"
          name="number"
          onChange={(e) => {
            setDocNumber(e.target.value);
          }}
        />
      </Box>

      <Box display="flex" flexDirection="column" alignItems="flex-end">
        <Button
          sx={{ mt: "0.8rem", mb: "1rem" }}
          variant="contained"
          color="primary"
          type="submit"
          onClick={() => {
            onSubmit();
          }}
        >
          Salvar
        </Button>
      </Box>
    </>
  );
}
