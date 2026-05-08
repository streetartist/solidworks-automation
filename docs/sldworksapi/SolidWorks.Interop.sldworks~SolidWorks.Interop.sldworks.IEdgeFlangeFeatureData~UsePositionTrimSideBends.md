# UsePositionTrimSideBends Property (IEdgeFlangeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~UsePositionTrimSideBends`

Gets or sets whether to trim side bends for this edge flange.
Gets or sets whether to trim side bends for this edge flange.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UsePositionTrimSideBends As System.Boolean
```

```

Dim instance As IEdgeFlangeFeatureData
Dim value As System.Boolean
 
instance.UsePositionTrimSideBends = value
 
value = instance.UsePositionTrimSideBends
```

```

System.bool UsePositionTrimSideBends {get; set;}
```

```

property System.bool UsePositionTrimSideBends {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True trims side bends, false does not (default)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.md)  
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.md)  
[IEdgeFlangeFeatureData::GetPositionReferenceType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~GetPositionReferenceType.md)  
[IEdgeFlangeFeatureData::PositionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~PositionType.md)
