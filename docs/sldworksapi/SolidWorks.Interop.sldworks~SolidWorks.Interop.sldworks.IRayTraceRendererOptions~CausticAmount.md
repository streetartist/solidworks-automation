# CausticAmount Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~CausticAmount`

Gets or sets the maximum number of photons fired, which controls the amount of visible caustics.
Gets or sets the maximum number of photons fired, which controls the amount of visible caustics.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CausticAmount As System.Integer
```

```

Dim instance As IRayTraceRendererOptions
Dim value As System.Integer
 
instance.CausticAmount = value
 
value = instance.CausticAmount
```

```

System.int CausticAmount {get; set;}
```

```

property System.int CausticAmount {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Maximum number of photons fired

Remarks

Increasing the amount of photons fired creates sharper and clearer caustics but increases rendering time.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.md)  
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.md)  
[IRayTraceRendererOptions::CausticQuality Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~CausticQuality.md)  
[IRayTraceRendererOptions::DirectCaustics Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~DirectCaustics.md)
