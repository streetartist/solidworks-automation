# EvaluateCellEquation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~EvaluateCellEquation`

Solves the specified equation in the specified cell of this BOM table.
Solves the specified equation in the specified cell of this BOM table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EvaluateCellEquation( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer, _
   ByVal IncludeHidden As System.Boolean, _
   ByVal Equation As System.String, _
   ByRef SolvedValue As System.String _
) As System.Integer
```

```

Dim instance As ITableAnnotation
Dim Row As System.Integer
Dim Column As System.Integer
Dim IncludeHidden As System.Boolean
Dim Equation As System.String
Dim SolvedValue As System.String
Dim value As System.Integer
 
value = instance.EvaluateCellEquation(Row, Column, IncludeHidden, Equation, SolvedValue)
```

```

System.int EvaluateCellEquation( 
   System.int Row,
   System.int Column,
   System.bool IncludeHidden,
   System.string Equation,
   out System.string SolvedValue
)
```

```

System.int EvaluateCellEquation( 
   System.int Row,
   System.int Column,
   System.bool IncludeHidden,
   System.String^ Equation,
   [Out] System.String^ SolvedValue
) 
```

#### Parameters

*Row*
:   0-based index of the row

*Column*
:   0-based index of the column

*IncludeHidden*
:   True to include hidden rows and columns in the Row and Column indexes, false to not

*Equation*
:   Equation to solve; empty string to remove an equation

*SolvedValue*
:   Value of solved Equation

#### Return Value

Return code as defined in [swCellEquationStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCellEquationStatus_e.html)

Example

[Get and Set BOM Column Types and Cell Equations (VBA)](Get_and_Set_Column_Types_and_Cell_Equations_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)  
[ITableAnnotation::GetCellEquation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellEquation.md)  
[ITableAnnotation::SetCellEquation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellEquation.md)  
[ITableAnnotation::GetColumnType3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnType3.md)
