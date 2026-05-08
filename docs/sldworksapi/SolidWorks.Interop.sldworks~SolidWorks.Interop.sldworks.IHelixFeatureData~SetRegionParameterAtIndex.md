# SetRegionParameterAtIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~SetRegionParameterAtIndex`

Sets the specified parameter for the specified region in this variable-pitch helix.
Sets the specified parameter for the specified region in this variable-pitch helix.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetRegionParameterAtIndex( _
   ByVal Index As System.Integer, _
   ByVal Parameter As System.Integer, _
   ByVal PitchValue As System.Double _
) As System.Integer
```

```

Dim instance As IHelixFeatureData
Dim Index As System.Integer
Dim Parameter As System.Integer
Dim PitchValue As System.Double
Dim value As System.Integer
 
value = instance.SetRegionParameterAtIndex(Index, Parameter, PitchValue)
```

```

System.int SetRegionParameterAtIndex( 
   System.int Index,
   System.int Parameter,
   System.double PitchValue
)
```

```

System.int SetRegionParameterAtIndex( 
   System.int Index,
   System.int Parameter,
   System.double PitchValue
) 
```

#### Parameters

*Index*
:   Index of the region

*Parameter*
:   Region parameter as defined in [swVariablePitchHelixRegionParameter\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swVariablePitchHelixRegionParameter_e.html) (see **Remarks**)

*PitchValue*
:   Region parameter value

#### Return Value

Status of setting region parameters as defined in [swSetHelixRegionParameterStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSetHelixRegionParameterStatus_e.html)

Remarks

|  |  |
| --- | --- |
| **If the [helix is defined](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~DefinedBy.md) as...** | **Then you cannot change...** |
| swHelixDefinedBy\_e.swHelixDefinedByHeightAndPitch | Revolution value |
| swHelixDefinedBy\_e.swHelixDefinedByHeightAndRevolution | Pitch value |
| swHelixDefinedBy\_e.swHelixDefinedByPitchAndRevolution | Height value |

|  |  |
| --- | --- |
| **If setting a value for...** | **Then you...** |
| Revolution | Must specify a value greater than the previous region's revolution value and less than the next region's revolution value |
| Pitch for the first region only | Cannot change diameter, height, or revolution |

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
[IHelixFeatureData::GetRegionParameterAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~GetRegionParameterAtIndex.md)  
[IHelixFeatureData::InsertRecord Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~InsertRecord.md)  
[IHelixFeatureData::DeleteRecord Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~DeleteRecord.md)  
[IHelixFeatureData::AddLastRecord Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~AddLastRecord.md)
