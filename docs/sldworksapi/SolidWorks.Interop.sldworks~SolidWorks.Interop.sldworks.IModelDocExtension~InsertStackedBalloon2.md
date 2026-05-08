# InsertStackedBalloon2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertStackedBalloon2`

Inserts a stack of balloons for selected items.
Inserts a stack of balloons for selected items.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertStackedBalloon2( _
   ByVal BalloonOptions As StackedBalloonOptions _
) As Note
```

```

Dim instance As IModelDocExtension
Dim BalloonOptions As StackedBalloonOptions
Dim value As Note
 
value = instance.InsertStackedBalloon2(BalloonOptions)
```

```

Note InsertStackedBalloon2( 
   StackedBalloonOptions BalloonOptions
)
```

```

Note^ InsertStackedBalloon2( 
   StackedBalloonOptions^ BalloonOptions
) 
```

#### Parameters

*BalloonOptions*
:   [IStackedBalloonOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.md)

#### Return Value

[Note](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)

Remarks

To create a stack of balloons:

1. Select an item to insert the first balloon on the stack.
2. Call [IModelDocExtension::CreateStackedBalloonOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateStackedBalloonOptions.md) to create an [IStackedBalloonOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.md) object.
3. Set the properties on the IStackedBalloonOptions object.
4. Call this method using the IStackedBalloonOptions object in the BalloonOptions argument.
5. Select one or more items to add one or more balloons to the stack.

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
[INote::IsStackedBalloon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsStackedBalloon.md)  
[IBalloonStack Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack.md)  
[IModelDocExtension::InsertBOMBalloon2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertBOMBalloon2.md)  
[IDrawingDoc::AutoBalloon5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AutoBalloon5.md)  
[INote::MakeStackedBalloon Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~MakeStackedBalloon.md)  
[INote::GetBalloonOptions Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonOptions.md)
