# IGetTableAnnotations Method (ITitleBlockTableFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlockTableFeature~IGetTableAnnotations`

Gets all of the title block table annotations in this title block table feature.
Gets all of the title block table annotations in this title block table feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetTableAnnotations( _
   ByVal Count As System.Integer _
) As TitleBlockTableAnnotation
```

```

Dim instance As ITitleBlockTableFeature
Dim Count As System.Integer
Dim value As TitleBlockTableAnnotation
 
value = instance.IGetTableAnnotations(Count)
```

```

TitleBlockTableAnnotation IGetTableAnnotations( 
   System.int Count
)
```

```

TitleBlockTableAnnotation^ IGetTableAnnotations( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of annotations in this title block feature

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [title block table annotations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlockTableAnnotation.md)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

Remarks

Before calling this method, call [ITitleBlockTableFeature::GetTableAnnotationCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlockTableFeature~GetTableAnnotationCount.md) to get the value for Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITitleBlockTableFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlockTableFeature.md)  
[ITitleBlockTableFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlockTableFeature_members.md)
