# MergeSmoothFaces Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~MergeSmoothFaces`

Gets or sets whether to merge the smooth faces of this sweep feature that uses guide curves.
Gets or sets whether to merge the smooth faces of this sweep feature that uses guide curves.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MergeSmoothFaces As System.Boolean
```

```

Dim instance As ISweepFeatureData
Dim value As System.Boolean
 
instance.MergeSmoothFaces = value
 
value = instance.MergeSmoothFaces
```

```

System.bool MergeSmoothFaces {get; set;}
```

```

property System.bool MergeSmoothFaces {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to merge the smooth faces, false to not (see **Remarks**)

Remarks

This property corresponds to the Merge smooth faces check box on the Guide Curves group box on the Sweep PropertyManager.

Setting this property to false improves the performance of sweeps with guide curves and segments the sweep at all points where the guide curve or path is not curvature continuous.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.md)  
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.md)  
[ISweepFeatureData::GetGuideCurvesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetGuideCurvesCount.md)  
[ISweepFeatureData::GetGuideCurvesType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetGuideCurvesType.md)  
[ISweepFeatureData::IGetGuideCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~IGetGuideCurves.md)  
[ISweepFeatureData::IGetGuideCurvesType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~IGetGuideCurvesType.md)  
[ISweepFeatureData::ISetGuideCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~ISetGuideCurves.md)  
[ISweepFeatureData::GuideCurves Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GuideCurves.md)
