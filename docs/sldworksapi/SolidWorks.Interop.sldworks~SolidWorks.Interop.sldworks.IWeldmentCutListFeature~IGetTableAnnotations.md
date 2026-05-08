# IGetTableAnnotations Method (IWeldmentCutListFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~IGetTableAnnotations`

Gets the weldment cut list annotations for this weldment cut list table.
Gets the weldment cut list annotations for this weldment cut list table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetTableAnnotations( _
   ByVal Count As System.Integer _
) As WeldmentCutListAnnotation
```

```

Dim instance As IWeldmentCutListFeature
Dim Count As System.Integer
Dim value As WeldmentCutListAnnotation
 
value = instance.IGetTableAnnotations(Count)
```

```

WeldmentCutListAnnotation IGetTableAnnotations( 
   System.int Count
)
```

```

WeldmentCutListAnnotation^ IGetTableAnnotations( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of weldment cut list annotations for this weldment cut list feature

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [weldment cut-list annotations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation.md) for this weldment cut list table

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IWeldmentCutListFeature::GetTableAnnotationCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~GetTableAnnotationCount.md) to get Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldmentCutListFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature.md)  
[IWeldmentCutListFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature_members.md)  
[IWeldmentCutListFeature::GetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~GetTableAnnotations.md)
