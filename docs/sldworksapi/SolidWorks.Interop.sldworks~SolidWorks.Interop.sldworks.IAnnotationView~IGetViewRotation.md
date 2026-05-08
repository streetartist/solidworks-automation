# IGetViewRotation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~IGetViewRotation`

Gets the rotation matrix of the annotation view relative to the X-Y plane of the model.
Gets the rotation matrix of the annotation view relative to the X-Y plane of the model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetViewRotation() As System.Double
```

```

Dim instance As IAnnotationView
Dim value As System.Double
 
value = instance.IGetViewRotation()
```

```

System.double IGetViewRotation()
```

```

System.double IGetViewRotation(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an array of 9 doubles of the rotation matrix of the annotation view relative to the X-Y plane of the model

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotationView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.md)  
[IAnnotationView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView_members.md)  
[IAnnotation::GetViewRotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~GetViewRotation.md)  
[IAnnotation::GetPlane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPlane.md)
