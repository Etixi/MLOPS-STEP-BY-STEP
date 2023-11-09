## **cheat sheet**

### **Building Demos** 

| Fonctions                                                                              |
|----------------------------------------------------------------------------------------|
| [gr.Interface(fn, inputs, outputs, ...)](https://www.gradio.app/docs/interface)        |
| [gr.ChatInterface(fn, ...)](https://www.gradio.app/docs/chatinterface)                 |
| [gr.TabbedInterface(interface_list, ...)](https://www.gradio.app/docs/tabbedinterface) |
| [with gr.Blocks() :](https://www.gradio.app/docs/blocks)                               |

### **Block Layouts**

| Fonctions                                                     |
|---------------------------------------------------------------|
| [with gr.Row():](https://www.gradio.app/docs/row)             |
| [with gr.Column():](https://www.gradio.app/docs/column)       |
| [with gr.Tab():](https://www.gradio.app/docs/tab)             |
| [with gr.Group():](https://www.gradio.app/docs/group)         |
| [with gr.Accordion():](https://www.gradio.app/docs/accordion) |


### **Components**

| Fonctions                                                              |
|------------------------------------------------------------------------|
| [gr.AnnotatedImage(...)](https://www.gradio.app/docs/annotatedimage)   |
| [gr.Audio(...)](https://www.gradio.app/docs/audio)                     |
| [gr.Barplot(...)](https://www.gradio.app/docs/barplot)                 |
| [gr.Button(...)](https://www.gradio.app/docs/button)                   |
| [gr.Chatbot(...)](https://www.gradio.app/docs/chatbot)                 |
| [gr.Checkbox(...)](https://www.gradio.app/docs/themes)                 |
| [gr.CheckboxGroup(...)](https://www.gradio.app/docs/checkboxgroup)     |
| [gr.ClearButton(...)](https://www.gradio.app/docs/clearbutton)         |
| [gr.Code(...)](https://www.gradio.app/docs/code)                       |
| [gr.ColorPicker(...)](https://www.gradio.app/docs/colorpicker)         |
| [gr.Dataframe(...)](https://www.gradio.app/docs/dataframe)             |
| [gr.Dataset(components, samples)](https://www.gradio.app/docs/dataset) |
| [gr.Dropdown(...)](https://www.gradio.app/docs/dropdown)               |
| [gr.DuplicateButton(...)](https://www.gradio.app/docs/duplicatebutton) |
| [gr.File(...)](https://www.gradio.app/docs/file)                       |
| [gr.FileExplorer(...)](https://www.gradio.app/docs/fileexplorer)       |
| [gr.Gallery(..)](https://www.gradio.app/docs/gallery)                  |
| [gr.HTML(..)](https://www.gradio.app/docs/html)                        |
| [gr.HighlightedText(..)](https://www.gradio.app/docs/highlightedtext)  |
| [gr.Image(..)](https://www.gradio.app/docs/image)                      |
| [gr.Interpretation(..)](https://www.gradio.app/docs/interpretation)    |
| [gr.JSON(..)](https://www.gradio.app/docs/json)                        |
| [gr.Lineplot(..)](https://www.gradio.app/docs/lineplot)                |
| [gr.LoginButton(..)](https://www.gradio.app/docs/loginbutton)          |
| [gr.LogoutButton(..)](https://www.gradio.app/docs/logoutbutton)        |
| [gr.Markdown(..)](https://www.gradio.app/docs/markdown)                |
| [gr.Model3D(..)](https://www.gradio.app/docs/model3d)                  |
| [gr.Number(..)](https://www.gradio.app/docs/number)                    |
| [gr.Plot(..)](https://www.gradio.app/docs/plot)                        |
| [gr.Radio(..)](https://www.gradio.app/docs/radio)                      |
| [gr.Scatterplot(..)](https://www.gradio.app/docs/scatterplot)          |
| [gr.Slider(..)](https://www.gradio.app/docs/slider)                    |
| [gr.State(..)](https://www.gradio.app/docs/state)                      |
| [gr.Textbox(..)](https://www.gradio.app/docs/textbox)                  |
| [gr.Timeseries(..)](https://www.gradio.app/docs/timeseries)            |
| [gr.UploadButton(..)](https://www.gradio.app/docs/uploadbutton)        |
| [gr.Video(..)](https://www.gradio.app/docs/video)                      |


### **Modals**

| Fonctions                                              |
|--------------------------------------------------------|
| [gr.Error(...)](https://www.gradio.app/docs/error)     |
| [gr.Warning(...)](https://www.gradio.app/docs/warning) |
| [gr.Info(...)](https://www.gradio.app/docs/info)       |

### **Routers**
#### **1) Request**

| Fonctions                                         |
|---------------------------------------------------|
| [gr.Request](https://www.gradio.app/docs/request) |


#### **2) mount_gradio_app**

| Fonctions                                                           |
|---------------------------------------------------------------------|
| [gr.mount_gradio_app](https://www.gradio.app/docs/mount_gradio_app) |

### **Other**
#### **1) Flagging**

| Fonctions                                                                                       |
|-------------------------------------------------------------------------------------------------|
| [gr.SimpleCSVLogger(...)](https://www.gradio.app/docs/flagging)                                 |
| [gr.CSVLogger(...)](https://www.gradio.app/docs/flagging)                                       |
| [gr.HuggingFaceDatasetSaver(hf_token, dataset_name, ...)](https://www.gradio.app/docs/flagging) |

#### **2) Themes**

| Fonctions                                          |
|----------------------------------------------------|
| [gr.Base(...)](https://www.gradio.app/docs/themes) |
| [gr.Base.push_to_hub(repo_name, ...)](https://www.gradio.app/docs/themes)              |
| [gr.Base.from_hub(repo_name, ...)](https://www.gradio.app/docs/themes)                 |
| [gr.Base.load(path, ...)](https://www.gradio.app/docs/themes)                          |
| [gr.Base.dump(filename, ...)](https://www.gradio.app/docs/themes)                      |
| [gr.Base.from_dict(theme, ...)](https://www.gradio.app/docs/themes)                    |
| [gr.Base.to_dict(...)](https://www.gradio.app/docs/themes)                             |
