# CausticsCast Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~CausticsCast`

Gets or sets whether specular materials reflect caustic photons for illuminating this appearance.
Gets or sets whether specular materials reflect caustic photons for illuminating this appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CausticsCast As System.Boolean
```

```

Dim instance As IRenderMaterial
Dim value As System.Boolean
 
instance.CausticsCast = value
 
value = instance.CausticsCast
```

```

System.bool CausticsCast {get; set;}
```

```

property System.bool CausticsCast {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if specular materials reflect caustic photons, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)
