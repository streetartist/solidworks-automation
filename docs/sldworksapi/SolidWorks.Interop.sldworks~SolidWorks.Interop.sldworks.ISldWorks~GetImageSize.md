# GetImageSize Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetImageSize`

Gets:
Gets:

- small, medium, and large image sizes suitable for the current DPI setting of the display device.
- default image size for the current DPI setting of the display device for images that are not based on the SOLIDWORKS icon size setting.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetImageSize( _
   ByRef Small As System.Integer, _
   ByRef Medium As System.Integer, _
   ByRef Large As System.Integer _
) As System.Integer
```

```

Dim instance As ISldWorks
Dim Small As System.Integer
Dim Medium As System.Integer
Dim Large As System.Integer
Dim value As System.Integer
 
value = instance.GetImageSize(Small, Medium, Large)
```

```

System.int GetImageSize( 
   out System.int Small,
   out System.int Medium,
   out System.int Large
)
```

```

System.int GetImageSize( 
   [Out] System.int Small,
   [Out] System.int Medium,
   [Out] System.int Large
) 
```

#### Parameters

*Small*
:   Small image size suitable for the current DPI setting of the display device

*Medium*
:   Medium image size suitable for the current DPI setting of the display device

*Large*
:   Large image size suitable for the current DPI setting of the display device

#### Return Value

Default image size for the current DPI setting of the display device for images that are not based on the SOLIDWORKS icon size setting as defined in [swImageSizeToUse\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swImageSizeToUse_e.html)

Remarks

You can use this method to determine the correct size for:

- buttons for your PropertyManager pages.
- icons for your macro features.

Example

[Create Flyouts in the CommandManager (C#)](Create_Flyouts_in_the_CommandManager_Example_CSharp.htm)  
[Create Flyouts in the CommandManager (VB.NET)](Create_Flyouts_in_the_CommandManager_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ICommandGroup::IconList Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~IconList.md)  
[ICommandGroup::MainIconList Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~MainIconList.md)  
[ICommandManager::CreateFlyoutGroup2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~CreateFlyoutGroup2.md)  
[IFlyoutGroup::IconList Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~IconList.md)  
[IFlyoutGroup::MainIconList Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~MainIconList.md)  
[IFrame::AddMenuPopupIcon3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuPopupIcon3.md)  
[IPropertyManagerPageBitmapButton::SetBitmapsByName3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton~SetBitmapsByName3.md)  
[ISldWorks::AddMenuItem5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuItem5.md)  
[ISldWorks::AddToolbar5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar5.md)  
[ITaskPaneView::AddCustomButton2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~AddCustomButton2.md)  
[ISldWorks::CreateTaskpaneView3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CreateTaskpaneView3.md)
