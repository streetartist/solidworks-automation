# SetAsTableAnchor Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetAsTableAnchor`

Sets the anchor for the specified table at a selected point in the sheet format.
Sets the anchor for the specified table at a selected point in the sheet format.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetAsTableAnchor( _
   ByVal TableType As System.Integer _
) As System.Object
```

```

Dim instance As ISheet
Dim TableType As System.Integer
Dim value As System.Object
 
value = instance.SetAsTableAnchor(TableType)
```

```

System.object SetAsTableAnchor( 
   System.int TableType
)
```

```

System.Object^ SetAsTableAnchor( 
   System.int TableType
) 
```

#### Parameters

*TableType*
:   Table for which an anchor is required as defined in [swTableAnnotationType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTableAnnotationType_e.html)

#### Return Value

[ITableAnchor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnchor.md)

Remarks

Before calling this method, you must call:

1. [IDrawingDoc::EditTemplate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditTemplate.md) to edit the sheet format.
2. [IModelDoc2::EditSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditSketch.md) to create a sketch.
3. [ISketchManager::CreatePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreatePoint.md) to create a sketch point where to position the table anchor.

If an anchor already exists for the table, then this method moves the anchor of that table to the selected position.

After calling this method you must call:

1. [IDrawingDoc::EditSheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditSheet.md)
2. IModelDoc2::EditSketch
3. [IModelDoc2::ForceRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3.md)

Example

[Set Table Anchors in Sheet Formats (VBA)](Set_Table_Anchors_Example_VB.htm)  
[Set Table Anchors in Sheet Formats (VB.NET)](Set_Table_Anchors_Example_VBNET.htm)  
[Set Table Anchors in Sheet Formats (C#)](Set_Table_Anchors_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)  
[ISheet::TableAnchor Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~TableAnchor.md)
