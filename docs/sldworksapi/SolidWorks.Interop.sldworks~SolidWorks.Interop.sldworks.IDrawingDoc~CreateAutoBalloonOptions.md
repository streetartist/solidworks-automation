# CreateAutoBalloonOptions Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAutoBalloonOptions`

Creates an object that stores auto balloon options.
Creates an object that stores auto balloon options.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateAutoBalloonOptions() As AutoBalloonOptions
```

```

Dim instance As IDrawingDoc
Dim value As AutoBalloonOptions
 
value = instance.CreateAutoBalloonOptions()
```

```

AutoBalloonOptions CreateAutoBalloonOptions()
```

```

AutoBalloonOptions^ CreateAutoBalloonOptions(); 
```

#### Return Value

[IAutoBalloonOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.md)

Remarks

To automatically create BOM balloons:

1. Select one or more views or sheets for which to automatically create BOM balloons.
2. Call this method to create an [IAutoBalloonOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.md) object.
3. Set the properties on the IAutoBalloonOptions object.
4. Pass the IAutoBalloonOptions object in a call to [IDrawingDoc::AutoBalloon5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AutoBalloon5.md).

Example

[Add Autoballoons to Drawing (C#)](Add_Autoballoon_to_Face_Example_CSharp.htm)  
[Add Autoballoons to Drawing (VB.NET)](Add_Autoballoon_to_Face_Example_VBNET.htm)  
[Add Autoballoons to Drawing (VBA)](Add_Autoballoon_to_Face_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IModelDocExtension::CreateBalloonOptions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateBalloonOptions.md)  
[IModelDocExtension::CreateStackedBalloonOptions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateStackedBalloonOptions.md)
