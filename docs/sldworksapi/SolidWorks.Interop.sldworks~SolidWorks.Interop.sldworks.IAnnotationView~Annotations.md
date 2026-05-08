# Annotations Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Annotations`

Obsolete. Superseded by IAnnotationView::GetAnnotations2.
Obsolete. Superseded by [IAnnotationView::GetAnnotations2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~GetAnnotations2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Annotations As System.Object
```

```

Dim instance As IAnnotationView
Dim value As System.Object
 
value = instance.Annotations
```

```

System.object Annotations {get;}
```

```

property System.Object^ Annotations {
   System.Object^ get();
}
```

#### Property Value

[Annotations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotationView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.md)  
[IAnnotationView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView_members.md)  
[IAnnotationView::IGetAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~IGetAnnotations.md)  
[IAnnotationView::AnnotationCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~AnnotationCount.md)
