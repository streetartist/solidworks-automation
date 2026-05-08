# Display3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Display3`

Displays this temporary body in the context of the specified part or component.
Displays this temporary body in the context of the specified part or component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Display3( _
   ByVal Component As System.Object, _
   ByVal Color As System.Integer, _
   ByVal Option As System.Integer _
) As System.Integer
```

```

Dim instance As IBody2
Dim Component As System.Object
Dim Color As System.Integer
Dim Option As System.Integer
Dim value As System.Integer
 
value = instance.Display3(Component, Color, Option)
```

```

System.int Display3( 
   System.object Component,
   System.int Color,
   System.int Option
)
```

```

System.int Display3( 
   System.Object^ Component,
   System.int Color,
   System.int Option
) 
```

#### Parameters

*Component*
:   Part or component where the temporary body exists (see **Remarks**)

*Color*
:   COLORREF value (see **Remarks**)

*Option*
:   Selection state of temporary body as defined by [swTempBodySelectOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTempBodySelectOptions_e.html) (see **Remarks**)

#### Return Value

- 0 = Success
- 1 = Failed because this body is not a temporary body
- 2 = Invalid component
- 3 = Not a part instance

Remarks

This method:

- Is valid only for temporary bodies. To determine whether a body is temporary, use [IBody2::IsTemporaryBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IsTemporaryBody.md).
- Applies Color to this temporary body in the graphics area, effectively selecting it.

You can also use [IBody2::MaterialPropertyValues2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~MaterialPropertyValues2.md) to change the appearance of this temporary body.

Component cannot be in a subassembly.

Specifying Option with swTempBodySelectable sets the blocking state to [swBlockingStates\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBlockingStates_e.html).swModifyBlock. Unset the blocking state by calling [IBody2::Hide](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Hide.md).

Example

[Create Loft Body (VB.NET)](Create_Loft_Body_Example_VBNET.htm)  
[Create Loft Body (VBA)](Create_Loft_Body_Example_VB.htm)  
[Create Loft Body (C#)](Create_Loft_Body_Example_CSharp.htm)  
[Display Temporary Body (C#)](Display_Temporary_Body_Example_CSharp.htm)  
[Display Temporary Body (VB.NET)](Display_Temporary_Body_Example_VBNET.htm)  
[Display Temporary Body (VBA)](Display_Temporary_Body_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)
