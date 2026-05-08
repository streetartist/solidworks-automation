# IGetAnnotations Method (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetAnnotations`

Gets the annotations in this view.
Gets the annotations in this view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetAnnotations( _
   ByVal NumAnnotations As System.Integer _
) As Annotation
```

```

Dim instance As IView
Dim NumAnnotations As System.Integer
Dim value As Annotation
 
value = instance.IGetAnnotations(NumAnnotations)
```

```

Annotation IGetAnnotations( 
   System.int NumAnnotations
)
```

```

Annotation^ IGetAnnotations( 
   System.int NumAnnotations
) 
```

#### Parameters

*NumAnnotations*
:   Number of annotations

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [annotations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [IView::GetAnnotationCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetAnnotationCount.md) before calling this method to get the value for NumAnnotations.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetAnnotations.md)  
[IView::GetFirstAnnotation3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstAnnotation3.md)
