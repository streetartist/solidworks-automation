# XPosition Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~XPosition`

Gets or sets the X offset direction for the appearance.
Gets or sets the X offset direction for the appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property XPosition As System.Double
```

```

Dim instance As IRenderMaterial
Dim value As System.Double
 
instance.XPosition = value
 
value = instance.XPosition
```

```

System.double XPosition {get; set;}
```

```

property System.double XPosition {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

X offset direction

Remarks

This property offsets the appearance from its original position.

Call [IRenderMaterial::YPosition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~YPosition.md) to set the Y offset direction for the appearance.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)
