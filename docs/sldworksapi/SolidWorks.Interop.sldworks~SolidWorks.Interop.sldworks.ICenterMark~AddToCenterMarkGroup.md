# AddToCenterMarkGroup Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~AddToCenterMarkGroup`

Adds a center mark for the selected entity in an existing center mark set.
Adds a center mark for the selected entity in an existing center mark set.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddToCenterMarkGroup() As System.Boolean
```

```

Dim instance As ICenterMark
Dim value As System.Boolean
 
value = instance.AddToCenterMarkGroup()
```

```

System.bool AddToCenterMarkGroup()
```

```

System.bool AddToCenterMarkGroup(); 
```

#### Return Value

True if a center mark is added for the selected entity in an existing center mark set, false if not (see **Remarks**)

Remarks

You must pre-select an entity in an existing center mark set (i.e., a linear or circular pattern) for which to add a center mark. If the existing center mark set is a linear pattern, then the selected entity must be in that linear pattern, else this method fails. The same rule applies when adding an entity to an existing center mark set that is a circular pattern.

To determine if a center mark is in a center mark set, use [ICenterMark::IsGrouped](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~IsGrouped.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.md)  
[ICenterMark Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark_members.md)  
[ICenterMark::GroupCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~GroupCount.md)  
[ICenterMark::HasDetachCenterMark Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~HasDetachCenterMark.md)  
[ICenterMark::IsDetached Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~IsDetached.md)  
[ICenterMark::ReattachToCenterMarkGroup Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~ReattachToCenterMarkGroup.md)
