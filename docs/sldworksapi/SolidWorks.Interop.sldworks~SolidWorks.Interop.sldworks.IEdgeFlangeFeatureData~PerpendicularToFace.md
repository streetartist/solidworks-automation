# PerpendicularToFace Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~PerpendicularToFace`

Gets or sets whether to set this edge flange perpendicular to the angle reference face.
Gets or sets whether to set this edge flange perpendicular to the angle reference face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PerpendicularToFace As System.Boolean
```

```

Dim instance As IEdgeFlangeFeatureData
Dim value As System.Boolean
 
instance.PerpendicularToFace = value
 
value = instance.PerpendicularToFace
```

```

System.bool PerpendicularToFace {get; set;}
```

```

property System.bool PerpendicularToFace {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to set this edge flange perpendicular to the angle reference face, false to set it parallel to the angle reference face (default)

Remarks

This property is valid only if [IEdgeFlangeFeatureData::AngleReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~AngleReference.md) is not null.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.md)  
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.md)
