# HasDetachCenterMark Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~HasDetachCenterMark`

Gets whether the selected center mark set contains any detached center marks.
Gets whether the selected center mark set contains any detached center marks.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function HasDetachCenterMark() As System.Boolean
```

```

Dim instance As ICenterMark
Dim value As System.Boolean
 
value = instance.HasDetachCenterMark()
```

```

System.bool HasDetachCenterMark()
```

```

System.bool HasDetachCenterMark(); 
```

#### Return Value

True if the selected center mark set contains any detached center marks, false if not

Remarks

You must select the center mark set before calling this method. To determine if a center mark is in a center mark set (i.e., a linear or circular pattern), use [ICenterMark::IsGrouped](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~IsGrouped.md).

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
[ICenterMark::IsDetached Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~IsDetached.md)  
[ICenterMark::ReattachToCenterMarkGroup Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~ReattachToCenterMarkGroup.md)  
[ICenterMark::AddToCenterMarkGroup Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~AddToCenterMarkGroup.md)
