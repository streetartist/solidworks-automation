# IGetTableAnnotations Method (IRevisionTableFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableFeature~IGetTableAnnotations`

Gets the revision table annotations for this revision table.
Gets the revision table annotations for this revision table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetTableAnnotations( _
   ByVal Count As System.Integer _
) As RevisionTableAnnotation
```

```

Dim instance As IRevisionTableFeature
Dim Count As System.Integer
Dim value As RevisionTableAnnotation
 
value = instance.IGetTableAnnotations(Count)
```

```

RevisionTableAnnotation IGetTableAnnotations( 
   System.int Count
)
```

```

RevisionTableAnnotation^ IGetTableAnnotations( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of revision table annotations

#### Return Value

- in-process, unmanaged C++: Pointer to an array of the [revision table annotations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [IRevisionTableFeature::GetTableAnnotationCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableFeature~GetTableAnnotationCount.md) before calling this method to get the value of Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRevisionTableFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableFeature.md)  
[IRevisionTableFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableFeature_members.md)  
[IRevisionTableFeature::GetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableFeature~GetTableAnnotations.md)
