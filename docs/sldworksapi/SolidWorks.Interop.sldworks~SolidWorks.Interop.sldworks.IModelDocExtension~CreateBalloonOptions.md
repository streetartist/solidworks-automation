# CreateBalloonOptions Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateBalloonOptions`

Creates an object that stores BOM balloon options.
Creates an object that stores BOM balloon options.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateBalloonOptions() As BalloonOptions
```

```

Dim instance As IModelDocExtension
Dim value As BalloonOptions
 
value = instance.CreateBalloonOptions()
```

```

BalloonOptions CreateBalloonOptions()
```

```

BalloonOptions^ CreateBalloonOptions(); 
```

#### Return Value

[IBalloonOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions.md)

Remarks

To create a single BOM balloon:

1. Select an item for which to create a BOM balloon.
2. Call this method to create an [IBalloonOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions.md) object.
3. Set the properties on the IBalloonOptions object.
4. Pass the IBalloonOptions object in a call to [IModelDocExtension::InsertBOMBalloon2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertBOMBalloon2.md).

Example

[Insert and Show BOM Table and BOM Balloon (C#)](Insert_and_Show_BOM_Table_and_BOM_Balloon_Example_CSharp.htm)  
[Insert and Show BOM Table and BOM Balloon (VB.NET)](Insert_and_Show_BOM_Table_and_BOM_Balloon_Example_VB.htm)  
[Insert and Show BOM Table and BOM Balloon (VBA)](Insert_and_Show_BOM_Table_and_BOM_Balloon_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::CreateStackedBalloonOptions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateStackedBalloonOptions.md)  
[IDrawingDoc::CreateAutoBalloonOptions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAutoBalloonOptions.md)
