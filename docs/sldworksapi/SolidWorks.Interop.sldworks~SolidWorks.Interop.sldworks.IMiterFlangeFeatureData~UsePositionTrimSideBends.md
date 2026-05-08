# UsePositionTrimSideBends Property (IMiterFlangeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~UsePositionTrimSideBends`

Gets or sets whether to remove extra material in neighboring bends for this miter flange feature.
Gets or sets whether to remove extra material in neighboring bends for this miter flange feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UsePositionTrimSideBends As System.Boolean
```

```

Dim instance As IMiterFlangeFeatureData
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

True to remove extra material in neighboring bends, false to not remove material

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMiterFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData.md)  
[IMiterFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData_members.md)
