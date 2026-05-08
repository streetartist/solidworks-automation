# Clearance Property (IIndentFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~Clearance`

Gets or sets the clearance between the target and tool bodies in this indent feature.
Gets or sets the clearance between the target and tool bodies in this indent feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Clearance As System.Double
```

```

Dim instance As IIndentFeatureData
Dim value As System.Double
 
instance.Clearance = value
 
value = instance.Clearance
```

```

System.double Clearance {get; set;}
```

```

property System.double Clearance {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Clearance between the target and tool bodies

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IIndentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData.md)  
[IIndentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData_members.md)  
[IIndentFeatureData::ClearanceDirection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~ClearanceDirection.md)  
[IIndentFeatureData::TargetBody Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~TargetBody.md)  
[IIndentFeatureData::ToolBodyRegion Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~ToolBodyRegion.md)
