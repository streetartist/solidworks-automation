# CreateStackedBalloonOptions Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateStackedBalloonOptions`

Creates an object that stores options for stacked balloons.
Creates an object that stores options for stacked balloons.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateStackedBalloonOptions() As StackedBalloonOptions
```

```

Dim instance As IModelDocExtension
Dim value As StackedBalloonOptions
 
value = instance.CreateStackedBalloonOptions()
```

```

StackedBalloonOptions CreateStackedBalloonOptions()
```

```

StackedBalloonOptions^ CreateStackedBalloonOptions(); 
```

#### Return Value

[IStackedBalloonOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.md)

Remarks

To create a stack of balloons:

1. Select an item to create the first balloon of the stack.
2. Call this method to create an [IStackedBalloonOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.md) object.
3. Set the properties on the IStackedBalloonOptions object.
4. Pass the IStackedBalloonOptions object in a call to [IModelDocExtension::InsertStackedBalloon2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertStackedBalloon2.md).
5. Select one or more items to add one or more balloons to the stack.

Example

[Insert BOM Table and Stacked Balloon (VBA)](Insert_BOM_Table_and_Stacked_Balloon_Example_VB.htm)  
[Insert BOM Table and Stacked Balloon (VB.NET)](Insert_BOM_Table_and_Stacked_Balloon_Example_VBNET.htm)  
[Insert BOM Table and Stacked Balloon (C#)](Insert_BOM_Table_and_Stacked_Balloon_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::CreateBalloonOptions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateBalloonOptions.md)  
[IDrawingDoc::CreateAutoBalloonOptions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAutoBalloonOptions.md)
