# SetExtendedLength Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~SetExtendedLength`

Sets the extended length of this center mark.
Sets the extended length of this center mark.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetExtendedLength( _
   ByVal GroupID As System.Integer, _
   ByVal HandleID As System.Integer, _
   ByVal ExtendedLength As System.Double _
) As System.Boolean
```

```

Dim instance As ICenterMark
Dim GroupID As System.Integer
Dim HandleID As System.Integer
Dim ExtendedLength As System.Double
Dim value As System.Boolean
 
value = instance.SetExtendedLength(GroupID, HandleID, ExtendedLength)
```

```

System.bool SetExtendedLength( 
   System.int GroupID,
   System.int HandleID,
   System.double ExtendedLength
)
```

```

System.bool SetExtendedLength( 
   System.int GroupID,
   System.int HandleID,
   System.double ExtendedLength
) 
```

#### Parameters

*GroupID*
:   Instance of center mark (see Remarks)

*HandleID*
:   Center mark handle ID as defined by [swCenterMarkHandle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCenterMarkHandle_e.html)

*ExtendedLength*
:   Extended length of HandleID

#### Return Value

True if the extended length of the specified center mark is set, false if not

Remarks

If the center mark is in a center mark set (i.e., a linear or circular pattern), then use [ICenterMark::GroupCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~GroupCount.md) to get the range of valid values for the GroupID parameter. You can use a value from 0 to ICenterMark::GroupCount for the GroupID parameter. To determine if a center mark is in a center mark set, use [ICenterMark::IsGrouped](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~IsGrouped.md).

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
[ICenterMark::GetExtendedLength Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~GetExtendedLength.md)
