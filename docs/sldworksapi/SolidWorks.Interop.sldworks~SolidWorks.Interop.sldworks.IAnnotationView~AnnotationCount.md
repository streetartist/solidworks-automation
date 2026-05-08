# AnnotationCount Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~AnnotationCount`

Gets the number of annotations in this annotation view.
Gets the number of [annotations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md) in this annotation view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property AnnotationCount As System.Integer
```

```

Dim instance As IAnnotationView
Dim value As System.Integer
 
value = instance.AnnotationCount
```

```

System.int AnnotationCount {get;}
```

```

property System.int AnnotationCount {
   System.int get();
}
```

#### Property Value

Number of annotations

Remarks

Call this method before calling [IAnnotationView::IGetAnnotations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~IGetAnnotations.md) to get the size of the array for that method.

Example

[Move Annotations to Notes Area Annotation View (C#)](Move_Annotations_to_First_Annotation_View_Example_CSharp.htm)  
[Move Annotations to Notes Area Annotation View (VB.NET)](Move_Annotations_to_First_Annotation_View_Example_VBNET.htm)  
[Move Annotations to Notes Area Annotation View (VBA)](Move_Annotations_to_First_Annotation_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotationView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.md)  
[IAnnotationView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView_members.md)  
[IAnnotationView::Annotations Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Annotations.md)
