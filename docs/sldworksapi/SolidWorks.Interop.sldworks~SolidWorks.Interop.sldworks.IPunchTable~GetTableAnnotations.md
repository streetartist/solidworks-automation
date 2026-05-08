# GetTableAnnotations Method (IPunchTable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable~GetTableAnnotations`

Gets the punch table annotations for this punch table feature.
Gets the punch table annotations for this punch table feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTableAnnotations() As System.Object
```

```

Dim instance As IPunchTable
Dim value As System.Object
 
value = instance.GetTableAnnotations()
```

```

System.object GetTableAnnotations()
```

```

System.Object^ GetTableAnnotations(); 
```

#### Return Value

Array of [IPunchTableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTableAnnotation.md) objects for this punch table feature

Remarks

This method gets all of the table annotations of a split table. Many of the [ITableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md) methods and properties get table annotation information that is common to all table annotations. You should apply these [ITableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md) methods and properties to only one of the split table annotations returned by this method. Otherwise, you will get redundant data.

Example

[Insert Punch Table (VBA)](Insert_Punch_Table_Example_VB.htm)  
[Insert Punch Table (VB.NET)](Insert_Punch_Table_Example_VBNET.htm)  
[Insert Punch Table (C#)](Insert_Punch_Table_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPunchTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable.md)  
[IPunchTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable_members.md)  
[IPunchTable::IGetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable~IGetTableAnnotations.md)
