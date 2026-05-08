# WidthMirror Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~WidthMirror`

Gets or sets whether to flip the appearance texture about the selected direction horizontally.
Gets or sets whether to flip the appearance texture about the selected direction horizontally.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property WidthMirror As System.Boolean
```

```

Dim instance As IRenderMaterial
Dim value As System.Boolean
 
instance.WidthMirror = value
 
value = instance.WidthMirror
```

```

System.bool WidthMirror {get; set;}
```

```

property System.bool WidthMirror {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to flip the appearance texture about the selected direction horizontally, false to not

Remarks

Call [IRenderMaterial::HeightMirror](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~HeightMirror.md) to flip the appearance texture about the selected direction vertically.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)
