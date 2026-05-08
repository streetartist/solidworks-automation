# GroupCount Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~GroupCount`

Gets the number of center marks in a center mark set.
Gets the number of center marks in a center mark set.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property GroupCount As System.Integer
```

```

Dim instance As ICenterMark
Dim value As System.Integer
 
value = instance.GroupCount
```

```

System.int GroupCount {get;}
```

```

property System.int GroupCount {
   System.int get();
}
```

#### Property Value

Number of center marks in a center mark set

Remarks

If the center mark is in a center mark set (i.e., a linear or circular pattern), then:

- you can only change the length of the arms of any of the center marks in that pattern; you cannot change any other properties of those center marks. Call [ICenterMark::IsGrouped](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~IsGrouped.md) to determine if a center mark is in a center mark set.
- use this property to get a range of valid values for [ICenterMark::GetExtendedLength](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~GetExtendedLength.md)'s and [ICenterMark::SetExtendedLength](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~SetExtendedLength.md)'s GroupID parameter. You can use a value from 0 to the number of center marks in a center mark set for the GroupID parameter.

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
