# GetAnnotations2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~GetAnnotations2`

Gets the annotations in this annotation view.
Gets the annotations in this annotation view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAnnotations2( _
   ByVal DimXpertOnly As System.Boolean, _
   ByVal UnassignedInPlane As System.Boolean _
) As System.Object
```

```

Dim instance As IAnnotationView
Dim DimXpertOnly As System.Boolean
Dim UnassignedInPlane As System.Boolean
Dim value As System.Object
 
value = instance.GetAnnotations2(DimXpertOnly, UnassignedInPlane)
```

```

System.object GetAnnotations2( 
   System.bool DimXpertOnly,
   System.bool UnassignedInPlane
)
```

```

System.Object^ GetAnnotations2( 
   System.bool DimXpertOnly,
   System.bool UnassignedInPlane
) 
```

#### Parameters

*DimXpertOnly*
:   :   True to get only DimXpert annotations, false to get all annotations

*UnassignedInPlane*
:   True to get annotations on all planes, including annotations on unassigned planes; false to get annotations on all planes, except annotations on unassigned planes

#### Return Value

[Annotations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)

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
[IAnnotationView::AnnotationCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~AnnotationCount.md)
