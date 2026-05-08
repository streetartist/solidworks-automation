# ClearanceDirection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~ClearanceDirection`

Gets or sets the direction of the clearance for this indent feature.
Gets or sets the direction of the [clearance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~Clearance.md) for this indent feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ClearanceDirection As System.Boolean
```

```

Dim instance As IIndentFeatureData
Dim value As System.Boolean
 
instance.ClearanceDirection = value
 
value = instance.ClearanceDirection
```

```

System.bool ClearanceDirection {get; set;}
```

```

property System.bool ClearanceDirection {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to reverse the direction of clearance, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IIndentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData.md)  
[IIndentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData_members.md)
