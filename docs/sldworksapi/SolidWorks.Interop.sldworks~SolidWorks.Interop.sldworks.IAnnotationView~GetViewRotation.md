# GetViewRotation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~GetViewRotation`

Gets the rotation matrix of the annotation view relative to the X-Y plane of the model.
Gets the rotation matrix of the annotation view relative to the X-Y plane of the model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetViewRotation() As System.Object
```

```

Dim instance As IAnnotationView
Dim value As System.Object
 
value = instance.GetViewRotation()
```

```

System.object GetViewRotation()
```

```

System.Object^ GetViewRotation(); 
```

#### Return Value

Array of 9 doubles of the rotation matrix of the annotation view relative to the X-Y plane of the model

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotationView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.md)  
[IAnnotationView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView_members.md)  
[IAnnotation::IGetViewRotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~IGetViewRotation.md)  
[IAnnotation::GetPlane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPlane.md)
