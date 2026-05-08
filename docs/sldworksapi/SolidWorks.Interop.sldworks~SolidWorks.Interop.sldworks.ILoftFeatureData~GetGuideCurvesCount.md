# GetGuideCurvesCount Method (ILoftFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GetGuideCurvesCount`

Gets the number of guide curves for this loft feature.
Gets the number of guide curves for this loft feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetGuideCurvesCount() As System.Short
```

```

Dim instance As ILoftFeatureData
Dim value As System.Short
 
value = instance.GetGuideCurvesCount()
```

```

System.short GetGuideCurvesCount()
```

```

System.short GetGuideCurvesCount(); 
```

#### Return Value

Number of guide curves

Remarks

Call this method before calling [ILoftFeatureData::IGetGuideCurves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~IGetGuideCurves.md) to determine the size of the array for that method.

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
[ILoftFeatureData::GetGuideCurvesType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GetGuideCurvesType.md)  
[ILoftFeatureData::IGetGuideCurvesType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~IGetGuideCurvesType.md)  
[ILoftFeatureData::ISetGuideCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~ISetGuideCurves.md)  
[ILoftFeatureData::GuideCurveInfluence Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GuideCurveInfluence.md)  
[ILoftFeatureData::GuideCurves Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GuideCurves.md)  
[ILoftFeatureData::GetGuideTangencyType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GetGuideTangencyType.md)  
[ILoftFeatureData::SetGuideTangencyType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~SetGuideTangencyType.md)
