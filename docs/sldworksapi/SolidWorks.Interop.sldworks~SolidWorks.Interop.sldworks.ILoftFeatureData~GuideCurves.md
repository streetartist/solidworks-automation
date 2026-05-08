# GuideCurves Property (ILoftFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GuideCurves`

Gets and sets the guide curves for this loft feature.
Gets and sets the guide curves for this loft feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property GuideCurves As System.Object
```

```

Dim instance As ILoftFeatureData
Dim value As System.Object
 
instance.GuideCurves = value
 
value = instance.GuideCurves
```

```

System.object GuideCurves {get; set;}
```

```

property System.Object^ GuideCurves {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of [features](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) of guide curves

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Example

[Get Guide Curves in Loft Feature (C#)](Get_Guide_Curves_in_Loft_Feature_Example_CSharp.htm)  
[Get Guide Curves in Loft Feature (VB.NET)](Get_Guide_Curves_in_Loft_Feature_Example_VBNET.htm)  
[Get Guide Curves in Loft Feature (VBA)](Get_Guide_Curves_in_Loft_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.md)  
[ILoftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.md)  
[ILoftFeatureData::GetGuideCurvesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GetGuideCurvesCount.md)  
[ILoftFeatureData::GetGuideCurvesType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GetGuideCurvesType.md)  
[ILoftFeatureData::GetGuideTangencyType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GetGuideTangencyType.md)  
[ILoftFeatureData::IGetGuideCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~IGetGuideCurves.md)  
[ILoftFeatureData::IGetGuideCurvesType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~IGetGuideCurvesType.md)  
[ILoftFeatureData::ISetGuideCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~ISetGuideCurves.md)  
[ILoftFeatureData::SetGuideTangencyType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~SetGuideTangencyType.md)  
[ILoftFeatureData::GuideCurveInfluence Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GuideCurveInfluence.md)
