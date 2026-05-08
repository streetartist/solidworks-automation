# GetFlipPlaneTransform Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetFlipPlaneTransform`

Gets the transformation matrix of the annotation plane in the opposite direction.
Gets the transformation matrix of the annotation plane in the opposite direction.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFlipPlaneTransform() As MathTransform
```

```

Dim instance As IAnnotation
Dim value As MathTransform
 
value = instance.GetFlipPlaneTransform()
```

```

MathTransform GetFlipPlaneTransform()
```

```

MathTransform^ GetFlipPlaneTransform(); 
```

#### Return Value

[Transformation matrix](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md) of the annotation plane in the opposite direction

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
