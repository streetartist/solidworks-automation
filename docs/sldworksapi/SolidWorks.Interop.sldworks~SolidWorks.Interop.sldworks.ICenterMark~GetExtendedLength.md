# GetExtendedLength Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~GetExtendedLength`

Gets the extended length of the specified arm (handle) of this center mark.
Gets the extended length of the specified arm (handle) of this center mark.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetExtendedLength( _
   ByVal GroupID As System.Integer, _
   ByVal HandleID As System.Integer _
) As System.Double
```

```

Dim instance As ICenterMark
Dim GroupID As System.Integer
Dim HandleID As System.Integer
Dim value As System.Double
 
value = instance.GetExtendedLength(GroupID, HandleID)
```

```

System.double GetExtendedLength( 
   System.int GroupID,
   System.int HandleID
)
```

```

System.double GetExtendedLength( 
   System.int GroupID,
   System.int HandleID
) 
```

#### Parameters

*GroupID*
:   Center mark instance (see Remarks)

*HandleID*
:   Center mark handle ID as defined in [swCenterMarkHandle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCenterMarkHandle_e.html)

#### Return Value

Extended length of the HandleID

Remarks

If the center mark is in a center mark set (i.e., a linear or circular pattern), then use [ICenterMark::GroupCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~GroupCount.md) to get the range of valid values for the GroupID parameter. You can use a value from 0 to ICenterMark::GroupCount for the GroupID parameter. To determine if a center mark is in a center mark set, use [ICenterMark::IsGrouped](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~IsGrouped.md).

Example

[Extend Arms of Center Mark (VBA)](Extend_Arms_of_Center_Mark_Examples_VB.htm)  
[Get and Set Center Mark Set (C#)](Get_and_Set_Center_Marks_Set_Example_CSharp.htm)  
[Get and Set Center Mark Set (VB.NET)](Get_and_Set_Center_Marks_Set_Example_VBNET.htm)  
[Get and Set Center Mark Set (VBA)](Get_and_Set_Center_Marks_Set_Example_VBA.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.md)  
[ICenterMark Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark_members.md)  
[ICenterMark::SetExtendedLength Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~SetExtendedLength.md)
