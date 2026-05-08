# Rotation Property (IView3D)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D~Rotation`

Gets or sets the 3D View rotation with respect to the Front view.
Gets or sets the 3D View rotation with respect to the Front view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Rotation As MathTransform
```

```

Dim instance As IView3D
Dim value As MathTransform
 
instance.Rotation = value
 
value = instance.Rotation
```

```

MathTransform Rotation {get; set;}
```

```

property MathTransform^ Rotation {
   MathTransform^ get();
   void set (    MathTransform^ value);
}
```

#### Property Value

[IMathTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView3D Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.md)  
[IView3D Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D_members.md)
