# AccurateReflections Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~AccurateReflections`

Selects or clears the Accurate reflections (slower) setting, which controls the level of surface reflections, for illuminating this appearance.
Selects or clears the Accurate reflections (slower) setting, which controls the level of surface reflections, for illuminating this appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AccurateReflections As System.Boolean
```

```

Dim instance As IRenderMaterial
Dim value As System.Boolean
 
instance.AccurateReflections = value
 
value = instance.AccurateReflections
```

```

System.bool AccurateReflections {get; set;}
```

```

property System.bool AccurateReflections {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to select the Accurate reflections (slower) setting, false to clear it

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)
