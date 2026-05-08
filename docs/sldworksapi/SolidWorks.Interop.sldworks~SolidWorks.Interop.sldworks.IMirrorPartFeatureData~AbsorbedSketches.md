# AbsorbedSketches Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~AbsorbedSketches`

Gets or sets whether to import absorbed sketches.
Gets or sets whether to import absorbed sketches.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AbsorbedSketches As System.Boolean
```

```

Dim instance As IMirrorPartFeatureData
Dim value As System.Boolean
 
instance.AbsorbedSketches = value
 
value = instance.AbsorbedSketches
```

```

System.bool AbsorbedSketches {get; set;}
```

```

property System.bool AbsorbedSketches {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to import absorbed sketches, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMirrorPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData.md)  
[IMirrorPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData_members.md)  
[IMirrorPartFeatureData::UnabsorbedSketches Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~UnabsorbedSketches.md)
