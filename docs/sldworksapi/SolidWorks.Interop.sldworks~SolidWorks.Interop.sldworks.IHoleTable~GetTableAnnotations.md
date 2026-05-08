# GetTableAnnotations Method (IHoleTable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~GetTableAnnotations`

Gets the hole table annotations for this hole table feature.
Gets the hole table annotations for this hole table feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTableAnnotations() As System.Object
```

```

Dim instance As IHoleTable
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

Array of [IHoleTableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTableAnnotation.md) objects for this hole table feature

Remarks

Because many of the [ITableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md) APIs apply to all parts of a table annotation that has been split, you might not want all of the table annotations when just one table annotation would be sufficient.

Example

[Hide or Show First Column in Hole Table (VB.NET)](Hide_or_Show_First_Column_in_Hole_Table_Example_VBNET.htm)  
[Hide or Show First Column in Hole Table (VBA)](Hide_or_Show_First_Column_in_Hole_Table_Example_VB.htm)  
[Hide or Show First Column in Hole Table (C#)](Hide_or_Show_First_Column_in_Hole_Table_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHoleTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable.md)  
[IHoleTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable_members.md)  
[IHoleTable::GetTableAnnotationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~GetTableAnnotationCount.md)  
[IHoleTable::IGetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~IGetTableAnnotations.md)
