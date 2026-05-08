# GetPosition Method (ICenterMark)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~GetPosition`

Gets the x, y, and z coordinates for the specified center mark.
Gets the x, y, and z coordinates for the specified center mark.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPosition( _
   ByVal Index As System.Integer _
) As System.Object
```

```

Dim instance As ICenterMark
Dim Index As System.Integer
Dim value As System.Object
 
value = instance.GetPosition(Index)
```

```

System.object GetPosition( 
   System.int Index
)
```

```

System.Object^ GetPosition( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of the center mark (see **Remarks**)

#### Return Value

Array of three doubles of the x, y, and z coordinates of the center mark specified by Index

Remarks

This method is available to center marks in a center mark set and center marks in an array of center marks.

Use:

- [ICenterMark::IsGrouped](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~IsGrouped.md) to determine if the center mark is in a center mark set (i.e., a linear or circular pattern)
- [ICenterMark::GroupCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~GroupCount.md) to get a valid value for Index for a center mark in a center mark set.

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
