# AddLastRecord Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~AddLastRecord`

Adds a region to the end of the Region parameters table of this variable-pitch helix.
Adds a region to the end of the Region parameters table of this variable-pitch helix.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddLastRecord( _
   ByVal HelixPointValue As System.Object _
) As System.Boolean
```

```

Dim instance As IHelixFeatureData
Dim HelixPointValue As System.Object
Dim value As System.Boolean
 
value = instance.AddLastRecord(HelixPointValue)
```

```

System.bool AddLastRecord( 
   System.object HelixPointValue
)
```

```

System.bool AddLastRecord( 
   System.Object^ HelixPointValue
) 
```

#### Parameters

*HelixPointValue*
:   Array of four doubles for the region to add to the end of the Region parameters table (see **Remarks**)

#### Return Value

True if the region is added to the end of the Region parameters table, false if not

Remarks

The values in the array specified for HelixPointValue depends on the type of variable-pitch helix:

|  |  |
| --- | --- |
| **Helix type** | **Array of doubles in this order** |
| Pitch and revolution | Pitch, number of revolutions, 0, diameter |
| Height and revolution | Height, number of revolutions, 0, diameter |
| Height and pitch | Height, pitch, 0, diameter |

**NOTE:** You must specify 0 for any element that SOLIDWORKS calculates.

To insert a record at a specific index in the Region parameters table (i.e., between existing records) of this variable-pitch helix, use [IHelixFeatureData::InsertRecord](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~InsertRecord.md).

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
[IHelixFeatureData::DeleteRecord Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~DeleteRecord.md)  
[IHelixFeatureData::GetRegionParameterAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~GetRegionParameterAtIndex.md)  
[IHelixFeatureData::SetRegionParameterAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~SetRegionParameterAtIndex.md)  
[IHelixFeatureData::PitchCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~PitchCount.md)  
[IHelixFeatureData::VariablePitch Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~VariablePitch.md)
