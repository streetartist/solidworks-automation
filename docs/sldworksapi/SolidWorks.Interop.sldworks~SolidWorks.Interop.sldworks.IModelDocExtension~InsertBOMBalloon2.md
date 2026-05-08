# InsertBOMBalloon2 Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertBOMBalloon2`

Inserts a BOM balloon for the selected item.
Inserts a BOM balloon for the selected item.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertBOMBalloon2( _
   ByVal BalloonOptions As BalloonOptions _
) As Note
```

```

Dim instance As IModelDocExtension
Dim BalloonOptions As BalloonOptions
Dim value As Note
 
value = instance.InsertBOMBalloon2(BalloonOptions)
```

```

Note InsertBOMBalloon2( 
   BalloonOptions BalloonOptions
)
```

```

Note^ InsertBOMBalloon2( 
   BalloonOptions^ BalloonOptions
) 
```

#### Parameters

*BalloonOptions*
:   [IBalloonOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions.md)

#### Return Value

[Note](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)

Remarks

To create a single BOM balloon:

1. Select an item for which to create a BOM balloon.
2. Call [IModelDocExtension::CreateBalloonOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateBalloonOptions.md) to create an [IBalloonOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions.md) object.
3. Set the properties on the IBalloonOptions object.
4. Call this method using the IBalloonOptions object in the BalloonOptions argument.

Example

[Insert and Show BOM Table and BOM Balloon (VBA)](Insert_and_Show_BOM_Table_and_BOM_Balloon_Example_VB.htm)  
[Insert and Show BOM Table and BOM Balloon (VB.NET)](Insert_and_Show_BOM_Table_and_BOM_Balloon_Example_VBNET.htm)  
[Insert and Show BOM Table and BOM Balloon (C#)](Insert_and_Show_BOM_Table_and_BOM_Balloon_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::InsertStackedBalloon2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertStackedBalloon2.md)  
[IDrawingDoc::AutoBalloon5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AutoBalloon5.md)  
[INote::GetBalloonOptions Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonOptions.md)
