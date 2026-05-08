# DiameterOverride Property (IThreadFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~DiameterOverride`

Gets or sets whether to override the diameter of the cylindrical face or helix of this thread feature.
Gets or sets whether to override the diameter of the cylindrical face or helix of this thread feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DiameterOverride As System.Boolean
```

```

Dim instance As IThreadFeatureData
Dim value As System.Boolean
 
instance.DiameterOverride = value
 
value = instance.DiameterOverride
```

```

System.bool DiameterOverride {get; set;}
```

```

property System.bool DiameterOverride {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to override the diameter, false to not (default)

Remarks

If this property is set to true, use [IThreadFeatureData::Diameter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~Diameter.md) to specify the override diameter.

Example

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md)  
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.md)
