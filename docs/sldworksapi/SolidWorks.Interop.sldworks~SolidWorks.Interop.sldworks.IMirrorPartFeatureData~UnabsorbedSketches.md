# UnabsorbedSketches Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~UnabsorbedSketches`

Gets or sets whether to import unabsorbed sketches.
Gets or sets whether to import unabsorbed sketches.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UnabsorbedSketches As System.Boolean
```

```

Dim instance As IMirrorPartFeatureData
Dim value As System.Boolean
 
instance.UnabsorbedSketches = value
 
value = instance.UnabsorbedSketches
```

```

System.bool UnabsorbedSketches {get; set;}
```

```

property System.bool UnabsorbedSketches {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to import unabsorbed sketches, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMirrorPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData.md)  
[IMirrorPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData_members.md)  
[IMirrorPartFeatureData::AbsorbedSketches Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~AbsorbedSketches.md)
