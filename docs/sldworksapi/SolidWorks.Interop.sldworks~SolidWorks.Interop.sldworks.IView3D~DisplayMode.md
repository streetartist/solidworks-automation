# DisplayMode Property (IView3D)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D~DisplayMode`

Gets or sets the display mode of this 3D View.
Gets or sets the display mode of this 3D View.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DisplayMode As System.Integer
```

```

Dim instance As IView3D
Dim value As System.Integer
 
instance.DisplayMode = value
 
value = instance.DisplayMode
```

```

System.int DisplayMode {get; set;}
```

```

property System.int DisplayMode {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Display mode as defined in [swDisplayMode\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDisplayMode_e.html)

Example

See the [IView3D](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView3D Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.md)  
[IView3D Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D_members.md)
