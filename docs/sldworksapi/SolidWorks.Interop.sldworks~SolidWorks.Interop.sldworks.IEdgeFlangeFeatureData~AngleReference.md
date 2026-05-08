# AngleReference Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~AngleReference`

Gets or sets the reference face used to define the bend angle of this edge flange.
Gets or sets the reference face used to define the bend angle of this edge flange.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AngleReference As System.Object
```

```

Dim instance As IEdgeFlangeFeatureData
Dim value As System.Object
 
instance.AngleReference = value
 
value = instance.AngleReference
```

```

System.object AngleReference {get; set;}
```

```

property System.Object^ AngleReference {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Reference [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.md)  
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.md)  
[IEdgeFlangeFeatureData::PerpendicularToFace Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~PerpendicularToFace.md)
