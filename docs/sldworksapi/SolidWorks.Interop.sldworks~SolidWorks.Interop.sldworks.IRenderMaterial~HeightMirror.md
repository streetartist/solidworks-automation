# HeightMirror Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~HeightMirror`

Gets or sets whether to flip the appearance texture about the selected direction vertically.
Gets or sets whether to flip the appearance texture about the selected direction vertically.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property HeightMirror As System.Boolean
```

```

Dim instance As IRenderMaterial
Dim value As System.Boolean
 
instance.HeightMirror = value
 
value = instance.HeightMirror
```

```

System.bool HeightMirror {get; set;}
```

```

property System.bool HeightMirror {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to flip the appearance texture about the selected direction vertically, false to not

Remarks

Call [IRenderMaterial::WidthMirror](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~WidthMirror.md) to flip the appearance texture about the selected direction horizontally.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)
