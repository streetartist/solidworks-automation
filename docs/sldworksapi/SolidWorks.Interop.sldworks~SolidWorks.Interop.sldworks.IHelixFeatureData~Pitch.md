# Pitch Property (IHelixFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~Pitch`

Gets or sets the pitch of this helix feature.
Gets or sets the pitch of this helix feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Pitch As System.Double
```

```

Dim instance As IHelixFeatureData
Dim value As System.Double
 
instance.Pitch = value
 
value = instance.Pitch
```

```

System.double Pitch {get; set;}
```

```

property System.double Pitch {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Pitch (see **Remarks**)

Remarks

|  |  |
| --- | --- |
| **For...** | **This property sets...** |
| Helixes | Distance between turns |
| Spirals | Radial distance between revolutions of the curve |

**NOTES**:

- If the [helix is defined](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~DefinedBy.md) as swHelixDefinedBy\_e.swHelixDefinedByHeightAndRevolution, then you cannot change the pitch of the helix.
- If setting a value for pitch for the first region only, then you cannot change diameter, height, or revolution.

Example

[Change Pitch of Helix (C#)](Change_Pitch_of_Helix_Example_CSharp.htm)  
[Change Pitch of Helix (VB.NET)](Change_Pitch_of_Helix_Example_VBNET.htm)  
[Change Pitch of Helix (VBA)](Change_Pitch_of_Helix_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHelixFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData.md)  
[IHelixFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData_members.md)
