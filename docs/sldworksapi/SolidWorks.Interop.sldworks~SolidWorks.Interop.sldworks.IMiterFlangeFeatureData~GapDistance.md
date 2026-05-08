# GapDistance Property (IMiterFlangeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~GapDistance`

Gets or sets the gap distance of the tear for this miter flange feature.
Gets or sets the gap distance of the tear for this miter flange feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property GapDistance As System.Double
```

```

Dim instance As IMiterFlangeFeatureData
Dim value As System.Double
 
instance.GapDistance = value
 
value = instance.GapDistance
```

```

System.double GapDistance {get; set;}
```

```

property System.double GapDistance {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Distance in meters between edges in the miter flange

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMiterFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData.md)  
[IMiterFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData_members.md)
