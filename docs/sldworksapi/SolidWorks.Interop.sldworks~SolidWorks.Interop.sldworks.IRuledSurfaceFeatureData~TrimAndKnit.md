# TrimAndKnit Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~TrimAndKnit`

Gets or sets whether to trim and knit the surfaces of this ruled-surface feature.
Gets or sets whether to trim and knit the surfaces of this ruled-surface feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TrimAndKnit As System.Boolean
```

```

Dim instance As IRuledSurfaceFeatureData
Dim value As System.Boolean
 
instance.TrimAndKnit = value
 
value = instance.TrimAndKnit
```

```

System.bool TrimAndKnit {get; set;}
```

```

property System.bool TrimAndKnit {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to trim and knit surfaces, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRuledSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData.md)  
[IRuledSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData_members.md)
