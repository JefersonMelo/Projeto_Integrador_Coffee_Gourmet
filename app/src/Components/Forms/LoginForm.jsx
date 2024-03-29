import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import { Chip, TextField } from "@mui/material";
import { FormHelperText } from "@mui/material";
import { useAppContext } from "../../Contexts/AppContext";
import { useAuthContext } from "../../Contexts/AuthenticationContext";
import api from "../../Services/api";
import { apiRouts } from "../../Helpers/Globals";
import { EmailValidator } from "../../Helpers/Validators/EmailValidator";
import { ShowSuccessSnackBar } from "../../Helpers/SnackBars";
import { Theme } from "../../Helpers/Theme";

export default function LoginForm() {
  const [, setAppContext] = useAppContext();
  const [, setAuthContext] = useAuthContext();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [checkedUser, setCheckedUser] = useState(true);
  const navigate = useNavigate();
  const colors = Theme.palette;

  const onSubmit = () => {
    const data = {
      UserEmail: email,
      Password: password,
    };

    api.post(apiRouts.GET_LOGIN, data)
      .then((res) => {
        ShowSuccessSnackBar(res, setAppContext);
        setAuthContext((prev) => ({
          ...prev,
          userid: res.data.userid,
          username: res.data.username,
          token: res.data.token,
        }));
        navigate("/home");
      })
      .catch((err) => {
        setCheckedUser(false);
      });
  };

  return (
    <>
      <Box display="flex" flexDirection="column" alignItems="center">
        <strong>
          <Chip label="Login cbgourmet" />
        </strong>
        <TextField
          error={!checkedUser}
          
          variant="outlined"
          size="small"
          margin="normal"
          fullWidth
          required={true}
          id="email"
          label="E-mail"
          name="email"
          autoComplete="email"
          autoFocus
          onChange={(e) => {
            setEmail(e.target.value);
          }}
        />
        <TextField
          error={!checkedUser}
          onKeyPress={(e) => {
            if (e.key === "Enter") {
              onSubmit();
            }
          }}
          variant="outlined"
          
          size="small"
          margin="normal"
          fullWidth
          required={true}
          name="password"
          label="Senha"
          type="password"
          id="password"
          autoComplete="current-password"
          onChange={(e) => {
            setPassword(e.target.value);
          }}
        />
        {!checkedUser && (
          <>
            <Box
              sx={{
                justifyContent: "flex-end",
                display: "flex",
                alignItems: "flex-end",
              }}
            >
              <FormHelperText error={!checkedUser} sx={{ mt: "0.5rem" }}>
                Verifique Email e Senha 😞
              </FormHelperText>
            </Box>
          </>
        )}
        <Button
          sx={{ mt: "0.8rem" }}
          disabled={!EmailValidator(email)}
          variant="contained"
          color="primary"
          type="submit"
          fullWidth
          onClick={() => {
            onSubmit();
          }}
        >
          Entrar
        </Button>
      </Box>
      {!checkedUser && (
        <>
          <Box
            sx={{
              justifyContent: "flex-end",
              display: "flex",
              alignItems: "flex-end",
            }}
          >
            <FormHelperText sx={{ mt: "0.5rem" }}>
              Não tem cadastro?
            </FormHelperText>
          </Box>
        </>
      )}
      <Box
        sx={{
          mt: "0.5rem",
          justifyContent: "flex-end",
          display: "flex",
          alignItems: "flex-end",
        }}
      >
        <Button
          sx={{
            "&:hover, &.Mui-focusVisible": {
              backgroundColor: colors.dropzone.lighGrey,
            },
          }}
          color="primary"
          onClick={() => {
            navigate("/new/user");
          }}
        >
          Cadastre-se
        </Button>
      </Box>
    </>
  );
}
