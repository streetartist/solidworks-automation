# SetColumnType3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnType3`

Sets the type and property data for the specified BOM table column.
Sets the type and property data for the specified BOM table column.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetColumnType3( _
   ByVal Index As System.Integer, _
   ByVal ColumnType As System.Integer, _
   ByVal IncludeHidden As System.Boolean, _
   ByVal PropertyData As System.Object _
) As System.Integer
```

```

Dim instance As ITableAnnotation
Dim Index As System.Integer
Dim ColumnType As System.Integer
Dim IncludeHidden As System.Boolean
Dim PropertyData As System.Object
Dim value As System.Integer
 
value = instance.SetColumnType3(Index, ColumnType, IncludeHidden, PropertyData)
```

```

System.int SetColumnType3( 
   System.int Index,
   System.int ColumnType,
   System.bool IncludeHidden,
   System.object PropertyData
)
```

```

System.int SetColumnType3( 
   System.int Index,
   System.int ColumnType,
   System.bool IncludeHidden,
   System.Object^ PropertyData
) 
```

#### Parameters

*Index*
:   0-based index of the column whose type to set

*ColumnType*
:   Type of column as defined in [swTableColumnTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTableColumnTypes_e.html) (see **Remarks**)

*IncludeHidden*
:   True to include hidden columns in Index, false to not

*PropertyData*
:   Property data specific to ColumnType (see **Remarks**)

#### Return Value

Return code as defined in [swColumnTypeStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swColumnTypeStatus_e.html)

Remarks

PropertyData specifies the column title and contents.

| If ColumnType is set to swTableColumnTypes\_e.... | Then Set PropertyData with... |
| --- | --- |
| swBomTableColumnType\_CustomProperty | Valid property name\* |
| swBomTableColumnType\_UnitOfMeasure | Valid property name\* |
| swBomTableColumnType\_Equation | Equation string |
| swBomTableColumnType\_ComponentReference | Null or Nothing |
| swBomTableColumnType\_ToolboxProperty | Property as defined in [swToolBoxPropertyName\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swToolBoxPropertyName_e.html) |
| swBomTableColumnType\_CutListProperties (valid only for sheetmetal parts) | Valid cutlist property name\* |
| swBomTableColumnType\_ItemNumber | Array of four values {*Start\_Item\_Int*, *Increment\_Int*, *Order\_balloons\_and\_BOM\_to\_follow\_assembly\_order\_Bool*, *Do\_not\_change\_BOM\_item\_number\_Bool*} |
| swBomTableColumnType\_PartNumber | True to use title summary, false to not |

\* Note: To get the valid property names for a given column type, open a part in SOLIDWORKS and add a BOM table to it. Right-click a column and select **Insert > Column Right**. In the popup, select the column type of interest in the first dropdown. Inspect the contents of the second dropdown to see the valid property names for the column type.

When you set a column type, the title is automatically changed to match that column type. If you change the column type to custom property, you must set the column title using [ITableAnnotation::SetColumnTitle2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnTitle2.md).

This method is consistent with the SOLIDWORKS user interface where you cannot add, delete, or replace the Quantity type column in a BOM table.

Example

[Get and Set BOM Column Types and Cell Equations (VBA)](Get_and_Set_Column_Types_and_Cell_Equations_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)  
[ITableAnnotation::GetColumnType3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnType3.md)  
[ITableAnnotation::SetCellEquation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellEquation.md)
