# IGetTableAnnotations Method (IGeneralTableFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableFeature~IGetTableAnnotations`

Gets the table annotations for this general table feature.
Gets the table annotations for this general table feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetTableAnnotations( _
   ByVal Count As System.Integer _
) As TableAnnotation
```

```

Dim instance As IGeneralTableFeature
Dim Count As System.Integer
Dim value As TableAnnotation
 
value = instance.IGetTableAnnotations(Count)
```

```

TableAnnotation IGetTableAnnotations( 
   System.int Count
)
```

```

TableAnnotation^ IGetTableAnnotations( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of table annotations

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [IGeneralTableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableAnnotation.md) objects

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [IGeneralTableFeature::GetTableAnnotationCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableFeature~GetTableAnnotationCount.md) before calling this method to get the size of the array.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGeneralTableFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableFeature.md)  
[IGeneralTableFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableFeature_members.md)  
[IGeneralTableFeature::GetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableFeature~GetTableAnnotations.md)
