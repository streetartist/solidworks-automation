# GetTableAnnotationCount Method (IBendTable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable~GetTableAnnotationCount`

Gets the number of bend table annotations.
Gets the number of bend table annotations.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTableAnnotationCount() As System.Integer
```

```

Dim instance As IBendTable
Dim value As System.Integer
 
value = instance.GetTableAnnotationCount()
```

```

System.int GetTableAnnotationCount()
```

```

System.int GetTableAnnotationCount(); 
```

#### Return Value

Number of bend table annotations (see **Remarks**)

Remarks

There is usually only one annotation for each bend table. If a bend table is split, there are two annotations associated with it.

Example

[Insert Bend Table (VBA)](Insert_Bend_Table_Example_VB.htm)  
[Insert Bend Table (VB.NET)](Insert_Bend_Table_Example_VBNET.htm)  
[Insert Bend Table (C#)](Insert_Bend_Table_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBendTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable.md)  
[IBendTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable_members.md)  
[IBendTable::GetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable~GetTableAnnotations.md)  
[IGetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable~IGetTableAnnotations.md)
