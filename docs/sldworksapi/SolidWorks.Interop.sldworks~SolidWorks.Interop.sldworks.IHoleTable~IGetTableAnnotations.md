# IGetTableAnnotations Method (IHoleTable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~IGetTableAnnotations`

Gets the hole table annotations for this hole table feature.
Gets the hole table annotations for this hole table feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetTableAnnotations( _
   ByVal Count As System.Integer _
) As HoleTableAnnotation
```

```

Dim instance As IHoleTable
Dim Count As System.Integer
Dim value As HoleTableAnnotation
 
value = instance.IGetTableAnnotations(Count)
```

```

HoleTableAnnotation IGetTableAnnotations( 
   System.int Count
)
```

```

HoleTableAnnotation^ IGetTableAnnotations( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of hole table annotations for this hole table feature (see **Remarks**)

#### Return Value

- in-process, unmanaged C++: Pointer to the [IHoleTableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTableAnnotation.md) objects for this hole table feature

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Because many of the [ITableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md) APIs apply to all parts of a table annotation that has been split, you might not want all of the table annotations when just one table annotation would be sufficient.

For example, if you change the thickness of the grid line, then changing it on one table annotation affects all splits of that table annotation. Thus, for this method, you might want to specify 1 for Count so that a single value is returned. Or, you can call [IHoleTable::GetTableAnnotationCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~GetTableAnnotationCount.md) if you want the total number of table annotations, including any splits, for this hole table feature.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHoleTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable.md)  
[IHoleTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable_members.md)
