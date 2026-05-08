# GetRegionParameterAtIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~GetRegionParameterAtIndex`

Gets the specified parameter value for the specified region in this variable-pitch helix.
Gets the specified parameter value for the specified region in this variable-pitch helix.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRegionParameterAtIndex( _
   ByVal Index As System.Integer, _
   ByVal RegionParameter As System.Integer _
) As System.Double
```

```

Dim instance As IHelixFeatureData
Dim Index As System.Integer
Dim RegionParameter As System.Integer
Dim value As System.Double
 
value = instance.GetRegionParameterAtIndex(Index, RegionParameter)
```

```

System.double GetRegionParameterAtIndex( 
   System.int Index,
   System.int RegionParameter
)
```

```

System.double GetRegionParameterAtIndex( 
   System.int Index,
   System.int RegionParameter
) 
```

#### Parameters

*Index*
:   Index of the region

*RegionParameter*
:   Region parameter as defined in [swVariablePitchHelixRegionParameter\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swVariablePitchHelixRegionParameter_e.html)

#### Return Value

Region parameter value

Example

[Create and Modify Variable-pitch Helix (C#)](Create_and_Modify_Variable-pitch_Helix_Example_CSharp.htm)  
[Create and Modify Variable-pitch Helix (VB.NET)](Create_and_Modify_Variable-pitch_Helix_Example_VBNET.htm)  
[Create and Modify Variable-pitch Helix (VBA)](Create_and_Modify_Variable-pitch_Helix_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHelixFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData.md)  
[IHelixFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData_members.md)  
[IHelixFeatureData::VariablePitch Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~VariablePitch.md)  
[IHelixFeatureData::PitchCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~PitchCount.md)  
[IHelixFeatureData::SetRegionParameterAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~SetRegionParameterAtIndex.md)  
[IHelixFeatureData::InsertRecord Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~InsertRecord.md)  
[IHelixFeatureData::DeleteRecord Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~DeleteRecord.md)  
[IHelixFeatureData::AddLastRecord Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~AddLastRecord.md)
