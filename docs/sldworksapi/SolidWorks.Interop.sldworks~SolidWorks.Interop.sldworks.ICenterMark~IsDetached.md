# IsDetached Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~IsDetached`

Gets whether the specified center mark is detached.
Gets whether the specified center mark is detached.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsDetached( _
   ByVal Index As System.Integer _
) As System.Boolean
```

```

Dim instance As ICenterMark
Dim Index As System.Integer
Dim value As System.Boolean
 
value = instance.IsDetached(Index)
```

```

System.bool IsDetached( 
   System.int Index
)
```

```

System.bool IsDetached( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of center mark (see **Remarks**)

#### Return Value

True if the center mark specified by Index is detached, false if not

Remarks

This method is available to center marks in a center mark set and center marks in an array of center marks.

Use:

- [ICenterMark::IsGrouped](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~IsGrouped.md) to determine if the center mark is in a center mark set (i.e., a linear or circular pattern).
- [ICenterMark::GroupCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~GroupCount.md) to get a valid value for Index for a center mark in a center mark set.

Use [ICenterMark::ReattachToCenterMarkGroup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~ReattachToCenterMarkGroup.md) to reattach a detached center mark in a center mark set. You cannot reattach a detached center mark that is not in a center mark set.

Example

[Get and Set Center Mark Set (C#)](Get_and_Set_Center_Marks_Set_Example_CSharp.htm)  
[Get and Set Center Mark Set (VB.NET)](Get_and_Set_Center_Marks_Set_Example_VBNET.htm)  
[Get and Set Center Mark Set (VBA)](Get_and_Set_Center_Marks_Set_Example_VBA.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.md)  
[ICenterMark Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark_members.md)  
[ICenterMark::IsGrouped Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~IsGrouped.md)  
[ICenterMark::GroupCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~GroupCount.md)  
[ICenterMark::HasDetachCenterMark Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~HasDetachCenterMark.md)  
[ICenterMark::ReattachToCenterMarkGroup Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~ReattachToCenterMarkGroup.md)  
[ICenterMark::AddToCenterMarkGroup Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~AddToCenterMarkGroup.md)
