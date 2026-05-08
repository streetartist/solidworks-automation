# SetAutoHatch Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetAutoHatch`

Sets whether auto hatching is enabled for the section view resulting from this section cut.
Sets whether auto hatching is enabled for the section view resulting from this section cut.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetAutoHatch( _
   ByVal AutoHatch As System.Boolean _
) 
```

```

Dim instance As IDrSection
Dim AutoHatch As System.Boolean
 
instance.SetAutoHatch(AutoHatch)
```

```

void SetAutoHatch( 
   System.bool AutoHatch
)
```

```

void SetAutoHatch( 
   System.bool AutoHatch
) 
```

#### Parameters

*AutoHatch*
:   True enables auto hatching for the section view, false disables it

Remarks

Automatic hatching applies only to assembly section views. For section views of parts, this method has no effect.

When the auto hatching setting is changed, regenerate the section view to see the results of this change in the user interface.

Example

[Create Section View and Get Some Data (C#)](Create_Section_View_and_Get_Some_Data_Example_CSharp.htm)  
[Create Section View and Get Some Data (VB.NET)](Create_Section_View_and_Get_Some_Data_Example_VBNET.htm)  
[Create Section View and Get Some Data (VBA)](Create_Section_View_and_Get_Some_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md)  
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.md)  
[IDrSection::GetAutoHatch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetAutoHatch.md)  
[IDrSection::ScaleHatchPattern Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~ScaleHatchPattern.md)
