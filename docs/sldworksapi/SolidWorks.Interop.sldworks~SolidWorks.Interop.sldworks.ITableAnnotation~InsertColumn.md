# InsertColumn Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~InsertColumn`

Obsolete. Superseded by ITableAnnnotation::InsertColumn2.
Obsolete. Superseded by [ITableAnnnotation::InsertColumn2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~InsertColumn2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertColumn( _
   ByVal Where As System.Integer, _
   ByVal Index As System.Integer, _
   ByVal Name As System.String _
) As System.Boolean
```

```

Dim instance As ITableAnnotation
Dim Where As System.Integer
Dim Index As System.Integer
Dim Name As System.String
Dim value As System.Boolean
 
value = instance.InsertColumn(Where, Index, Name)
```

```

System.bool InsertColumn( 
   System.int Where,
   System.int Index,
   System.string Name
)
```

```

System.bool InsertColumn( 
   System.int Where,
   System.int Index,
   System.String^ Name
) 
```

#### Parameters

*Where*
:   Where to insert the column as specified in [swTableItemInsertPosition\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTableItemInsertPosition_e.html)

*Index*
:   Index of the column where to insert the new column

*Name*
:   Column name

#### Return Value

True if column is inserted successfully, false if not

Remarks

The index for both rows and columns is 0-based.

Example

[Insert Part Number Column in BOM Table (C#)](Insert_Part_Number_Column_in_BOM_Table_Example_CSharp.htm)  
[Insert Part Number Column in BOM Table (VB.NET)](Insert_Part_Number_Column_in_BOM_Table_Example_VBNET.htm)  
[Insert Part Number Column in BOM Table (VBA)](Insert_Part_Number_Column_in_BOM_Table_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)
