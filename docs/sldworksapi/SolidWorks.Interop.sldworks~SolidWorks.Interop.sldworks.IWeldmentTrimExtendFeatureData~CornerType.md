# CornerType Property (IWeldmentTrimExtendFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~CornerType`

Gets or sets the corner type.
Gets or sets the corner type.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CornerType As System.Integer
```

```

Dim instance As IWeldmentTrimExtendFeatureData
Dim value As System.Integer
 
instance.CornerType = value
 
value = instance.CornerType
```

```

System.int CornerType {get; set;}
```

```

property System.int CornerType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of corner as defined in [swSolidworksWeldmentEndCondOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSolidworksWeldmentEndCondOptions_e.html) (see Remarks)

Remarks

You must set the bodies to trim and the trimming boundary when changing the corner type.

Valid values for type are:

- swEndConditionButt1
- swEndConditionButt2
- swEndConditionMiter
- swEndConditionTrim

These values are not valid for type:

- swEndConditionNone
- swEndConditionUseDefault

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

See the [IWeldmentTrimExtendFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldmentTrimExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData.md)  
[IWeldmentTrimExtendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData_members.md)  
[IWeldmentTrimExtendFeatureData::BodiesToBeTrimmed Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~BodiesToBeTrimmed.md)  
[IWeldmentTrimExtendFeatureData::ISetBodiesToBeTrimmed Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~ISetBodiesToBeTrimmed.md)  
[IWeldmentTrimExtendFeatureData::IGetBodiesToBeTrimmed Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~IGetBodiesToBeTrimmed.md)  
[IWeldmentTrimExtendFeatureData::GetTrimmingBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~GetTrimmingBoundary.md)  
[IWeldmentTrimExtendFeatureData::IGetTrimmingBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~IGetTrimmingBoundary.md)  
[IWeldmentTrimExtendFeatureData::ISetTrimmingBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~ISetTrimmingBoundary.md)  
[IWeldmentTrimExtendFeatureData::SetTrimmingBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~SetTrimmingBoundary.md)
