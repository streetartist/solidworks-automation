# IsDeleted Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~IsDeleted`

Gets whether the specified center mark is deleted in this center mark set.
Gets whether the specified center mark is deleted in this center mark set.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsDeleted( _
   ByVal Index As System.Integer _
) As System.Boolean
```

```

Dim instance As ICenterMark
Dim Index As System.Integer
Dim value As System.Boolean
 
value = instance.IsDeleted(Index)
```

```

System.bool IsDeleted( 
   System.int Index
)
```

```

System.bool IsDeleted( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of the center mark in the center mark set (see **Remarks**)

#### Return Value

True if the specified center mark in this center mark set is deleted, false if not

Remarks

You can use a value from 0 to the [number of center marks in a center mark set](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~GroupCount.md) for the Index parameter.

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
