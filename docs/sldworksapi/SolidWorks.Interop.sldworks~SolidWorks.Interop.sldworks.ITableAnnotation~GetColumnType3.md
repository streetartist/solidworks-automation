# GetColumnType3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnType3`

Gets the type and property data for the specified BOM table column.
Gets the type and property data for the specified BOM table column.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetColumnType3( _
   ByVal Index As System.Integer, _
   ByVal IncludeHidden As System.Boolean, _
   ByRef PropertyData As System.Object, _
   ByRef Status As System.Integer _
) As System.Integer
```

```

Dim instance As ITableAnnotation
Dim Index As System.Integer
Dim IncludeHidden As System.Boolean
Dim PropertyData As System.Object
Dim Status As System.Integer
Dim value As System.Integer
 
value = instance.GetColumnType3(Index, IncludeHidden, PropertyData, Status)
```

```

System.int GetColumnType3( 
   System.int Index,
   System.bool IncludeHidden,
   out System.object PropertyData,
   out System.int Status
)
```

```

System.int GetColumnType3( 
   System.int Index,
   System.bool IncludeHidden,
   [Out] System.Object^ PropertyData,
   [Out] System.int Status
) 
```

#### Parameters

*Index*
:   0-based index of the column whose type to get

*IncludeHidden*
:   True to include hidden columns in Index, false to not

*PropertyData*
:   Property data specific to the type of column (see **Remarks**)

*Status*
:   Return code as defined in [swColumnTypeStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swColumnTypeStatus_e.html)

#### Return Value

Type of column as defined in [swTableColumnTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTableColumnTypes_e.html)

Remarks

PropertyData varies by the type of column. See the Remarks in [ITableAnnotation::SetColumnType3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnType3.md).

Example

[Get and Set BOM Column Types and Cell Equations (VBA)](Get_and_Set_Column_Types_and_Cell_Equations_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)  
[ITableAnnotation::GetCellEquation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellEquation.md)
