# ReattachToCenterMarkGroup Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~ReattachToCenterMarkGroup`

Reattaches the specified center mark to the selected entity in a center mark set.
Reattaches the specified center mark to the selected entity in a center mark set.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ReattachToCenterMarkGroup( _
   ByVal Index As System.Integer _
) As System.Boolean
```

```

Dim instance As ICenterMark
Dim Index As System.Integer
Dim value As System.Boolean
 
value = instance.ReattachToCenterMarkGroup(Index)
```

```

System.bool ReattachToCenterMarkGroup( 
   System.int Index
)
```

```

System.bool ReattachToCenterMarkGroup( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of center mark (see **Remarks**)

#### Return Value

True if the center mark specified by Index is reattached to the selected entity in a center mark set, false if not

Remarks

You must pre-select an entity in an existing center mark set (i.e., a linear or circular pattern) for which to reattach the center mark. If the existing center mark set is a linear pattern, then the selected entity must be in that linear pattern, else this method fails. The same rule applies when reattaching an entity to an existing center mark set that is a circular pattern.

Use:

- [ICenterMark::IsGrouped](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~IsGrouped.md) to determine if the center mark is in a center mark set (i.e., a linear or circular pattern).
- [ICenterMark::GroupCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~GroupCount.md) to get a valid value for Index for a center mark in a center mark set.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.md)  
[ICenterMark Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark_members.md)  
[ICenterMark::HasDetachCenterMark Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~HasDetachCenterMark.md)  
[ICenterMark::IsDetached Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~IsDetached.md)  
[ICenterMark::IsGrouped Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~IsGrouped.md)
