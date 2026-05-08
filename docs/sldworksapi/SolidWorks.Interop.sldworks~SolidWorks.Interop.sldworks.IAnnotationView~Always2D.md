# Always2D Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Always2D`

Gets whether to display annotations in 2D or 3D.
Gets whether to display annotations in 2D or 3D.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Always2D As System.Boolean
```

```

Dim instance As IAnnotationView
Dim value As System.Boolean
 
value = instance.Always2D
```

```

System.bool Always2D {get;}
```

```

property System.bool Always2D {
   System.bool get();
}
```

#### Property Value

True to display annotations in 2D, false to display them in 3D

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotationView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.md)  
[IAnnotationView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView_members.md)
