# CausticsReceive Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~CausticsReceive`

Gets or sets whether diffuse materials absorb caustic photons for illuminating this appearance.
Gets or sets whether diffuse materials absorb caustic photons for illuminating this appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CausticsReceive As System.Boolean
```

```

Dim instance As IRenderMaterial
Dim value As System.Boolean
 
instance.CausticsReceive = value
 
value = instance.CausticsReceive
```

```

System.bool CausticsReceive {get; set;}
```

```

property System.bool CausticsReceive {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if diffuse materials absorb caustic photons, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)
