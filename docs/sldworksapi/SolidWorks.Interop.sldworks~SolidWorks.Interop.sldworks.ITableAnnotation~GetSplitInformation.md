# GetSplitInformation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetSplitInformation`

Gets information about any splits in this table.
Gets information about any splits in this table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSplitInformation( _
   ByRef Index As System.Integer, _
   ByRef Count As System.Integer, _
   ByRef RangeStart As System.Integer, _
   ByRef RangeEnd As System.Integer _
) As System.Integer
```

```

Dim instance As ITableAnnotation
Dim Index As System.Integer
Dim Count As System.Integer
Dim RangeStart As System.Integer
Dim RangeEnd As System.Integer
Dim value As System.Integer
 
value = instance.GetSplitInformation(Index, Count, RangeStart, RangeEnd)
```

```

System.int GetSplitInformation( 
   out System.int Index,
   out System.int Count,
   out System.int RangeStart,
   out System.int RangeEnd
)
```

```

System.int GetSplitInformation( 
   [Out] System.int Index,
   [Out] System.int Count,
   [Out] System.int RangeStart,
   [Out] System.int RangeEnd
) 
```

#### Parameters

*Index*
:   Piece of the table that this is

*Count*
:   Piece of the table that this is

*RangeStart*
:   Beginning row for this piece of the table

*RangeEnd*
:   Ending row for this piece of the table

#### Return Value

Direction in which the table was split as defined by [swTableSplitDirection\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTableSplitDirection_e.html)

Remarks

A table split is a table divided into multiple tables, also called pieces.

Example

[Export BOMs to XML (C#)](Export_BOMs_to_XML_Example_CSharp.htm)  
[Export BOMs to XML (VB.NET)](Export_BOMs_to_XML_Example_VBNET.htm)  
[Export BOMs to XML (VBA)](Export_BOMs_to_XML_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)  
[ITableAnnotation::Split Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Split.md)  
[ITableAnnotation::HorizontalAutoSplit Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~HorizontalAutoSplit.md)  
[ITableAnnotation::StopAutoSplitting Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~StopAutoSplitting.md)
