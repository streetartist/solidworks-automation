# GetAnnotationsByType Method (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetAnnotationsByType`

Gets the annotations of the specified type in this view.
Gets the annotations of the specified type in this view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAnnotationsByType( _
   ByVal Type As System.Integer _
) As System.Object
```

```

Dim instance As IView
Dim Type As System.Integer
Dim value As System.Object
 
value = instance.GetAnnotationsByType(Type)
```

```

System.object GetAnnotationsByType( 
   System.int Type
)
```

```

System.Object^ GetAnnotationsByType( 
   System.int Type
) 
```

#### Parameters

*Type*
:   Annotation type as defined by [swAnnotationType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAnnotationType_e.html)

#### Return Value

Array of [annotations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetAnnotations Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetAnnotations.md)  
[IView::GetFirstAnnotation3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstAnnotation3.md)
