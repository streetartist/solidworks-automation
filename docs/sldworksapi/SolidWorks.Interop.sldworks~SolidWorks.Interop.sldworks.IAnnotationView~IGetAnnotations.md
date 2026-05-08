# IGetAnnotations Method (IAnnotationView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~IGetAnnotations`

Obsolete. Superseded by IAnnotationView::GetAnnotations2.
Obsolete. Superseded by [IAnnotationView::GetAnnotations2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~GetAnnotations2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetAnnotations( _
   ByVal AnnotationCount As System.Integer _
) As Annotation
```

```

Dim instance As IAnnotationView
Dim AnnotationCount As System.Integer
Dim value As Annotation
 
value = instance.IGetAnnotations(AnnotationCount)
```

```

Annotation IGetAnnotations( 
   System.int AnnotationCount
)
```

```

Annotation^ IGetAnnotations( 
   System.int AnnotationCount
) 
```

#### Parameters

*AnnotationCount*
:   Number of annotations

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [annotations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IAnnotationView::AnnotationCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~AnnotationCount.md) to get the value for AnnotationCount.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotationView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.md)  
[IAnnotationView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView_members.md)  
[IAnnotationView::Annotations Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Annotations.md)
