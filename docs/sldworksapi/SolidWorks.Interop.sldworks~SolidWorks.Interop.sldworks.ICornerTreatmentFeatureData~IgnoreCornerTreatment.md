# IgnoreCornerTreatment Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentFeatureData~IgnoreCornerTreatment`

Gets and sets whether to ignore this corner treatment.
Gets and sets whether to ignore this corner treatment.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IgnoreCornerTreatment As System.Boolean
```

```

Dim instance As ICornerTreatmentFeatureData
Dim value As System.Boolean
 
instance.IgnoreCornerTreatment = value
 
value = instance.IgnoreCornerTreatment
```

```

System.bool IgnoreCornerTreatment {get; set;}
```

```

property System.bool IgnoreCornerTreatment {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to ignore the corner treatment, false to not

Example

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICornerTreatmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentFeatureData.md)  
[ICornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentFeatureData_members.md)
