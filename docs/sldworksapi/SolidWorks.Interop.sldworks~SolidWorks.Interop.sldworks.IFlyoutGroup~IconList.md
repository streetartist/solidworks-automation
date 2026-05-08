# IconList Property (IFlyoutGroup)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~IconList`

Gets or sets the paths for the icons for the toolbar buttons for this flyout.
Gets or sets the paths for the icons for the toolbar buttons for this flyout.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IconList As System.Object
```

```

Dim instance As IFlyoutGroup
Dim value As System.Object
 
instance.IconList = value
 
value = instance.IconList
```

```

System.object IconList {get; set;}
```

```

property System.Object^ IconList {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of strings of the paths for the icons for the toolbar buttons for this flyout (see **Remarks**)

Remarks

This property supports scaling for high resolution screens with high resolution operating system scaling options.

The array of strings for the paths to the image files can contain icons of the following sizes:

- 20 x 20 pixels
- 32 x 32 pixels
- 40 x 40 pixels
- 64 x 64 pixels
- 96 x 96 pixels
- 128 x128 pixels

Each image file (**.bmp** or **.png**) should contain all of the same-size icons for all of the buttons. For example:

![](ToolbarLarge.bmp)

Each icon strip should use a 256-color palette.

The order in which you specify the icons must be the same for this property and [IFlyoutGroup::MainIconList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~MainIconList.md). For example, if you specify an array of paths to 20 x 20 pixels, 32 x 32 pixels, and 40 x 40 pixels icons for this property, then you must specify an array of paths to 20 x 20 pixels, 32 x 32 pixels, and 40 x 40 pixels icons for IFlyoutGroup::MainIconList.

Example

[Create Flyouts in the CommandManager (C#)](Create_Flyouts_in_the_CommandManager_Example_CSharp.htm)  
[Create Flyouts in the CommandManager (VB.NET)](Create_Flyouts_in_the_CommandManager_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFlyoutGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup.md)  
[IFlyoutGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup_members.md)  
[ISldWorks::GetImageSize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetImageSize.md)
