# MaintainTangency Property (ILoftFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~MaintainTangency`

Gets or sets whether to maintain tangency for this loft feature.
Gets or sets whether to maintain tangency for this loft feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MaintainTangency As System.Boolean
```

```

Dim instance As ILoftFeatureData
Dim value As System.Boolean
 
instance.MaintainTangency = value
 
value = instance.MaintainTangency
```

```

System.bool MaintainTangency {get; set;}
```

```

property System.bool MaintainTangency {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True maintains tangency, false does not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.md)  
[ILoftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.md)  
[ILoftFeatureData::GetGuideTangencyType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GetGuideTangencyType.md)  
[ILoftFeatureData::SetGuideTangencyType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~SetGuideTangencyType.md)  
[ILoftFeatureData::EndConstraintApplyToAll Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~EndConstraintApplyToAll.md)  
[ILoftFeatureData::EndConstraintDraftAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~EndConstraintDraftAngle.md)  
[ILoftFeatureData::EndConstraintDraftAngleDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~EndConstraintDraftAngleDirection.md)  
[ILoftFeatureData::EndTangencyType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~EndTangencyType.md)  
[ILoftFeatureData::EndTangentLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~EndTangentLength.md)  
[ILoftFeatureData::ReverseEndTangentDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~ReverseEndTangentDirection.md)  
[ILoftFeatureData::ReverseStartTangentDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~ReverseStartTangentDirection.md)  
[ILoftFeatureData::StartConstraintApplyToAll Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~StartConstraintApplyToAll.md)  
[ILoftFeatureData::StartConstraintDraftAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~StartConstraintDraftAngle.md)  
[ILoftFeatureData::StartConstraintDraftAngleDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~StartConstraintDraftAngleDirection.md)  
[ILoftFeatureData::StartTangencyType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~StartTangencyType.md)  
[ILoftFeatureData::StartTangentLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~StartTangentLength.md)
