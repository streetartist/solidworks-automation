# SetCellEquation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellEquation`

Sets the specified equation for the specified row and column of this BOM table.
Sets the specified equation for the specified row and column of this BOM table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetCellEquation( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer, _
   ByVal IncludeHidden As System.Boolean, _
   ByVal Equation As System.String _
) As System.Integer
```

```

Dim instance As ITableAnnotation
Dim Row As System.Integer
Dim Column As System.Integer
Dim IncludeHidden As System.Boolean
Dim Equation As System.String
Dim value As System.Integer
 
value = instance.SetCellEquation(Row, Column, IncludeHidden, Equation)
```

```

System.int SetCellEquation( 
   System.int Row,
   System.int Column,
   System.bool IncludeHidden,
   System.string Equation
)
```

```

System.int SetCellEquation( 
   System.int Row,
   System.int Column,
   System.bool IncludeHidden,
   System.String^ Equation
) 
```

#### Parameters

*Row*
:   0-based index of the row, -1 to set a column equation

*Column*
:   0-based index of the column

*IncludeHidden*
:   True to include hidden rows and columns in the Row and Column indexes, false to not

*Equation*
:   Equation

#### Return Value

Return code as defined in [swCellEquationStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCellEquationStatus_e.html)

Remarks

After calling this method, call [IModelDoc2::EditRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md) to refresh the table in the user interface.

Example

[Get and Set BOM Column Types and Cell Equations (VBA)](Get_and_Set_Column_Types_and_Cell_Equations_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)  
[ITableAnnotation::GetCellEquation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellEquation.md)  
[ITableAnnotation::EvaluateCellEquation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~EvaluateCellEquation.md)
