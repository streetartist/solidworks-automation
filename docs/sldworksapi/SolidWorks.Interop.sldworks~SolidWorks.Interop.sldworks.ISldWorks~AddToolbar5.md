# AddToolbar5 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar5`

Creates a Windows-style dockable toolbar.
Creates a Windows-style dockable toolbar.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddToolbar5( _
   ByVal Cookie As System.Integer, _
   ByVal Title As System.String, _
   ByVal ImageList As System.Object, _
   ByVal MenuPositionForToolbar As System.Integer, _
   ByVal DocumentType As System.Integer _
) As System.Integer
```

```

Dim instance As ISldWorks
Dim Cookie As System.Integer
Dim Title As System.String
Dim ImageList As System.Object
Dim MenuPositionForToolbar As System.Integer
Dim DocumentType As System.Integer
Dim value As System.Integer
 
value = instance.AddToolbar5(Cookie, Title, ImageList, MenuPositionForToolbar, DocumentType)
```

```

System.int AddToolbar5( 
   System.int Cookie,
   System.string Title,
   System.object ImageList,
   System.int MenuPositionForToolbar,
   System.int DocumentType
)
```

```

System.int AddToolbar5( 
   System.int Cookie,
   System.String^ Title,
   System.Object^ ImageList,
   System.int MenuPositionForToolbar,
   System.int DocumentType
) 
```

#### Parameters

*Cookie*
:   Resource ID of the toolbar; this is the same cookie that you specified in [ISwAddin::ConnectToSW](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~ConnectToSW.md)

*Title*
:   Title of the toolbar

*ImageList*
:   Array of strings of the paths for the icons for the toolbar (see **Remarks**)

*MenuPositionForToolbar*
:   Not used (SOLIDWORKS always puts toolbar names in alphabetical order)

*DocumentType*
:   Bitwise values indicating what frame window types should have this toolbar's name added to the View > Toolbars menu; values from [swDocTemplateTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocTemplateTypes_e.html)

#### Return Value

Toolbar ID for use with other methods or -1 if not created

Remarks

For information about using this method with the [ISwAddin](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin.md) object, see [Using ISwAddin to Create a SOLIDWORKS Add-in](sldworksAPIProgGuide.chm::/OVERVIEW/Using_SwAddin_to_Create_a_SOLIDWORKS_Addin.htm).

This method:

- only operates properly when the application is implemented as a **.dll** and not as an **.exe**.
- adds the toolbar name to the View > Toolbars menu.
- only creates the toolbar and passes the images for the icons to SOLIDWORKS. To add functionality, use [ISldWorks::AddToolbarCommand2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbarCommand2.md).
- supports scaling for high resolution screens with high resolution operating system scaling options.

ImageList icons can be:

- 20 x 20 pixels
- 32 x 32 pixels
- 40 x 40 pixels
- 64 x 64 pixels
- 96 x 96 pixels
- 128 x128 pixels

Each image file (**.bmp** or **.png**) should contain all of the same-size icons for the toolbar buttons and separators. For example:

![](ToolbarLarge.bmp)

Each icon strip should use a 256-color palette.

NOTES:  

- When your add-in is unloaded, you must call [ISldWorks::RemoveToolbar2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveToolbar2.md) to remove this toolbar.
- If you want the toolbar to show up in specific locations only, do not use the now obsolete ISldWorks::ShowToolbar2 method. If your application uses that method, your application ignores the DocumentType argument. ISldWorks::ShowToolbar2 assumes that the application is controlling the visibility state of the toolbar, and not the user. This means that the toolbar will be available in all locations.

Example

[Add Toolbars (C#)](Add_Toolbars_Example_CSharp.htm)  
[Add Toolbars (VB.NET)](Add_Toolbars_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::AddMenu Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenu.md)  
[ISldWorks::DragToolbarButton Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DragToolbarButton.md)  
[ISldWorks::DragToolbarButtonFromCommandID Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DragToolbarButtonFromCommandID.md)  
[ISldWorks::GetButtonPosition Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetButtonPosition.md)  
[ISldWorks::GetToolbarDock2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarDock2.md)  
[ISldWorks::GetToolbarState2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarState2.md)  
[ISldWorks::GetToolbarVisibility Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarVisibility.md)  
[ISldWorks::HideToolbar2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~HideToolbar2.md)  
[ISldWorks::RemoveFromMenu Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFromMenu.md)  
[ISldWorks::SetToolbarDock2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetToolbarDock2.md)  
[ISldWorks::SetToolbarVisibility Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetToolbarVisibility.md)  
[ISldWorks::GetImageSize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetImageSize.md)
