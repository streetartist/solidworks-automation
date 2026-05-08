# BlurryReflection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting~BlurryReflection`

Gets or sets whether to blur the reflections of surfaces.
Gets or sets whether to blur the reflections of surfaces.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BlurryReflection As System.Boolean
```

```

Dim instance As IAppearanceSetting
Dim value As System.Boolean
 
instance.BlurryReflection = value
 
value = instance.BlurryReflection
```

```

System.bool BlurryReflection {get; set;}
```

```

property System.bool BlurryReflection {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to blur reflections, false to not

Remarks

See SOLIDWORKS Help for more information about appearances.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAppearanceSetting Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting.md)  
[IAppearanceSetting Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting_members.md)
