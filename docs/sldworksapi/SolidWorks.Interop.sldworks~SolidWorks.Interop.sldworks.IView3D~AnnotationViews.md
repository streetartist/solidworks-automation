# AnnotationViews Property (IView3D)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D~AnnotationViews`

Gets or sets the annotation views assigned to this 3D View.
Gets or sets the annotation views assigned to this 3D View.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AnnotationViews As System.Object
```

```

Dim instance As IView3D
Dim value As System.Object
 
instance.AnnotationViews = value
 
value = instance.AnnotationViews
```

```

System.object AnnotationViews {get; set;}
```

```

property System.Object^ AnnotationViews {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of [IAnnotationView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.md)s

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView3D Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.md)  
[IView3D Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D_members.md)
