# IReorderSheets Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IReorderSheets`

Reorders the drawing sheets per their positions in the input array.
Reorders the drawing sheets per their positions in the input array.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IReorderSheets( _
   ByVal SheetCount As System.Integer, _
   ByRef NewSheetList As System.String _
) As System.Boolean
```

```

Dim instance As IDrawingDoc
Dim SheetCount As System.Integer
Dim NewSheetList As System.String
Dim value As System.Boolean
 
value = instance.IReorderSheets(SheetCount, NewSheetList)
```

```

System.bool IReorderSheets( 
   System.int SheetCount,
   ref System.string NewSheetList
)
```

```

System.bool IReorderSheets( 
   System.int SheetCount,
   System.String^% NewSheetList
) 
```

#### Parameters

*SheetCount*
:   Number of sheets to reorder

*NewSheetList*
:   Array of the names of the sheets to reorder

#### Return Value

True if the sheets are reordered per their position in NewSheetList, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::ReorderSheets Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ReorderSheets.md)  
[IDrawingDoc::ActivateSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActivateSheet.md)  
[IDrawingDoc::EditSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditSheet.md)  
[IDrawingDoc::GetCurrentSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetCurrentSheet.md)  
[IDrawingDoc::GetEditSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetEditSheet.md)  
[IDrawingDoc::GetSheetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetSheetCount.md)  
[IDrawingDoc::GetSheetNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetSheetNames.md)  
[IDrawingDoc::IGetCurrentSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetCurrentSheet.md)  
[IDrawingDoc::IGetSheetNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetSheetNames.md)  
[IDrawingDoc::SetupSheet4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetupSheet4.md)  
[ISheet::GetName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetName.md)  
[ISheet::SetName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetName.md)
