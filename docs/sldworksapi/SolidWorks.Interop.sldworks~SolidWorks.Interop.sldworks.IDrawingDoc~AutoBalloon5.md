# AutoBalloon5 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AutoBalloon5`

Automatically inserts BOM balloons in selected drawing views.
Automatically inserts BOM balloons in selected drawing views.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AutoBalloon5( _
   ByVal BalloonOptions As AutoBalloonOptions _
) As System.Object
```

```

Dim instance As IDrawingDoc
Dim BalloonOptions As AutoBalloonOptions
Dim value As System.Object
 
value = instance.AutoBalloon5(BalloonOptions)
```

```

System.object AutoBalloon5( 
   AutoBalloonOptions BalloonOptions
)
```

```

System.Object^ AutoBalloon5( 
   AutoBalloonOptions^ BalloonOptions
) 
```

#### Parameters

*BalloonOptions*
:   [IAutoBalloonOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.md)

#### Return Value

Array of [INotes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)

Remarks

This method automatically inserts BOM balloons for bill of materials items in selected drawing views. If a drawing sheet is selected, BOM balloons are automatically inserted for all of the drawing views on that drawing sheet.

To automatically insert BOM balloons:

1. Select one or more views or sheets for which to automatically create BOM balloons.
2. Call [IDrawingDoc::CreateAutoBalloonOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAutoBalloonOptions.md) to create an [IAutoBalloonOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.md) object.
3. Set the properties on the IAutoBalloonOptions object.
4. Call this method using the IAutoBalloonOptions object in the BalloonOptions argument.

Example

[Add Autoballoons to Drawing (VBA)](Add_Autoballoon_to_Face_Example_VB.htm)  
[Add Autoballoons to Drawing (VB.NET)](Add_Autoballoon_to_Face_Example_VBNET.htm)  
[Add Autoballoons to Drawing (C#)](Add_Autoballoon_to_Face_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IModelDocExtension::InsertBOMBalloon2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertBOMBalloon2.md)  
[IModelDocExtension::InsertStackedBalloon2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertStackedBalloon2.md)
