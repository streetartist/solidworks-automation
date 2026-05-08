# GapDistance Property (IEdgeFlangeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~GapDistance`

Gets or sets the gap distance of the tear for this edge flange.
Gets or sets the gap distance of the tear for this edge flange.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property GapDistance As System.Double
```

```

Dim instance As IEdgeFlangeFeatureData
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

Distance in meters between the edges in the flange; default value is 0.001 m

Example

See the [IEdgeFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.md)  
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.md)
