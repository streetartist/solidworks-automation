# IGetTableAnnotations Method (IPunchTable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable~IGetTableAnnotations`

Gets the punch table annotations for this punch table feature.
Gets the punch table annotations for this punch table feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetTableAnnotations( _
   ByVal Count As System.Integer _
) As PunchTableAnnotation
```

```

Dim instance As IPunchTable
Dim Count As System.Integer
Dim value As PunchTableAnnotation
 
value = instance.IGetTableAnnotations(Count)
```

```

PunchTableAnnotation IGetTableAnnotations( 
   System.int Count
)
```

```

PunchTableAnnotation^ IGetTableAnnotations( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of punch table annotations for this punch table feature (see **Remarks**)

#### Return Value

- In-process, unmanaged C++: Pointer to the [IPunchTableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTableAnnotation.md) objects for this punch table feature

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

This method gets all of the table annotations of a split table. Many of the [ITableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md) methods and properties get table annotation information that is common to all table annotations. You should apply these [ITableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md) methods and properties to only one of the split table annotations returned by this method. Otherwise, you will get redundant data.

For example, if you change the thickness of the grid line, then changing it on one table annotation affects all splits of that table annotation. Thus, for this method, you might want to specify 1 for Count so that a single value is returned. Or, you can call [IPunchTable::GetTableAnnotationCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable~GetTableAnnotationCount.md) if you want the total number of table annotations, including any splits, for this punch table feature.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPunchTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable.md)  
[IPunchTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable_members.md)  
[IPunchTable::GetTableAnnotations Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable~GetTableAnnotations.md)
