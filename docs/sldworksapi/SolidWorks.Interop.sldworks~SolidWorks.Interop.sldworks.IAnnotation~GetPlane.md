# GetPlane Method (IAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPlane`

Gets the rotation matrix of the annotation relative to the X-Y plane of the model.
Gets the rotation matrix of the annotation relative to the X-Y plane of the model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPlane() As System.Object
```

```

Dim instance As IAnnotation
Dim value As System.Object
 
value = instance.GetPlane()
```

```

System.object GetPlane()
```

```

System.Object^ GetPlane(); 
```

#### Return Value

Array of 9 doubles of the rotation matrix of the annotation relative to the X-Y plane of the model

Example

[Move Annotations to Notes Area Annotation View (C#)](Move_Annotations_to_First_Annotation_View_Example_CSharp.htm)  
[Move Annotations to Notes Area Annotation View (VB.NET)](Move_Annotations_to_First_Annotation_View_Example_VBNET.htm)  
[Move Annotations to Notes Area Annotation View (VBA)](Move_Annotations_to_First_Annotation_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)  
[IAnnotationView::GetViewRotation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~GetViewRotation.md)  
[IAnnotationView::IGetViewRotation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~IGetViewRotation.md)  
[IDisplayData::GetTextPlaneAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextPlaneAtIndex.md)
