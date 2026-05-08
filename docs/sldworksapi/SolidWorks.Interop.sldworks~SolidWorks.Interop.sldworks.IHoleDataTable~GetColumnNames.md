# GetColumnNames Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable~GetColumnNames`

Gets the names of all the columns in this Hole Wizard fastener table.
Gets the names of all the columns in this Hole Wizard fastener table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetColumnNames( _
   ByRef ColumnNames As System.Object _
) As System.Boolean
```

```

Dim instance As IHoleDataTable
Dim ColumnNames As System.Object
Dim value As System.Boolean
 
value = instance.GetColumnNames(ColumnNames)
```

```

System.bool GetColumnNames( 
   out System.object ColumnNames
)
```

```

System.bool GetColumnNames( 
   [Out] System.Object^ ColumnNames
) 
```

#### Parameters

*ColumnNames*
:   Array of column names

#### Return Value

True if column names successfully retrieved, false if not

Example

See the [IHoleDataTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHoleDataTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable.md)  
[IHoleDataTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable_members.md)
