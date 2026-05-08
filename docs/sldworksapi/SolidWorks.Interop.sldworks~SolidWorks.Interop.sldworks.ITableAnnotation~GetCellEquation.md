# GetCellEquation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellEquation`

Gets the equation and its solved value for the specified row and column of this BOM table.
Gets the equation and its solved value for the specified row and column of this BOM table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCellEquation( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer, _
   ByVal IncludeHidden As System.Boolean, _
   ByRef SolvedValue As System.String, _
   ByRef Status As System.Integer _
) As System.String
```

```

Dim instance As ITableAnnotation
Dim Row As System.Integer
Dim Column As System.Integer
Dim IncludeHidden As System.Boolean
Dim SolvedValue As System.String
Dim Status As System.Integer
Dim value As System.String
 
value = instance.GetCellEquation(Row, Column, IncludeHidden, SolvedValue, Status)
```

```

System.string GetCellEquation( 
   System.int Row,
   System.int Column,
   System.bool IncludeHidden,
   out System.string SolvedValue,
   out System.int Status
)
```

```

System.String^ GetCellEquation( 
   System.int Row,
   System.int Column,
   System.bool IncludeHidden,
   [Out] System.String^ SolvedValue,
   [Out] System.int Status
) 
```

#### Parameters

*Row*
:   0-based index of the row, -1 to get the column equation

*Column*
:   0-based index of the column

*IncludeHidden*
:   True to include hidden rows and columns in the Row and Column indexes, false to not

*SolvedValue*
:   Evaluated equation

*Status*
:   Return code as defined in [swCellEquationStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCellEquationStatus_e.html)

#### Return Value

Equation

Example

[Get and Set BOM Column Types and Cell Equations (VBA)](Get_and_Set_Column_Types_and_Cell_Equations_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)  
[ITableAnnotation::SetCellEquation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellEquation.md)  
[ITableAnnotation::EvaluateCellEquation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~EvaluateCellEquation.md)  
[ITableAnnotation::GetColumnType3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnType3.md)
