# AnnotationViews2 Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D~AnnotationViews2`

Gets the annotation views assigned to this 3D View.
Gets the annotation views assigned to this 3D View.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property AnnotationViews2 As System.Object
```

```

Dim instance As IView3D
Dim value As System.Object
 
value = instance.AnnotationViews2
```

```

System.object AnnotationViews2 {get;}
```

```

property System.Object^ AnnotationViews2 {
   System.Object^ get();
}
```

#### Property Value

Array of [IAnnotationView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView3D Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.md)  
[IView3D Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D_members.md)
